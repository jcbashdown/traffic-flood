#!/bin/bash

# Set the base directory
BASE_DIR="output_images"
FINAL_DIR="final_images"

# Create the svgs directory if it doesn't exist
mkdir -p "$FINAL_DIR/svgs"
mkdir -p "$FINAL_DIR/pngs"

# Loop through each timestamped directory
for DIR in "$BASE_DIR"/*; do
    # Check if it's a directory
    if [ -d "$DIR" ]; then
        echo "Processing directory: $DIR"
        # If there is a file in final_images/svgs with the the name DIR.svg then skip this directory
        if [ -f "$FINAL_DIR/svgs/$(basename "$DIR").svg" ]; then
            echo "SVG already exists for this directory, skipping"
            continue
        fi
        
        # Run the stitching script
        ./image_processing/stitch-images.sh "$DIR"
        
        # Get the stitched map file
        STITCHED_MAP="$DIR/stitched_map.png"
        
        # Check if the stitched map file exists
        if [ -f "$STITCHED_MAP" ]; then
            echo "Stitched map found: $STITCHED_MAP"
            
            # Run the SVG processing script
            ./image_processing/filter-image.sh "$STITCHED_MAP"
            
            # Get the SVG output file
            SVG_OUTPUT="${STITCHED_MAP%.*}-filtered.svg"
            # Get the PNG output file
            PNG_OUTPUT="${STITCHED_MAP%.*}-filtered.png"
            # Extract the timestamp from the directory name
            TIMESTAMP=$(basename "$DIR")
            
            # Check if the SVG output file exists
            if [ -f "$SVG_OUTPUT" ]; then
                echo "SVG output found: $SVG_OUTPUT"
                
                # Copy the SVG to the svgs directory with the timestamped file name
                cp "$SVG_OUTPUT" "$FINAL_DIR/svgs/$TIMESTAMP.svg"
                
                echo "SVG copied to: $FINAL_DIR/svgs/$TIMESTAMP.svg"
            else
                echo "SVG output not found: $SVG_OUTPUT"
            fi
            if [ -f "$PNG_OUTPUT" ]; then
                echo "PNG output found: $PNG_OUTPUT"
                
                # Copy the SVG to the svgs directory with the timestamped file name
                cp "$PNG_OUTPUT" "$FINAL_DIR/pngs/$TIMESTAMP.png"
                
                echo "PNG copied to: $FINAL_DIR/pngs/$TIMESTAMP.png"
            else
                echo "PNG output not found: $PNG_OUTPUT"
            fi
        else
            echo "Stitched map not found: $STITCHED_MAP"
        fi
        
        echo "---"
    fi
done
