# C++ makefile generator
# Written in Python (oddly enough)
# Josh Jeppson

# Instructions: put file into directory for C/C++ code and run in Python

# This code--unfinished and tiny as it is--is open source. Feel free to clone, 
# fork, redistribute, etc., it. I know it's small now, but it will grow, adding
# features, etc.

# This code is designed to be a simple script for makefile generation for C and
# C++. It's (will be when it's done) useful for small (and large) projects.

# Currently code is not functional, but will be worked on and will eventually be useful
import sys
import glob
import os

g = ""

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
		i = i + 1;
	# Promp user for file:
	flist.append(input("File for input: ")
	files = input("Enter numbers of files separated by spaces that are dependant on above file")
	files.split(" ")

def main()
	# Make compatible with C and C++
	print("C or C++?\n1. C\n2. C++")
	ans = input()
	if ans == "1":
		g = "gcc "
	elif ans == "2":
		g = "g++ "
	# Go to prompted directory
	directory = input("Enter directory name: ")
	os.chdir(directory)
	f = open("makefile", "w")
	f.write("all: ")
	exename = input("Final output filename: ")
	f.write(exename, "\n\n")
	# String for the first line of the final output from the *.o's to the .exe
	fline = exename + ": "
	gline = g
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
