import requests
from bs4 import BeautifulSoup

# URL of the XML file
url = "https://bpa.ums.edu.my/next_kuliah/finder.xml"

# Send a GET request to the URL and get the XML content
response = requests.get(url)
print(response)

xml_content = response.text

# Create a BeautifulSoup object to parse the XML content
soup = BeautifulSoup(xml_content, "xml")
txt = soup.find_all("name")
x = [element.text.split(" ", 1) for element in txt]

# Initialize an empty list to store module codes
module_codes = []

# Prompt the user to enter the module code
module_code = input("Enter the module code (or leave blank to exit): ").upper()

while module_code:
    module_codes.append(module_code)
    module_code = input("Enter another module code (or leave blank to exit): ").upper()

# Print the two sections and scrape the link attribute value for each module code
for data in x:
  section1, section2 = data
  section1_parts = section1.strip()
  section2_parts = section2.split(", ")

  if section1_parts in module_codes:
    print("Section 1:")
    print(section1_parts)
    print("Section 2:")
    print(section2_parts[0].strip())
    print()