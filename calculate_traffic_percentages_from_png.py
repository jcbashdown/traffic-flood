import os
import json
from PIL import Image

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
        print(total_pixels, color_frequency)

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
    timestamp = os.path.splitext(png_file)[0]

    # Calculate the percentage of non-color pixels
    png_path = os.path.join(png_directory, png_file)
    percentage = calculate_non_color_percentage(png_path, excluded_color)

    # Create a dictionary with the timestamp and percentage
    result = {
        'timestamp': timestamp,
        'percentage': round(percentage, 4)
    }

    # Append the result to the list
    results.append(result)

# Convert the results to JSON format
json_output = json.dumps(results, indent=2)

# Print the JSON output
print(json_output)
