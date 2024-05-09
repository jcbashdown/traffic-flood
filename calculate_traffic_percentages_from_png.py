
import os
import json
from PIL import Image
from datetime import datetime

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

# Specify the directory containing the PNG files
png_directory = 'final_images/pngs'

# Specify the color to exclude (in RGB format)
excluded_color = (255, 255, 255)  # White color

# Get a list of all PNG files in the directory
png_files = [file for file in os.listdir(png_directory) if file.endswith('.png')]

# Sort the PNG files by timestamp (oldest to newest)
png_files.sort()

# Initialize an empty list to store the results
results = []

# Process each PNG file
for png_file in png_files:
    # Extract the timestamp from the PNG file name
    file_timestamp = os.path.splitext(png_file)[0]

    timestamp = convert_timestamp(file_timestamp)

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

    # Append the result to the list
    results.append(result)

# Convert the results to JSON format
json_output = json.dumps(results, indent=2)

# Print the JSON output
print(json_output)
