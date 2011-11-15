#!/usr/bin/python
import sys

set_of_english_characters = set([chr(x) for x in xrange(97,123)])

if len(sys.argv) < 2:
        print "Please Enter Filename"
        sys.exit(-1)
else:
        filename = sys.argv[1]
        file = open(filename,"r")

        for line in file:
                if line.strip() != "":
                        set_of_characters_in_line = set(list(line.lower()))
                        differences = set_of_english_characters.difference(set_of_characters_in_line)
                        if len(differences) == 0 :
                                print "NULL"
                        else:
                                print ''.join(differences)


