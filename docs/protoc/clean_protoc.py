#!/usr/bin/env python3

import re
import sys

data = {}

for filename in sys.argv[1:]:
    with open(filename) as f:
        data[filename] = f.read()

symbols = []

def fix_heading(m):
    heading = m.group(1)
    anchor = heading.lower()
    underline = "^" * len(heading)
    return f".. _{anchor}:\n\n{heading}\n{underline}"

for filename in data:
    data[filename] = re.sub("\n(.*?)\n\^{5,}", fix_heading, data[filename])
        
# TODO: build list of symbols across files
# TODO: add explicit anchors for ThingName
# TODO: and also THING_NAME (how?)
# TODO: replace all symbols with references (second pass)

for filename, contents in data.items():
    with open(filename, "w") as f:
        f.write(contents)
