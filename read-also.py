#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "Barack Obama"
__copyright__   = "Copyright 2009, Planet Earth"

try:
	f = open('also_10606786.txt', 'r')
	hLine = True
	for line in f:
		if hLine:
			# Head line
			hLine = False
		pr = line.split("\t")
		print(pr)
except:
		print("ERROR" + sys.exc_info()[0]) 
