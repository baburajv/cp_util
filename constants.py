# Define constants for all the keys you will access in the JSON
LI_DASHBOARD_NAME = "name"
LI_DASHBOARD_NAMESPACE = "namespace"
LI_DASHBOARD_CONTENT_PACK_ID = "contentPackId"
LI_DASHBOARD_FRAMEWORK = "framework"
LI_DASHBOARD_VERSION = "version"
LI_DASHBOARD_EXTRACTED_FIELDS = "extractedFields"
LI_DASHBOARD_QUERIES = "queries"
LI_DASHBOARD_ALERTS = "alerts"
LI_DASHBOARD_AUTHOR = "author"
LI_DASHBOARD_URL = "url"
LI_DASHBOARD_ALIAS_FIELDS = "aliasFields"
LI_DASHBOARD_ALIAS_RULES = "aliasRules"
LI_DASHBOARD_CONTENT_VERSION = "contentVersion"
LI_DASHBOARD_INFO = "info"
LI_DASHBOARD_INSTRUCTIONS = "instructions"
LI_DASHBOARD_UPGRADE_INSTRUCTIONS = "upgradeInstructions"
LI_DASHBOARD_ICON = "icon"

OPS_DASHBOARD_WIDGET_ID_PLACEHOLDER = "{widgetid}"

OPS_DASHBOARD_WIDGET_GRIDSTER_COORDS_X_PLACEHOLDER = "{gridsterCoords_x}"
OPS_DASHBOARD_WIDGET_GRIDSTER_COORDS_Y_PLACEHOLDER = "{gridsterCoords_y}"
OPS_DASHBOARD_WIDGET_GRIDSTER_COORDS_W_PLACEHOLDER = "{gridsterCoords_w}"
OPS_DASHBOARD_WIDGET_GRIDSTER_COORDS_H_PLACEHOLDER = "{gridsterCoords_h}"

OPS_DASHBOARD_WIDGET_TITLE_PLACEHOLDER = "{widget_title}"
OPS_DASHBOARD_WIDGET_IS_OVER_TIME_PLACEHOLDER = "{widget_liOverTime_isOverTime}"
OPS_DASHBOARD_WIDGET_GROUP_BY_PLACEHOLDER = "{widget_liOverTime_groupBy_array}"
OPS_DASHBOARD_WIDGET_LI_AGGREGATE_FUNCTION_PLACEHOLDER = "{widget_liAggregationFunction}"
OPS_DASHBOARD_WIDGET_LI_QUERYID_PLACEHOLDER = "{widget_liQueryId}"
OPS_DASHBOARD_WIDGET_CHART_TYPE_PLACEHOLDER = "{widget_chartType}"

OPS_DASHBOARD_WIDGET_HEADER ="""
        {
            "collapsed": false,
            "id": "{widgetid}",
            "gridsterCoords": {
               "w": "{gridsterCoords_w}",
               "x": "{gridsterCoords_x}",
               "h": "{gridsterCoords_h}",
               "y": "{gridsterCoords_y}"
            },
            "type": "LogAnalysis",
            "title": "{widget_title}",
"""

OPS_DASHBOARD_WIDGET_CONFIG = """
            "config": {
               "queryFilter_searchtext": [],
               "refreshInterval": 300,
               "resource": [],
               "refreshContent": {"refreshContent": false},
               "relationshipMode": {"relationshipMode": 0},
               "queryFilter": {
                  "size": 50,
                  "query": {"bool": {"filter": []}}
               },
               "title": "{widget_title}",
               "liViewMode": "chart",
               "liOverTime": {
                  "isOverTime": {widget_liOverTime_isOverTime},
                  "groupBy": "{widget_liOverTime_groupBy_array}"
               },
               "liAggregationFunction": "{widget_liAggregationFunction}",
               "mode": "all",
               "depth": 1,
               "liQueryId": "{widget_liQueryId}",
               "chartType": "{widget_chartType}",
               "liQueryMode": 2,
               "selfProvider": {"selfProvider": false}
            },
"""
OPS_DASHBOARD_WIDGET_FOOTER = """
            "height": 380
        },
"""

OPS_DASHBOARD_HEADER = """
{
    "entries": {},
    "dashboards": [{
       "shared": false,
       "temporary": false,
       "hidden": false,
       "creationTime": "{creatonTime}",
       "autoswitchEnabled": false,
       "importAttempts": 0,
       "lastUpdateUserId": "{lastUpdateUserId}",
       "columnProportion": "1-1",
       "importComplete": true,
       "description": "",
       "columnCount": 1,
"""

OPS_DASHBOARD_WIDGETS_ARRAY_START = '       "widgets": ['

OPS_DASHBOARD_WIDGETS_ARRAY_END = "],"

OPS_DASHBOARD_FOOTER = """
       "userId": "{userId}",
       "states": [],
       "homeTab": false,
       "name": "{name}",
       "gridsterMaxColumns": "{gridsterMaxColumns}",
       "rank": 0,
       "disabled": false,
       "id": "{id}",
       "locked": false,
       "dashboardNavigations": {},
       "widgetInteractions": [],
       "lastUpdateTime": "{lastUpdateTime}"
    }],
    "uuid": "{uuid}"
}
"""


OPS_DASHBOARD_CREATE_TIME_PLACEHOLDER = "{creatonTime}"
OPS_DASHBOARD_LASTUPDATE_TIME_PLACEHOLDER = "{lastUpdateTime}"
OPS_DASHBOARD_ID_PLACEHOLDER = "{id}"
OPS_DASHBOARD_UUID_PLACEHOLDER = "{uuid}"
OPS_DASHBOARD_NAME_PLACEHOLDER = "{name}"
COMMA =","