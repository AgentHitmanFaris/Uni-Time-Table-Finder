# Time-Table-Finder

Time-Table-Finder is a Python application designed to retrieve and display timetable information for specific module codes from the UMS (Universiti Malaysia Sabah) server. It fetches XML data, parses it, and presents the schedule in a readable table format. Users can also generate a PDF version of the timetable.

## Purpose

The main purpose of this tool is to simplify the process of checking class schedules for students and staff. Instead of navigating complex websites, users can quickly input their module codes and get the relevant timetable details, including day, time, venue, and instructor.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AgentHitmanFaris/Time-Table-Finder.git
    cd Time-Table-Finder
    ```

2.  **Install the required dependencies:**
    It is recommended to use a virtual environment.

    *   Using `pip`:
        ```bash
        pip install -r requirements.txt
        ```

    *   Using `pipenv`:
        ```bash
        pipenv install
        ```

## Usage

1.  **Run the application:**
    ```bash
    python Main.py
    ```

2.  **Enter Module Codes:**
    - The program will prompt you to enter a module code (e.g., `KT12303`).
    - You can enter multiple module codes one by one.
    - Leave the input blank and press Enter when you are done adding modules.

3.  **View Timetable:**
    - The program will search for the modules and display the timetable information (Day, Time, Category, Staff, Room) in the console.

4.  **Generate PDF:**
    - After displaying the results, you will be asked if you want to generate a PDF.
    - Enter `Y` (Yes) to generate a PDF.
    - Provide a name for the PDF file when prompted.
    - The PDF will be saved in the current directory.

## Dependencies

The project relies on the following Python packages:

-   `reportlab`: For generating PDF files.
-   `requests`: For making HTTP requests to fetch XML data.
-   `tqdm`: For displaying progress bars.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
