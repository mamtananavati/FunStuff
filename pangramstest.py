#!/usr/bin/python
import sys

"""The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. Such sentences are called pangrams. You are to write a program, which takes a sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII characters.In case the input sentence is already a pangram, print out the string NULL
   Input

   Your program should accept as its first argument a filename. This file will contain several text strings, one per line. Ignore all empty lines. eg.
   A quick brown fox jumps over the lazy dog
   A slow yellow fox crawls under the proactive dog

   Output
   Print out all the letters each string is missing in lowercase, alphabetical order .e.g.
   NULL
   bjkmqz
"""



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


