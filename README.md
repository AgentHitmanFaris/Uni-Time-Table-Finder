# Time-Table-Finder

Time-Table-Finder is a Python project that allows you to retrieve timetable information for specific module codes. It retrieves XML data from a given URL, parses it, and displays the timetable information in a table format. You also have the option to generate a PDF of the timetable.

## Installation

1. Clone the repository:
```
$ https://github.com/AgentHitmanFaris/Time-Table-Finder.git
```

2. Install the required dependencies:
- If you have pip installed:
  ```
  pip install -r requirements.txt
  ```
- If you have pipenv installed:
  ```
  pipenv install
  ```

3. Run the `Main.py` file:

4. Follow the on-screen prompts to enter module codes for which you want to retrieve timetable information.

5. The program will display the timetable information in a table format.

6. If you want to generate a PDF of the timetable, enter "Y" when prompted and provide a PDF filename.

7. The PDF will be generated and saved in the current directory.

## Dependencies

- reportlab
- requests
- tqdm

## License

This project is licensed under the [MIT License](LICENSE).
