import os
import json
from PIL import Image
from datetime import datetime
import sys

def convert_timestamp(custom_timestamp):
    # Parse the timestamp string into a datetime object
    dt = datetime.strptime(custom_timestamp, "%Y-%m-%dT%H-%M-%S.%fZ")

    # Format the datetime object into the desired ISO format
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def calculate_non_color_percentage(image_file, color):
    # Open the image file
    with Image.open(image_file) as image:
        # Convert the image to RGB mode
        rgb_image = image.convert('RGB')

        # Load the image data into a list of pixels
        pixels = list(rgb_image.getdata())

        # Get the dimensions of the image
        width, height = rgb_image.size

        # Calculate the total number of pixels in the image
        total_pixels = width * height

        # Count the frequency of the specified color
        color_frequency = pixels.count(color)
        # print(total_pixels, color_frequency)

        # Calculate the number of non-color pixels
        non_color_pixels = total_pixels - color_frequency

        # Calculate the percentage of non-color pixels
        non_color_percentage = (non_color_pixels / total_pixels) * 100

        return non_color_percentage

def process_png_files(png_directory, excluded_color, existing_data=None):
    # Initialize an empty list to store the results
    results = []

    # Get a list of all PNG files in the directory
    png_files = [file for file in os.listdir(png_directory) if file.endswith('.png')]

    # Sort the PNG files by timestamp (oldest to newest)
    png_files.sort()

    last_timestamp = existing_data[-1]['timestamp'] if existing_data else None

    # Process each PNG file
    for png_file in png_files:
        # Extract the timestamp from the PNG file name
        file_timestamp = os.path.splitext(png_file)[0]

        timestamp = convert_timestamp(file_timestamp)

        # Skip the file if the timestamp is an old one
        # If it is already in the existing data
        # then we have already processed this file
        if last_timestamp and timestamp <= last_timestamp:
            print(f"Skipping {png_file} as already processed")
            continue

        # Calculate the percentage of non-color pixels
        png_path = os.path.join(png_directory, png_file)
        percentage = calculate_non_color_percentage(png_path, excluded_color)

        svg_file = f"{file_timestamp}.svg"

        # Create a dictionary with the timestamp and percentage
        result = {
            'timestamp': timestamp,
            'filename': svg_file,
            'percentage': round(percentage, 4)
        }
        # print the new result
        print(result)

        # Append the result to the list
        results.append(result)
    return results

# Specify the directory containing the PNG files
png_directory = 'final_images/pngs'

# Specify the color to exclude (in RGB format)
excluded_color = (255, 255, 255)  # White color

# Get the output filename from the command line argument
output_filename = sys.argv[1] if len(sys.argv) > 1 else None

existing_data = None
if output_filename and os.path.isfile(output_filename):
    with open(output_filename, 'r') as file:
        existing_data = json.load(file)

results = process_png_files(png_directory, excluded_color, existing_data)

# If there is existing data, append the new results to it
if existing_data:
    existing_data.extend(results)
    results = existing_data

# Convert the results to JSON format
json_output = json.dumps(results, indent=2)

if output_filename:
    with open(output_filename, 'w') as file:
        file.write(json_output)
else:
    print(json_output)
