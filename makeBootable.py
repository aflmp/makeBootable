#!/usr/bin/python
import subprocess, argparse, stat, sys, os, re

def disk_exists(path):
	try:
		return stat.S_ISBLK(os.stat(path).st_mode)
	except:
		return False

parser = argparse.ArgumentParser()
parser.add_argument('-if', '--inputfile', help='specify the input file', action='store')
parser.add_argument('-of', '--outputfile', help='specify the output file', action='store')
args = parser.parse_args()

print(args.inputfile)
print(args.outputfile)
command1 = 'diskutil list'
p1 = subprocess.Popen(command1, shell=True)
p1.wait()

if args.outputfile:
	if not disk_exists(args.outputfile):
		sys.exit('Exiting...  Incorrect path')
	output_file = args.outputfile
else:
	output_file = raw_input('destination disk path:   ')
	if not disk_exists(output_file):
		sys.exit('Exiting...  Incorrect path')

if args.inputfile:
	if not os.path.isfile(args.inputfile):
		sys.exit('Exiting... Incorrect path')
	input_file = args.inputfile
else:
	input_file = raw_input('complete source iso path:   ')
	if not os.path.isfile(input_file):
		sys.exit('Exiting... Incorrect path')
		 
command2 = 'diskutil unmountDisk '+ output_file
p2 = subprocess.Popen(command2, shell=True)
p2.wait()

output_rfile = re.split("([\/])",output_file)
output_rfile.insert(4,'r')
output_rfile = "".join(output_rfile[1:])

command3 = 'sudo dd bs=1m if='+input_file+' of='+output_rfile
print('Writing to disk...')
p3 = subprocess.Popen(command3, shell=True)
p3.wait()

command4 = 'diskutil eject '+ output_file
print('command4: %s' %command4)
p4 = subprocess.Popen(command4, shell=True)
p4.wait()

print('Bootable USB created!')
