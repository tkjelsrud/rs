#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "Barack Obama"
__copyright__   = "Copyright 2009, Planet Earth"

#Actebis_SKU	Mfr_SKU	Mfr_Name	Product_Group	Product_Text	Product_Description	
#Price		Stock_Qty	Stock_Date	Barcode	TaxKey
#


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
