# Time-Table-Finder

Time-Table-Finder is a project that allows you to retrieve timetable information for specific module codes. It retrieves XML data from a given URL, parses it, and displays the timetable information in a table format. You also have the option to generate a PDF of the timetable.

## Installation

1. Clone the repository:
    git clone https://github.com/AgentHitmanFaris/Time-Table-Finder

3. Install the required dependencies:
pip install requests xmltodict reportlab

## Usage

1. Open the `Main.py` file in a text editor.

2. Update the `url` variable with the URL of the XML file containing the timetable data.

3. Run the `Main.py` file:
python Main.py

4. Follow the on-screen prompts to enter module codes for which you want to retrieve timetable information.

5. The program will display the timetable information in a table format.

6. If you want to generate a PDF of the timetable, enter "Y" when prompted and provide a PDF filename.

7. The PDF will be generated and saved in the current directory.

## Dependencies

- requests
- xmltodict
- reportlab

## License

This project is licensed under the [MIT License](LICENSE).
