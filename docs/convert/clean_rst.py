#!/usr/bin/env python3

import re
import sys


toctree = """
.. toctree::
   :maxdepth: 2
   :caption: Contents:
""".split()

with open(sys.argv[1]) as icdfile:
    icd = icdfile.read()

# Fix references

def reference(m):
    target = re.sub('%%20', ' ', m.group(2))
    return f':ref:`{m.group(1)} <{target}>`'

icd = re.sub('`([^ <]+) <#([^>]+)>`__', reference, icd)




# TODO inline the inexplicably substituted images

# TODO eventually replace the images with embedded plantuml code?

# TODO pre-calculate the TOC from headers
# We need a nested toctree -- toctrees in the files for section 3 and 4

# Introduction Context Behaviour Layer descriptions

# TODO special includes for the protoc files

# Control messages Request messages Data stream messages Sub-messages Enums
    
with open(sys.argv[2], "w") as indexfile:
    outfile = indexfile
    for line in icd.split("\n"):
        print(line, file=outfile)
