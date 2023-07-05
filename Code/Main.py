import requests
import xml.etree.ElementTree as ET
import json
import textwrap
from pdf_generator import generate_timetable_pdf


def wrap_text(text, width):
    return [text[i:i+width] for i in range(0, len(text), width)]

# Convert XML to JSON
def xml_to_json(element):
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

# URL of the XML file
url = "https://bpa.ums.edu.my/next_kuliah/finder.xml"

# Send a GET request to the URL and get the XML content
response = requests.get(url)
print(response)

xml_data = response.text

# Parse the XML
root = ET.fromstring(xml_data)
resource_elements = root.findall('.//resource')

# Initialize an empty list to store module codes
module_codes = []

# Prompt the user to enter the module code
module_code = input("Enter the module code (or leave blank to exit): ").upper()

while module_code:
    module_codes.append(module_code)
    module_code = input("Enter another module code (or leave blank to exit): ").upper()

# Print the information for matching module codes
found_module_codes = []

for resource_element in resource_elements:
    module_name = resource_element.find('name').text.upper()
    module_code = resource_element.attrib['id']

    if any(code in module_name for code in module_codes):
        print("Module Code:", module_code)
        print("Module Name:", module_name)
        link = resource_element.find('link').attrib['href']
        print("Link:", link)
        #link = link.replace('.xml', '.html')
        
        m = "https://bpa.ums.edu.my/next_kuliah/"+link
        print(m)
        response = requests.get(m)
        xml_contents = response.text

        # Parse the XML content
        roots = ET.fromstring(xml_contents)
        
        # Convert root element to JSON
        json_data = xml_to_json(roots)

        # Convert JSON to a formatted string
        json_string = json.dumps(json_data, indent=4)        
        data = json.loads(json_string)

        # Extract timetable information
        weeks = data["timetable"]["span"]["span"]["description"]["description"]
        events = data["timetable"]["event"]

        # Prepare table headers and data
        table_headers = ["Day", "Time", "Category", "Staff", "Room"]
        table_data = []

        # Populate table data
        for event in events:
            event_data = event["event"]
            day = event_data["day"]["day"]
            time = event_data["prettytimes"]["prettytimes"]
            category = event_data["category"]["category"]
            staff = event_data["resources"]["resources"]["staff"]["staff"]["item"]["item"]
            room_element = event_data["resources"]["resources"]["room"]["room"]["item"]["item"]
            room = room_element.split('(')[1].strip(" )")


            table_data.append([day, time, category,staff, room])

        # ...

        # Print timetable as a table
        print("Timetable for", weeks)
        print()
        col_width = 30  # Width of each column
        header_format = "{:<{}}"
        header = ' | '.join(header_format.format(header, col_width) for header in table_headers)
        print('-' * len(header))
        print(header)
        print('-' * len(header))
        for row in table_data:
            formatted_row = [' | '.join(cell.ljust(col_width) for cell in row)]
            print(formatted_row[0])
            print('-' * len(header))
            
for code in module_codes:
    found_module_codes.append(code)

# Check for module codes that were not found
not_found_module_codes = set(module_codes) - set(found_module_codes)
if not_found_module_codes:
    print("Module codes not found:")
    for code in not_found_module_codes:
        print(code)

# Call the PDF generation function
pdf = input("Did you want to generate PDF?(Y/N): ").upper()
print("Currently pdf generator only support one course at at time\n")
pdf_name = input("Insert PDF name: ")
if pdf == "Y":
    generate_timetable_pdf(table_headers, table_data, pdf_name+".pdf")
else:
    print('Bye2')