# utils/json_parser.py

import json
from jsonschema import validate, ValidationError
from .logging_config import setup_logging
from constants import *
from .create_dashboard import create_widget, add_dashboard_json
import pprint

logger = setup_logging()

def load_json_schema(schema_file='schemas/schema.json'):
    """
    Loads the JSON schema from a file.
    
    :param schema_file: Path to the JSON schema file.
    :return: Loaded schema as a dictionary.
    """
    try:
        with open(schema_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Schema file '{schema_file}' not found.")
        return None
    except IOError as e:
        logger.error(f"Error reading schema file '{schema_file}': {e}")
        return None

def validate_json(data, schema):
    """
    Validates the JSON data against a schema.
    
    :param data: The data to validate.
    :param schema: The schema to validate against.
    :return: True if valid, False otherwise.
    """
    try:
        validate(instance=data, schema=schema)
        logger.info("JSON data is valid")
        return True
    except ValidationError as e:
        logger.error(f"JSON validation error: {e.message}")
        return False

def parse_dashboard_section(data):
    dashboard_sections = data.get("dashboardSections", [])
    
    content_name = data.get('name', "")

    for i, section in enumerate(dashboard_sections):
        views = section.get("views", [])
        for j, view in enumerate(views):
            view_name = view.get("name","")

            dashboard_json = ""
            constraints = view.get("constraints", [])
            #for k, constraint in enumerate(constraints):
            #    print(f"      Constraint {k + 1}:")
            #    print(f"        Internal Name: {constraint.get('internalName')}")
            #    print(f"        Operator: {constraint.get('operator')}")
            
            widgets_array = ""
            rows = view.get("rows", [])
            for l, row in enumerate(rows):
                widgets = row.get("widgets", [])
  
                widgets_array = OPS_DASHBOARD_WIDGETS_ARRAY_START
                for m, widget in enumerate(widgets):
                    widget_json = create_widget(widget)
                    widgets_array = widgets_array + widget_json

            widgets_array = widgets_array[:-1]  # Remove the last character
            widgets_array = widgets_array + OPS_DASHBOARD_WIDGET_FOOTER    
            ops_dashboard_name = content_name + " - " + view_name
            dashboard_json = add_dashboard_json(widgets_array, ops_dashboard_name)
            print(dashboard_json)

def parse_json(data):
    """
    Parses the JSON data and extracts necessary fields.
    
    :param data: The JSON data (as string).
    :return: Extracted data as a dictionary or None if there's an error.
    """
    try:
        # Load JSON data
        parsed_data = json.loads(data)     
        extracted_data = {}
        # Load the schema and validate the JSON
        schema = load_json_schema()  # Loads the schema from file

        if not validate_json(parsed_data, schema):
            return None  # Invalid JSON structure

        # Extract main attributes using constants
        if(LI_DASHBOARD_NAME in  parsed_data):
            li_dashboard_name = parsed_data.get(LI_DASHBOARD_NAME, "Unknown")
            li_dashboard_namespace = parsed_data.get(LI_DASHBOARD_NAMESPACE, "Unknown")
            li_dashboard_content_pack_id = parsed_data.get(LI_DASHBOARD_CONTENT_PACK_ID, "Unknown")
            li_dashboard_framework = parsed_data.get(LI_DASHBOARD_FRAMEWORK, "Unknown")
            li_dashboard_version= parsed_data.get(LI_DASHBOARD_VERSION, "Unknown")
            li_dashboard_extracted_fields = parsed_data.get(LI_DASHBOARD_EXTRACTED_FIELDS, "No Extracted Fields")
            li_dashboard_queries = parsed_data.get(LI_DASHBOARD_QUERIES, "No Queries")
            li_dashboard_alerts = parsed_data.get(LI_DASHBOARD_ALERTS, "No Alerts")
            li_dashboard_author = parsed_data.get(LI_DASHBOARD_AUTHOR, "Unknown")
            li_dashboard_url = parsed_data.get(LI_DASHBOARD_URL, "Unknown")
            li_dashboard_alias_fields = parsed_data.get(LI_DASHBOARD_ALIAS_FIELDS, "Unknown")
            li_dashboard_alias_rules = parsed_data.get(LI_DASHBOARD_ALIAS_RULES, "Unknown")
            li_dashboard_content_version = parsed_data.get(LI_DASHBOARD_CONTENT_VERSION, "Unknown Version")
            li_dashboard_dashboard_info = parsed_data.get(LI_DASHBOARD_INFO, "No additional info")
            li_dashboard_additional_info = parsed_data.get(LI_DASHBOARD_INSTRUCTIONS, "No instructions available")
            li_dashboard_upgrade_instructions = parsed_data.get(LI_DASHBOARD_UPGRADE_INSTRUCTIONS, "No upgrae instructions")
            li_dashboard_icon = parsed_data.get(LI_DASHBOARD_ICON, "No Icon")


            # Return extracted data
            extracted_data[LI_DASHBOARD_NAME] = li_dashboard_name
            extracted_data[LI_DASHBOARD_NAMESPACE] = li_dashboard_namespace
            extracted_data[LI_DASHBOARD_CONTENT_PACK_ID] = li_dashboard_content_pack_id
            extracted_data[LI_DASHBOARD_FRAMEWORK] = li_dashboard_framework
            extracted_data[LI_DASHBOARD_VERSION] = li_dashboard_version
            extracted_data[LI_DASHBOARD_EXTRACTED_FIELDS] = li_dashboard_extracted_fields
            extracted_data[LI_DASHBOARD_QUERIES] = li_dashboard_queries
            extracted_data[LI_DASHBOARD_ALERTS] = li_dashboard_alerts
            extracted_data[LI_DASHBOARD_AUTHOR] = li_dashboard_author
            extracted_data[LI_DASHBOARD_URL] = li_dashboard_url
            extracted_data[LI_DASHBOARD_ALIAS_FIELDS] = li_dashboard_alias_fields
            extracted_data[LI_DASHBOARD_ALIAS_RULES] = li_dashboard_alias_rules
            extracted_data[LI_DASHBOARD_CONTENT_VERSION] = li_dashboard_content_version
            extracted_data[LI_DASHBOARD_INFO] = li_dashboard_dashboard_info
            extracted_data[LI_DASHBOARD_INSTRUCTIONS] = li_dashboard_additional_info
            extracted_data[LI_DASHBOARD_UPGRADE_INSTRUCTIONS] = li_dashboard_upgrade_instructions
            extracted_data[LI_DASHBOARD_ICON] = li_dashboard_icon
            #pprint.pprint(extracted_data)
            parse_dashboard_section(parsed_data)
        return extracted_data

    except json.JSONDecodeError as e:
        logger.error("Failed to decode JSON: %s", e)
        return None
    except Exception as e:
        logger.error("An error occurred while parsing JSON: %s", e)
        return None
