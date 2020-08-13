#!/usr/bin/env python3

import re
import sys

data = {}

for filename in sys.argv[1:]:
    with open(filename) as f:
        data[filename] = f.read()

# For automatic hyperlinks later
symbols = set()

# Add anchors to all headings

def fix_heading(m):
    heading = m.group(1)
    anchor = heading.lower()
    if not "." in anchor:
        symbols.add(heading)
    underline = "^" * len(heading)
    return f".. _{anchor}:\n\n{heading}\n{underline}"

# Colour some messages red or blue

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

# Separate map entry to remove and add to the main message table

ENTRY_TABLE = re.compile(r"""
\.\. _.*\..*entry:

(.*)\.(.*Entry)
\^+




\.\. list-table::
   :widths: 25 25 10 40
   :header-rows: 1

   \* - Field
     - Type
     - Label
     - Description
   \* - key
     - (.*)
     - 
     - 
   \* - value
     - (.*)
     - 
     - 
""")

map_info = {}

for filename in data:
    data[filename] = re.sub("\n(.*?)\n\^{5,}", fix_heading, data[filename])
    
    if "control" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", controlcolour, data[filename])
    elif "request" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", requestcolour, data[filename])
    elif "stream" in filename:
        data[filename] = re.sub("(\.\. _(.*):)", streamcolour, data[filename])
    
    # Gather the map info and delete the map entries in the first pass
    for msgname, mapname, keytype, valuetype in  ENTRY_TABLE.findall(data[filename]):
        map_info[(msgname, mapname)] = (keytype, valuetype)
    
    data[filename] = ENTRY_TABLE.sub("", data[filename])
    
# Second pass to rewrite the maps in the main tables

for filename in data:
    for (msgname, mapname), (keytype, valuetype) in map_info.items():
        data[filename] = re.sub(f"({msgname}\n\^+.*?- ){mapname}", f"\\1map<key: {keytype}, value: {valuetype}>", data[filename], flags=re.DOTALL)
        
# Third pass to add automatic :carta: hyperlinks to all messages
symbols_lower = set(s.lower() for s in symbols)

def auto_snake_link(m):
    name = m.group(1)
    if name.lower().replace("_", "") in symbols_lower:
        return f":carta:`{name}`"
    return m.group(0)

for filename in data:
    # Automatic links for CamelCaseNames not at the start of a line
    for symbol in symbols:
        data[filename] = re.sub(f"(?<!^)\\b{symbol}\\b", f":carta:`{symbol}`", data[filename], flags=re.MULTILINE)
        
    # Automatic links for recognised SNAKE_CASE_NAMES not at the start of a line
    data[filename] = re.sub(r"(?<!^)\b([A-Z_]{3,})\b", auto_snake_link, data[filename], flags=re.MULTILINE)

for filename, contents in data.items():
    with open(filename, "w") as f:
        f.write(contents)
