# pyinstaller --hidden-import=robot.libraries.BuiltIn --hidden-import=robot.libraries.Easter --hidden-import=SeleniumLibrary --hidden-import=webdriver_manager --onefile --add-data "main.robot;." --add-data "Results;Results" --add-data "C:/Users/20023350/Documents/Robotframework/Robot_executable/venv/Lib/site-packages/robot/htmldata;robot/htmldata" main.py

import os
import logging
from pathlib import Path
from robot.running import TestDefaults, TestSuite
from robot.api import ResultWriter
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def parse(source: Path, defaults: TestDefaults) -> TestSuite:
        # Read the content of the file
        data = source.read_text()

        # Replace the headers with Robot Framework syntax
        for header in 'Settings', 'Variables', 'Test Cases', 'Keywords':
            data = data.replace(f'=== {header} ===', f'*** {header} ***')

        # Create the test suite from the string
        suite = TestSuite.from_string(data, defaults=defaults)

        # Configure the suite with the source file name
        return suite.config(name=TestSuite.name_from_source(source), source=source)

def run_robot_test():
    # Get the paths for the temporary and current directories
    temporal_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(".")
    
    # Create the Results directory if it doesn't exist
    results_dir = os.path.join(base_path, "Results")
    os.makedirs(results_dir, exist_ok=True)
    
    # Build the path to the robot framework file
    robot_file = 'main.robot'
    print("temporal_path, ", temporal_path)
    print("base ,", base_path)
    robot_path = os.path.join(temporal_path, robot_file)
    print("ROBOT PATH ", robot_path)
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Log the path to the robot framework file
        logger.info("Robot path: %s", robot_path)
        # Define the variables
        variables = {
            '${VARIABLE1}': 'K286348'
        }

        # Parse the test suite from the source file
        source_path = Path(robot_path)
        suite = parse(source=source_path, defaults=TestDefaults())

        # Find the test case and add a keyword to it
        for test in suite.tests:
            if test.name == 'This is a test case':
                test.body.create_keyword(name='Log', args=['Hello!'])
                break
        
        # Add variables to the suite
        for name, value in variables.items():
            suite.resource.variables.create(name=name).value = value

        # Import the SeleniumLibrary
        suite.resource.imports.library('SeleniumLibrary')

        # Run the test suite and save the results
        output_xml = os.path.join(temporal_path, 'test_output.xml')
        suite.run(output=output_xml)

        # Write the results to report.html and log.html
        writer = ResultWriter(output_xml)
        writer.write_results(report=os.path.join(results_dir, 'report.html'), log=os.path.join(results_dir, 'log.html'))
        logging.info("Robotframework Test Cases completed.")
    
    except Exception as e:
        # Log any exceptions
        logger.error("An error occurred: %s", str(e))


def open_file():
    """Open a file and display its content."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window of Tkinter

    filepaths = filedialog.askopenfilenames(
        initialdir=f'{os.path.expanduser("~")}/Downloads', # Downloads directory of main user
        title="Open File",
        filetypes=(("Text Files", "*.xls"), ("All Files", "*.*")),
        multiple=True
    )
    dfs = []  # List to storage the pandas DataFrames

    for filepath in filepaths:
        with open(filepath) as xml_file:
            soup = BeautifulSoup(xml_file.read(), 'xml')
            for sheet in soup.findAll('Worksheet'):
                sheet_as_list = []
                for row in sheet.findAll('Row'):
                    sheet_as_list.append([cell.Data.text if cell.Data else '' for cell in row.findAll('Cell')])
                sheet_name = sheet.attrs['ss:Name']  # Get the sheet name
                dfs.append((dfs, sheet_name))
    return {"list dataframes": dfs}

if __name__ == "__main__":
    run_robot_test()
    print(open_file())
    logging.info("Completed.")

