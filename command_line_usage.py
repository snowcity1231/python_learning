#!/usr/bin/python3

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('GetoptError, usage: command_line_usage.py -i <inputfile> -0 <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('usage:command_line_usage.y -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
        
