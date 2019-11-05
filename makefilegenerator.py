# C++ makefile generator
# Written in Python (oddly enough)
# Josh Jeppson

# Instructions: put file into directory for C/C++ code and run in Python
import sys
import glob
import os

def add_item(flist, dlist, directory):
	# Clear screen
	sys.stderr.write("\x1b[2J\x1b[H")
	# Print each file in directory with a number
	i = 1
	files_in_directory = []
	print("Available Files: ")
	for file in os.listdir(directory):
		files_in_directory.append[str(file)]
		print(i, ". ", str(file))
	# Promp user for file:
	

def main()
	directory = input("Enter directory name: ")
	os.chdir(directory)
	f = open("makefile", "w")
	f.write("all: ")
	exename = input("Final output filename: ")
	f.write(exename, "\n\n")
	# String for the first line of the final output from the *.o's to the .exe
	fline = exename + ": "
	gline = "g++ "
	# List of .o filenames 
	flist = []
	# List of their dependencies
	dlist = []
	done = False
	while not done:
		add_item(flist, dlist, directory)
		done = ("y" == input("Add another dependency? [Y/N]").lower())
		
	for itm in flist:
		fline += itm + " "
		gline += itm + " "
	
	gline += "-o " + exename
	f.write(fline, "\n\t", gline)
	
	f.close()




main()