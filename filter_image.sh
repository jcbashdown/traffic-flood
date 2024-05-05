#!/bin/bash

# Check if an input file was given
if [ -z "$1" ]
then
  echo "Usage: $0 <input_file>"
  exit 1
fi

# Set input and output file names
input_file="$1"
output_file="${input_file%.*}-filtered.png"

# Apply the image transformation
convert "$input_file" -fuzz 30% -fill white +opaque "#F23C32" -fill white +opaque "#832525" "$output_file"

echo "Filtered image saved as $output_file"

svg_input_file="$output_file"
pnm_output_file="${output_file%.*}.pnm"
svg_output_file="${output_file%.*}.svg"
convert $svg_input_file $pnm_output_file 
potrace $pnm_output_file -s -o $svg_output_file --alphamax 0.1 --turdsize 100

echo "SVG saved as $svg_output_file"

rm $pnm_output_file
