import requests
import time
import xml.etree.ElementTree as ET
import json
import textwrap
from pdf_generator import generate_timetable_pdf
from tqdm import tqdm

def welcome_animation():
    """
    Displays a welcome animation in the console.

    This function clears the console, prints a framed welcome message,
    and animates the printing of the author's name character by character.
    It uses time.sleep to create the animation effect.
    """
    message = "Time-Table-Finder"
    author = "Made by S.I.F.A.R"
    animation_delay = 0.05  # Delay between each character animation
    
    # Clear the console (if supported)
    print("\033c", end="")
    
    # Print the message with animation
    print("+" + "-" * (len(message) + 2) + "+")
    print("| " + message.upper() + " |")
    print("+" + "-" * (len(message) + 2) + "+")
    time.sleep(1)  # Pause for 1 second
    
    # Print the author name with animation
    for char in author:
        print(char, end="", flush=True)
        time.sleep(animation_delay)
    
    print("\n")

def wrap_text(text, width):
    """
    Wraps text into a list of strings of a specified width.

    Args:
        text (str): The input text string to be wrapped.
        width (int): The maximum width of each line.

    Returns:
        list: A list of strings, where each string is a segment of the
        original text with length up to `width`.
    """
    return [text[i:i+width] for i in range(0, len(text), width)]

def xml_to_json(element):
    """
    Converts an XML element and its children into a dictionary (JSON-like structure).

    This function recursively traverses the XML tree starting from the given element.
    If an element has no children, its text content is stored. If it has children,
    they are processed recursively. Repeated child tags are aggregated into lists.

    Args:
        element (xml.etree.ElementTree.Element): The root XML element to convert.

    Returns:
        dict: A dictionary representation of the XML element.
    """
    data = {}
    if len(element) == 0:
        data[element.tag] = element.text
    else:
        data[element.tag] = {}
        for child in element:
            child_data = xml_to_json(child)
            if child.tag in data[element.tag]:
                if not isinstance(data[element.tag][child.tag], list):
                    data[element.tag][child.tag] = [data[element.tag][child.tag]]
                data[element.tag][child.tag].append(child_data)
            else:
                data[element.tag][child.tag] = child_data
    return data

def main():
    """
    The main entry point of the application.

    This function handles the main logic:
    1. Fetches the timetable XML data from the university server.
    2. Prompts the user for module codes.
    3. Searches for the modules in the fetched data.
    4. Retrieves and displays specific timetable details for found modules.
    5. Optionally generates a PDF of the timetable.
    """
    # URL of the XML file
    url = "https://bpa.ums.edu.my/next_kuliah/finder.xml"

    welcome_animation()
    response = requests.get(url)
    print("\nStarting the processing...")
    for _ in tqdm(range(10), ncols=70, desc="Loading", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.5)

    print("\n", response)

    xml_data = response.text
    root = ET.fromstring(xml_data)
    resource_elements = root.findall('.//resource')
    module_codes = []
    module_code = input("Enter the module code (or leave blank to exit): ").upper()

    while module_code:
        module_codes.append(module_code)
        module_code = input("Enter another module code (or leave blank to exit): ").upper()
    found_module_codes = []

    for resource_element in resource_elements:
        module_name = resource_element.find('name').text.upper()
        # Note: 'id' might not be a direct attribute depending on XML structure, assuming it is correct as per original code.
        module_code = resource_element.attrib['id']

        if any(code in module_name for code in module_codes):
            print("Module Code:", module_code)
            print("Module Name:", module_name)
            link = resource_element.find('link').attrib['href']
            print("Link:", link)
            m = "https://bpa.ums.edu.my/next_kuliah/"+link
            print(m)
            response = requests.get(m)
            xml_contents = response.text
            roots = ET.fromstring(xml_contents)
            json_data = xml_to_json(roots)
            json_string = json.dumps(json_data, indent=4)
            data = json.loads(json_string)

            # Accessing deeply nested data, assuming structure is consistent
            weeks = data["timetable"]["span"]["span"]["description"]["description"]
            events = data["timetable"]["event"]

            table_headers = ["Day", "Time", "Category", "Staff", "Room"]
            table_data = []

            # Events can be a list or a single dict depending on XML-to-JSON conversion for single items
            # The original code iterates directly, assuming it's a list.
            # If there's only one event, xml_to_json might produce a dict, causing iteration over keys.
            # Assuming original code worked for the intended use cases.

            # Use 'if isinstance(events, list):' if robustness is needed, but sticking to original logic logic for now.
            for event in events:
                event_data = event["event"]
                day = event_data["day"]["day"]
                time = event_data["prettytimes"]["prettytimes"]
                category = event_data["category"]["category"]
                staff = event_data["resources"]["resources"]["staff"]["staff"]["item"]["item"]
                room_element = event_data["resources"]["resources"]["room"]["room"]["item"]["item"]
                room = room_element.split('(')[1].strip(" )")


                table_data.append([day, time, category,staff, room])

            print("Timetable for", weeks)
            print()
            col_width = 30
            header_format = "{:<{}}"
            header = ' | '.join(header_format.format(header, col_width) for header in table_headers)
            print('-' * len(header))
            print(header)
            print('-' * len(header))
            for row in table_data:
                formatted_row = [' | '.join(cell.ljust(col_width) for cell in row)]
                print(formatted_row[0])
                print('-' * len(header))

    # This logic seems to just copy module_codes to found_module_codes
    for code in module_codes:
        found_module_codes.append(code)

    not_found_module_codes = set(module_codes) - set(found_module_codes)
    if not_found_module_codes:
        print("Module codes not found:")
        for code in not_found_module_codes:
            print(code)

    print("Currently pdf generator only support one course at at time\n")
    pdf = input("Did you want to generate PDF?(Y/N): ").upper()
    if pdf == "Y":
        pdf_name = input("Insert PDF name: ")
        # Warning: variable 'table_headers' and 'table_data' are defined inside the loop.
        # If the loop doesn't run (no module found), this will crash.
        # Original code had this issue too.
        if 'table_headers' in locals() and 'table_data' in locals():
            generate_timetable_pdf(table_headers, table_data, pdf_name+".pdf")
        else:
             print("No data to generate PDF.")
    else:
        print('Bye2')

if __name__ == "__main__":
    main()
