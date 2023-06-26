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
x = [element.text.split("#", 1) for element in txt]

# Print each data on a new line
for data in x:
    if len(data) == 2:
        section1, section2 = data
        print("Section 1:")
        print(section1.strip()) # Remove leading/trailing whitespaces

# Find the specific module
module_code = "AA10203"
