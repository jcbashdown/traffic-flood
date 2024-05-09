import json
# combine data in these formats
# 1. Precipitation:
# [
    # {
        # "timestamp": "2024-05-05T20:00:00Z",
        # "precipMM": 1.8
    # },
    # {
        # "timestamp": "2024-05-05T21:00:00Z",
        # "precipMM": 1.7
    # },
    # {
        # "timestamp": "2024-05-05T22:00:00Z",
        # "precipMM": 2.3
    # },
    # {
        # "timestamp": "2024-05-05T23:00:00Z",
        # "precipMM": 3.0
    # },
    # {
        # "timestamp": "2024-05-06T00:00:00Z",
        # "precipMM": 2.0
    # },
# ]
# 2. Traffic:
# [
    # {
        # 'timestamp': "2024-05-05T21:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
    # },
    # {
        # 'timestamp': "2024-05-05T22:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
    # },
    # {
        # 'timestamp': "2024-05-05T23:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
    # },
# ]
# By attaching the preceding precipitation to the traffic data
# 3. Output:
# [
    # {
        # 'timestamp': "2024-05-05T21:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
        # "precipMM": 1.7
    # },
    # {
        # 'timestamp': "2024-05-05T22:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
        # "precipMM": 2.3
    # },
    # {
        # 'timestamp': "2024-05-05T23:30:01:599Z.svg",
        # 'filename': "2024-05-05T04-30-01Z.svg",
        # 'percentage': 0.0333
        # "precipMM": 3.0
    # },
# ]
def combine_data(precipitation, traffic):
    combined_data = []
    for traffic_data in traffic:
        timestamp = traffic_data["timestamp"]
        # binary search would be better but isn't necessary because
        # we expect both json files ot be ordered and have a similar length
        # - the break is enough
        for precip_data in precipitation:
            # if the precipitation timestamp is < the traffic timestamp
            # then set precipitationMM to the precipitation value
            if precip_data["timestamp"] <= timestamp:
                precipMM = precip_data["precipMM"]
            else:
                # We assume the precip data is sorted by timestamp asc
                break
        combined_data.append({**traffic_data, "precipMM": precipMM})

    return combined_data

def get_json_data(json_file):
    # Read the JSON data from the file
    with open(json_file, "r") as file:
        data = json.load(file)    # Extract the relevant data and convert to the desired format
    return data

# Load the precipitation and traffic data
precipitation_json = "hourly_precip_mm.json"
traffic_json = "traffic_history_full.json"

precipitation = get_json_data(precipitation_json)
traffic = get_json_data(traffic_json)
combined_data = combine_data(precipitation, traffic)

print(json.dumps(combined_data, indent=4))
