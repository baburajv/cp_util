import json
from jsonschema import validate, ValidationError
from .logging_config import setup_logging
from constants import *
import uuid
import time

logger = setup_logging()

def create_widget(widget):
        
    widget_uuid = uuid.uuid4()
    widget_name = widget.get('name')
    widget_chart_type = widget.get('chartType')

    if widget_chart_type is not None:
        ops_widget_json_fragment = OPS_DASHBOARD_WIDGET_HEADER.replace(
            OPS_DASHBOARD_WIDGET_ID_PLACEHOLDER, str(widget_uuid)
        ).replace(
            OPS_DASHBOARD_WIDGET_TITLE_PLACEHOLDER, widget_name
        ).replace(
            OPS_DASHBOARD_WIDGET_CHART_TYPE_PLACEHOLDER, widget_chart_type
        )

        ops_widget_json_fragment = ops_widget_json_fragment + OPS_DASHBOARD_WIDGET_CONFIG + OPS_DASHBOARD_WIDGET_FOOTER
        return ops_widget_json_fragment
    else:    
        logger.error(f"widget chart type is None for {widget.name}", widget)
        return ""
    
def add_dashboard_json(widget_array, name):

    dashboard_uuid = uuid.uuid4()
    content_uuid = uuid.uuid4()

    # Get the current time in seconds since the epoch
    epoch_time_seconds = time.time()
    # Convert seconds to milliseconds
    epoch_time_millis = int(epoch_time_seconds * 1000)
    
    dashboard_footer_json = OPS_DASHBOARD_FOOTER.replace(OPS_DASHBOARD_ID_PLACEHOLDER,str(dashboard_uuid)).replace(
        OPS_DASHBOARD_UUID_PLACEHOLDER,str(content_uuid)
    ).replace(OPS_DASHBOARD_NAME_PLACEHOLDER, name)
              
    dashboard_json = OPS_DASHBOARD_HEADER + widget_array + dashboard_footer_json
    
    dashboard_json = dashboard_json.replace(OPS_DASHBOARD_CREATE_TIME_PLACEHOLDER, str(epoch_time_millis)).replace(
        OPS_DASHBOARD_LASTUPDATE_TIME_PLACEHOLDER,str(epoch_time_millis)
    )

    return dashboard_json
