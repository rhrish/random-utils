#! /usr/bin/python

import sys, getopt
import json
import re

def help():
    print 'lookup.py -d <delimiter> -f <field> -l <lookupfile>'
    sys.exit(2)


def main(argv):
    delimiter = ','
    field = 1
    lookupfile = 'codes.json'
    try:
        opts, args = getopt.getopt(argv,"hd:f:l:",["delimiter=","field=","lookup_file="])
    except getopt.GetoptError:
        help()
    for opt,arg in opts:
        if opt == "-h":
            help()
        elif opt in ("-d","--delimiter"):
            delimiter = arg
        elif opt in ("-f","--field"):
            field = int(arg)
        elif opt in ("-l","--lookup_file"):
            lookupfile = arg
    try:
        f = open(lookupfile,"r")
    except IOError:
        help()
    content = json.loads(f.read())
    f.close()
    for line in sys.stdin:
        data = line.split(delimiter)
        wdata = re.sub('[^A-Za-z0-9]','',data[(field-1)].encode("utf-8"))
        repl = content["data"][wdata]
        print re.sub(wdata,repl,line),

if __name__ == "__main__":
    main(sys.argv[1:])
