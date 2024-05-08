import subprocess
import json
from datetime import datetime
import os

def get_weather_data(start_date, end_date):
    #get the api key from .env file
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    location = "nairobi"
    unit_group = "metric"
    content_type = "json"

    # url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?key={api_key}&unitGroup={unit_group}&contentType={content_type}"

    # # Make the curl request and capture the response
    # response = subprocess.check_output(["curl", url])

    # # Parse the JSON response
    # data = json.loads(response)
def get_weather_data(json_file):
    # Read the JSON data from the file
    with open(json_file, "r") as file:
        data = json.load(file)    # Extract the relevant data and convert to the desired format
#Comment fn to here when switching back to curl
    result = []
    for day in data["days"]:
        for hour in day["hours"]:
            timestamp = datetime.utcfromtimestamp(hour["datetimeEpoch"]).isoformat() + "Z"
            precip_mm = hour.get("precip", 0.0)
            result.append({"timestamp": timestamp, "precipMM": precip_mm})

    return json.dumps(result, indent=4)

# Example usage
# start_date = "2024-05-05"
# end_date = "2024-05-06"
# output = get_weather_data(start_date, end_date)
json_file = "2024-05-05--2024-05-06-weather.json"
output = get_weather_data(json_file)
print(output)
