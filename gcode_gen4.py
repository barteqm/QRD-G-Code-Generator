#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by Bartek Magdon
# barteqm@gmail.com

import sys,csv,StringIO,math
import datetime,time
#Start
if __name__ == "__main__":
	print "Diffuser g-code Generator"
	# Main variables:
	path_header="header.gcode"
	path_footer="footer.gcode"
	#material_height=500 #mm
	#material_width=1000 #mm
	# Material Safety offset - gives safe distance from material when wire is not cutting
	material_safety_offset=float(10) #mm
	

	if len(sys.argv) != 8:
	# <matrix_file.csv>  - file with shape of diffuser in universal units. generated with qrd_gen.py
	# <cutting_velocity>  - velocity used when cutting material - has to be set experimentally - velocity depends on humidity of foam, temp of cutting wire etc.
	# <bottom offset> - depth of bottom layer of diffuser that holds everything in place
	# <material_height> - height of a single styrofoam prefab
	# <material_width>  - width of a single styrofoam prefab
	# <divider> - how many prefabs are generated
	# <output_file.nc> - gcode output file
	#

	    print "Usage: " + sys.argv[0] + " <matrix_file.csv> <cutting_velocity> <bottom offset> <material_height> <material_width> <divider> <output_file.nc>"
	    sys.exit(1)
	#matrix input path
	path_matrix = sys.argv[1]
	#Arguments
	
	velocity = float(sys.argv[2])
	bottom_offset = float(sys.argv[3])
	material_height=float(sys.argv[4]) #mm
	material_width=float(sys.argv[5]) #
	divider_y=int(sys.argv[6])
	#OUTPUT PATH
	path_out = sys.argv[7]
	# files - opening
	
	matrix_file = open(path_matrix)
	header_file = open(path_header)
	footer_file = open(path_footer)
	gcode_file = open(path_out, 'w')
	header = header_file.read()
	# creating array from csv file:
	f = StringIO.StringIO(matrix_file.read())
	reader = csv.reader(f, delimiter=';')
	matrix_data = list(reader)
	matrix_float = [float(s) for ss in matrix_data for s in ss]
	max_number = max(matrix_float)
	material_safety_offset_x=material_height+material_safety_offset
	max_h=material_height+material_safety_offset
	
	if max_h>=605: 
		max_height=604 
	else: 
		max_height=max_h
#	max_height=1000
# creating stats data for nc file header
	height=round((material_height/divider_y-2*bottom_offset)/max_number,3)
	size=round(material_width/len(matrix_data[0]),2)
	localtime = time.asctime( time.localtime(time.time()) )
	header_data = ''.join([ "(Matrix File: ", path_matrix, ")\n" ,
	"(Output File: ", path_out, ")\n" ,
	"(Generator name: ", sys.argv[0], ")\n" ,
	"(Date Generated: ", localtime , ")\n" ,
	"(--------------------------------------------------------------", ")\n" ,
	"(Diffuser total width:  ", str(size*len(matrix_data[0])), "mm", ")\n" ,
	"(Material total height: ", str(material_height), ")\n" ,
	"(Single  diffuser height: ", str(material_height/divider_y), ")\n" ,
	"(Material length: ", str(material_width), ")\n" ,
	"(--------------------------------------------------------------", ")\n" ,
	"(Single column width: ", str(size), "mm", ")\n" ,
	"(Single column height unit: ", str(height), "mm", ")\n" ,
	"(Max column height: ",str(max(matrix_float)*height), "mm", ")\n" ,
	"(Cutting speed: ", str(velocity), "mm/min", ")\n" ,
	"(Material Safety offset: ", str(material_safety_offset),"mm", ")\n" ,
	"(Bottom height: ", str(bottom_offset), "mm", ")\n" ,
	"(--------------------------------------------------------------", ")\n" ,
	"(Number of styrofoam prefabs in single cut: ", str(divider_y), " pieces", ")\n"  ])
	# print header to file
	gcode_file.write(header)
	print header_data
# inserting header data file with custom parameters
	gcode_file.write(header_data)
	gcode_file.write("\n(--------------------------------------------------------------)\n")
	gcode_file.write("(                        PROGRAM START                         )\n")
	gcode_file.write("(--------------------------------------------------------------)\n\n")
	k=0
	# main generator loop
	for k in range(0,divider_y):	
		i=0
		divider_offset=k*material_height/divider_y
	# single shape generator loop
		for i in range(len(matrix_data)):
			code_line_Set1="G00 X" + str(material_safety_offset*-1)
			gcode_file.write(code_line_Set1)
			gcode_file.write("\n")
			code_line_Set2="G00 Y" + str(int(matrix_data[0][0])*height+bottom_offset+divider_offset)
			gcode_file.write(code_line_Set2)
			gcode_file.write("\n")
			code_line_Set1="G00 X 0"
			gcode_file.write(code_line_Set1)
			gcode_file.write("\n")
			code_velocity= "G01 F"+ str(velocity)
			gcode_file.write(code_velocity)
			gcode_file.write("\n")		
			j=0
			for j in range(len(matrix_data[i])):
				code_line1 = "G01 "+ "X" + str(j * size) #+ " " + "F"+ str(velocity)
				code_line2 = "G01 "+ "Y" + str(int(matrix_data[i][j]) * height+bottom_offset+divider_offset)# + " " + "F" + str(velocity)
				gcode_file.write(code_line1)
				gcode_file.write("\n")
				gcode_file.write(code_line2)
				gcode_file.write("\n")
			
			code_line_Back1="G01 X"+ str(material_width+material_safety_offset*2) + "\n"
			gcode_file.write(code_line_Back1)
	
			code_line_Back2="G00 Y" + str(max_height) + "\n" + "G00 X"+ str(0-material_safety_offset) +"\n" + "(Koniec Plaszczyzny nr:" + str(i+1) + ")\n"
			gcode_file.write(code_line_Back2)
		code_line_Back3="(END OF LAYER: " + str(k+1) + ")\n"
		gcode_file.write(code_line_Back3)
	
	footer = footer_file.read()
	# footer write
	gcode_file.write(footer)
	print "Finished OK!"
	# closing of files
	gcode_file.close()
	matrix_file.close()
	header_file.close()
	footer_file.close()
	
