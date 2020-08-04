
# Simple G-code generator app

> Generates G-Code for CNC foam cutter. Allows to make producton files based on CSV templates. CSV templates are generated with additional py scripts.

> GCODE, QRD, DIY, PrimeRoot, Quadratic, Residue




## Table of Contents


- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)



## Installation

- GIT clone repository to your computer
- Make py files executable
- Run program with command line parameters
- Samples and ready to go production files are provided

### Clone

- Clone this repo to your local machine using `https://github.com/barteqm/QRD-G-Code-Generator/`

---

## Features

## Usage (Optional)
- pr_gen.py - generates 2D prime root matrices for gcode generator
- qrd_gen.py - generates 2D quadratic residue matrices for gcode generator
- you can also use your own matrices with custom well/column properties that gcode_gen.py will acceppt
- in CSV folder you can find sample matrices in csv format to use with generator

Usage:
> gcode_gen <matrix_file.csv> <cutting_velocity> <bottom offset> <material_height> <material_width> <divider> <output_file.nc>

Where:
 <matrix_file.csv>  - file with shape of diffuser in universal units. generated with qrd_gen.py
 <cutting_velocity>  - velocity used when cutting material - has to be set experimentally - velocity depends on humidity of foam, temp of cutting wire etc.
 <bottom offset> - depth of bottom layer of diffuser that holds everything in place
 <material_height> - height of a single styrofoam prefab
 <material_width>  - width of a single styrofoam prefab
 <divider> - how many prefabs are generated
 <output_file.nc> - gcode output file
	



---

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.