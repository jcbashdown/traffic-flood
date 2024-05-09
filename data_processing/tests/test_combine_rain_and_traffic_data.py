# test_my_module.py
from data_processing.combine_rain_and_traffic_data import combine_data


precipitation = [
    {
        "timestamp": "2024-05-05T20:00:00Z",
        "precipMM": 1.8
    },
    {
        "timestamp": "2024-05-05T21:00:00Z",
        "precipMM": 1.7
    },
    {
        "timestamp": "2024-05-05T22:00:00Z",
        "precipMM": 2.3
    },
    {
        "timestamp": "2024-05-05T23:00:00Z",
        "precipMM": 3.0
    },
    {
        "timestamp": "2024-05-06T00:00:00Z",
        "precipMM": 2.0
    },
]
traffic = [
    {
        'timestamp': "2024-05-05T21:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333
    },
    {
        'timestamp': "2024-05-05T22:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333
    },
    {
        'timestamp': "2024-05-05T23:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333
    },
]
result = [
    {
        'timestamp': "2024-05-05T21:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333,
        "precipMM": 1.7
    },
    {
        'timestamp': "2024-05-05T22:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333,
        "precipMM": 2.3
    },
    {
        'timestamp': "2024-05-05T23:30:01:599Z.svg",
        'filename': "2024-05-05T04-30-01Z.svg",
        'percentage': 0.0333,
        "precipMM": 3.0
    },
]
def test_combine_data():
    assert combine_data(precipitation, traffic) == result
