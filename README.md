# Time-Table-Finder
This project using Beautiful Soup to find and quickly sort my time table at my school
## Getting Started

To use this web scraper, follow these steps:

1. Install the required libraries:
   - `requests`
   - `beautifulsoup4`

2. Clone this repository:
   ```bash
   git clone https://github.com/AgentHitmanFaris/Time-Table-Finder
Run the Python script:

bash
Copy code
python scraper.py
Open the generated web page in a browser to view the extracted data.

Usage
The scraper.py script intercepts the connection using Burp Suite and captures the required JSON data from the specified URL.
It then processes the data and generates a web page that displays the extracted information.
Example
In the provided example, the scraper searches for the module AA10203 PENGANTAR SOSIOLOGI and extracts the corresponding day and time information from the BPA UMS website.

Dependencies
Python 3.x
Requests library
BeautifulSoup4 library
Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or additional features.

License
This project is licensed under the MIT License.

Feel free to modify the content as needed, including adding installation instructions, additional sections, or customizing it further to suit your repository's needs.

 
## How it works
User needs to enter the course code of the subject and this program will find it on the website, using powerfull algorithm the program will fidns and sort the time table according to date and time, and it will show to output using pdf/excel file.


## Updates
**22/06/23**
>Update new hashing algorithm
>
**01/07/22**
>Updating Webpage

**10/2/22**
>Adding web scrapping module
