#!/bin/bash

# NOTE: This script was a test and isn't intended to be used

convert output.png output.pnm
potrace output.pnm -s -o output.svg --alphamax 0.1 --turdsize 100
