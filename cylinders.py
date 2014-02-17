#!/bin/python

import sys
import subprocess

heads = 255
sectors = 63
block_size = 512

def usage(prog):
	print("Usage: %s /dev/sdX" %prog)

def cylinders(size):
	return size/(heads*sectors*block_size)	


if __name__ == "__main__":
	prog_name = sys.argv[0]
	if(len(sys.argv) != 2):
		usage(prog_name)
		exit(1)
		
	dev = sys.argv[1]
	cmd = ["lsblk", "-d", "-b", "-n", "-o", "size", dev]

	try:
		size = subprocess.check_output(cmd)	
	except subprocess.CalledProcessError:
		usage(prog_name)
		exit(1)
	
	num_of_cylinders = cylinders(int(size))
	print("The number of cylinders: %d" %num_of_cylinders)
