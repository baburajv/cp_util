# main.py

from utils.json_parser import parse_json
from utils.logging_config import setup_logging
import pprint

logger = setup_logging()

def read_json_from_file(file_path):
    """
    Reads JSON content from a file and returns it as a string.

    :param file_path: Path to the JSON file.
    :return: JSON content as a string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"Error: The file '{file_path}' was not found.")
        return None
    except IOError as e:
        logger.error(f"Error: Unable to read the file '{file_path}'. {e}")
        return None

def main():
    # Path to the JSON input file
    input_file_path = 'input/content.json'  # JSON file with actual data

    # Read the JSON data from the file
    json_data = read_json_from_file(input_file_path)

    if json_data:
        # Parse and validate the JSON data
        extracted_content = parse_json(json_data)

    else:
        logger.error("No data to parse.")

if __name__ == "__main__":
    main()
