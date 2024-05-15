import subprocess
import json
from datetime import datetime
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Read the JSON data from the file if it exists
def get_existing_data(json_file):
    if not os.path.isfile(json_file):
        return []

    with open(json_file, "r") as file:
        data = json.load(file)    # Extract the relevant data and convert to the desired format

    return data

def get_weather_data(start_date, end_date, existing_data):
    last_timestamp = existing_data[-1]['timestamp'] if existing_data else None

    # If the start date is before the last timestamp,
    # set the start date to the date part of the last timestamp
    # Currently I can't get datetime queries to work and so I can only get whole days
    if last_timestamp and start_date < last_timestamp:
        start_date = last_timestamp.split("T")[0]

    #get the api key from .env file
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    location = "nairobi"
    unit_group = "metric"
    content_type = "json"

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?key={api_key}&unitGroup={unit_group}&contentType={content_type}"

    print(f"Making request to {url}")

    # Make the curl request and capture the response
    response = subprocess.check_output(["curl", url])

    # Parse the JSON response
    data = json.loads(response)
    result = []
    for day in data["days"]:
        for hour in day["hours"]:
            timestamp = datetime.utcfromtimestamp(hour["datetimeEpoch"]).isoformat() + "Z"
            if timestamp <= last_timestamp:
                continue
            precip_mm = hour.get("precip", 0.0)
            result.append({"timestamp": timestamp, "precipMM": precip_mm})

    return result

# Get the start and end dates from command line arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <start_date> <end_date> <output_file>")
    sys.exit(1)

start_date = sys.argv[1]
end_date = sys.argv[2]
output_file = sys.argv[3]

existing_data=get_existing_data(output_file)

output = get_weather_data(start_date, end_date, existing_data)

existing_data.extend(output)
output = existing_data

# Write the output to the specified file
with open(output_file, "w") as file:
    file.write(json.dumps(output, indent=4))
