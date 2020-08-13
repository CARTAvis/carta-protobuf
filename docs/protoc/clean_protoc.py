#!/usr/bin/env python3

import re
import sys

data = {}

for filename in sys.argv[1:]:
    with open(filename) as f:
        data[filename] = f.read()

def fix_heading(m):
    heading = m.group(1)
    anchor = heading.lower()
    underline = "^" * len(heading)
    return f".. _{anchor}:\n\n{heading}\n{underline}"

def controlcolour(m):
    fullanchor = m.group(1)
    anchor = m.group(2)
    if "." in anchor:
        return m.group(1)
    cssclass = "b2f" if anchor.endswith("ack") else "f2b"
    return f".. cssclass:: {cssclass}\n\n{fullanchor}"

def requestcolour(m):
    fullanchor = m.group(1)
    anchor = m.group(2)
    if "." in anchor:
        return m.group(1)
    cssclass = "b2f" if anchor.endswith("response") else "f2b"
    return f".. cssclass:: {cssclass}\n\n{fullanchor}"

def streamcolour(m):
    fullanchor = m.group(1)
    anchor = m.group(2)
    if "." in anchor:
        return m.group(1)
    cssclass = "f2b" if anchor.endswith("request") else "b2f"
    return f".. cssclass:: {cssclass}\n\n{fullanchor}"

for filename in data:
    data[filename] = re.sub("\n(.*?)\n\^{5,}", fix_heading, data[filename])
    
    if "control" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", controlcolour, data[filename])
    elif "request" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", requestcolour, data[filename])
    elif "stream" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", streamcolour, data[filename])

for filename, contents in data.items():
    with open(filename, "w") as f:
        f.write(contents)
