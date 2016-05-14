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
# would make fifty versions, at normal intensity, and write them into 'output'
#
# Input file = the SVG you want to fuck up
# Output dir = the directory to spit out into (defaults to current directory)
# Copies = how many broken versions you want to output
# Intensity = how broken you want stuff. Can be LOW, NORMAL, HIGH, LUDICROUS, and OMG

import sys

input = sys.argv[1:][0]
output = sys.argv[1:][1]
copies = sys.argv[1:][2]

print("----------------------------------------------------")
print("OK! Fucking up " + input + " " + copies + " time(s)")
print("Fucked-up files will be written to: " + output)
