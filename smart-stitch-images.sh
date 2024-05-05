#!/bin/bash

# Ensure Hugin and ImageMagick are installed
if ! command -v pto_gen &> /dev/null
then
    echo "Hugin is not installed. Installing Hugin..."
    sudo apt-get update
    sudo apt-get install hugin
fi

if ! command -v convert &> /dev/null
then
    echo "ImageMagick is not installed. Installing ImageMagick..."
    sudo apt-get install imagemagick
fi

# Generate the initial project file from images
pto_gen -o project.pto map1.png map2.png map3.png map4.png

# Automatically find control points
cpfind --multirow -o project.pto project.pto

# Optimize the panorama
autooptimiser -a -m -l -s -o project_optimized.pto project.pto

# Stitch the images
hugin_executor --stitching --prefix=output project_optimized.pto

# Convert the output to a more common format like PNG 
convert output.tif final_output.png

echo "Stitching complete. The final output is 'final_output.png'."
