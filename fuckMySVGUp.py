# --- fuckMySVGUp.py ---
# A script for fucking SVG's up.
#
# Author:  Dan Hett (hellodanhett@gmail.com)
# Released under the DO WHAT THE FUCK YOU WANT public license.
#
# Usage:
# python [input file] [outputdir] [copies] [intensity]
# so
# python myFile.svg output 50 NORMAL
# would make fifty versions, at normal intensity, and write them into 'output'.
# Note, all args are mandatory for now.
#
# Input file = the SVG you want to fuck up.
# Output dir = the directory to spit out into. .
# Copies = how many broken versions you want to output.
# Intensity = Can be LOW, NORMAL, HIGH, LUDICROUS, and OMG.

import sys
import os.path

# Check to make sure the SVG exists
if os.path.isfile(sys.argv[1:][0]) == True:
    input = sys.argv[1:][0]
else:
    print("Error: Input SVG not found!")
    sys.exit()

# Check to ensure the output directory exists
if os.path.isdir(sys.argv[1:][1]) == True:
    output = sys.argv[1:][1]
else:
    print("Error: Output directory not found!")
    sys.exit()

# Add copies and intensity if passed in, or use defaults
# TODO - check these inputs maybs? iunno
copies = sys.argv[1:][2]
intensity = sys.argv[1:][3]

# Confirm we're offski
print("--------- FUCK MY SVG UP ---------")
print("OK! Fucking up " + input + " " + copies + " time(s) using " + intensity + " intensity!")
print("Fucked-up files will be written to: " + output)

# Open the file as a string
with open(input, 'r') as myfile:
    data = myfile.read().replace('\n', '')

print(data)
