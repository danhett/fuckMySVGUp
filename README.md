# Fuck My SVG Up!
If you need to fuck an SVG up, fuckMySVGUp will fuck your SVG up

### Wha?
This is a quick and dirty python script that takes an SVG and smashes it up. Nothing clever but quite nice.

### How?
- Get the source
- Stick an SVG somewhere
- Run something like `python fuckMySVGUp.py kitty.svg output 10 NORMAL`
- Arguments are: input SVG, output folder for glitches, number of outputs, intensity (currently does nothing but needed to run)

### Notes
- This is very brute force and sometimes makes wonky sized or entirely broken outputs
- I don't care.
- Enjoy!

### Output examples
Source image:
![original](https://raw.githubusercontent.com/danhett/fuckMySVGUp/master/examples/orig.jpg)

Outputs:
![image1](https://raw.githubusercontent.com/danhett/fuckMySVGUp/master/examples/glitch1.jpg)

![image2](https://raw.githubusercontent.com/danhett/fuckMySVGUp/master/examples/glitch2.jpg)

![image2](https://raw.githubusercontent.com/danhett/fuckMySVGUp/master/examples/glitch3.jpg)

### Todo list
Stuff that might be cool:
- Add proper colour shifting
- Noodle with things more intelligently to avoid unusably glitched images
- Either ignore or reinsert headers so images actually render
- Pop a video out with ffmpeg or something
- Ideally stop mis-sized outputs clipping, or constrain sizes etc 

### License
Released under the DO WHAT THE FUCK YOU WANT public license (see LICENSE.md for more info).
