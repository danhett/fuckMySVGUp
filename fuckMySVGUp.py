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
# Input file = the SVG you want to fuck . Required.
# Output dir = the directory to spit out into. Default: current directoy.
# Copies = how many broken versions you want to output. Default: one.
# Intensity = Can be LOW, NORMAL, HIGH, LUDICROUS, and OMG. Default: Normal.

import sys
import os.path

if os.path.isfile(sys.argv[1:][0]) == True:
    input = sys.argv[1:][0]
else:
    print("Error: Input SVG not found!")
    sys.exit()

output = sys.argv[1:][1]
copies = sys.argv[1:][2]
intensity = sys.argv[1:][3]

print("--------- FUCK MY SVG UP ---------")
print("OK! Fucking up " + input + " " + copies + " time(s) using " + intensity + " intensity!")
print("Fucked-up files will be written to: " + output)
