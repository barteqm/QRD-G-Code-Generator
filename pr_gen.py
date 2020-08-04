#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple code generating matrix file for main generator 
# Copyright by Bartek Magdon
# barteqm@gmail.com

import sys,csv,math
#Start
if __name__ == "__main__":
	print "Diffuser CSV Generator"
	if len(sys.argv) != 5:
	    print "Usage: " + sys.argv[0] + " <p> <height multiplier of qrd > <width multiplier of qrd> <output_file.csv>"
	    print "Where p is non even prime number"
	    sys.exit(1)
	#Input Path
	p = int(sys.argv[1])
	height=float(sys.argv[2])
	width=float(sys.argv[3])
	path_matrix=sys.argv[4]
	matrix_file = open(path_matrix,'w')
	well_width=width/(p+1)
	#qr_table = [0]*(p+1)
	b=2
	for a in range(1,p):
		qr = int(math.fmod(pow(b,a),p))
		#qr_table[a][0]=qr
		if a==p-1: 
			separator="" 
		else:
			separator=";"
		file_input = str(qr) + separator
		matrix_file.write(file_input)
	#matrix_file.write("\n")
	well_width=width/(p+1)
	#DFmax=2*height/max(qr_table)
	#DFmin = 0
	print "Single well width:",well_width
	print "Maximum Well heigjt:", (p-1)*height
	#print "Well width Ratio must be less than twoa nd is:", DFmax/2
	#print 2^2
	#print DFmax