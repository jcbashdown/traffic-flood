#!/bin/bash

# Check if directory is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Assign the directory to a variable
DIR=$1

# Check if directory exists
if [ ! -d "$DIR" ]; then
    echo "Directory does not exist: $DIR"
    exit 1
fi

# Construct the path to each map image
MAP1="$DIR/map1.png"
MAP2="$DIR/map2.png"
MAP3="$DIR/map3.png"
MAP4="$DIR/map4.png"

# Check if map files exist
if [ ! -f "$MAP1" ] || [ ! -f "$MAP2" ] || [ ! -f "$MAP3" ] || [ ! -f "$MAP4" ]; then
    echo "One or more map files are missing in the directory."
    exit 1
fi

# Use ImageMagick montage to stitch the maps
#montage "$MAP1" "$MAP2" "$MAP3" "$MAP4" -geometry +0+0 -mattecolor None -matte -frame 0 -border 0 -bordercolor Transparent -tile 2x2 "$DIR/stitched_map.png"
#
#convert "$MAP1" "$MAP2" +append intermediate1.png
#convert "$MAP3" "$MAP4" +append intermediate2.png
#convert intermediate1.png intermediate2.png -append "$DIR/stitched_map.png"
#
convert "$MAP1" -trim tmp_images/trimmed1.png
convert "$MAP2" -trim tmp_images/trimmed2.png
convert "$MAP3" -trim tmp_images/trimmed3.png
convert "$MAP4" -trim tmp_images/trimmed4.png
montage tmp_images/trimmed1.png tmp_images/trimmed2.png tmp_images/trimmed3.png tmp_images/trimmed4.png -geometry +0+0 -tile 2x2 -frame 0 -border 0 -matte "$DIR/stitched_map.png"

echo "Stitched map created at: $DIR/stitched_map.png"
