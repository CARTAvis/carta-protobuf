#!/usr/bin/env python3

import re
import sys
import os
from collections import defaultdict

inputname, destdir = sys.argv[1:3]

with open(inputname) as icdfile:
    icd = icdfile.read()

# Fix references

def reference(m):
    label = m.group(1)
    target = re.sub('%%20', ' ', m.group(2))
    if label.lower().replace('_', '') == target.lower():
        return f':carta:`{label}`'
    return f':ref:`{label} <{target}>`'

icd = re.sub('`([^`<]+) <#([^>]+)>`__', reference, icd)

# Remove nested markup from custom colour roles (for now)

icd = re.sub(':f2b:```(.*?)```', r':f2b:`\1`', icd)
icd = re.sub(':b2f:```(.*?)```', r':b2f:`\1`', icd)

# inline the inexplicably substituted images and replace them with plantuml

icd = re.sub(r'#\. (.*?)\\ (\|image\d+\|)', r'\1\n\n\2\n', icd)

images = re.findall('(\.\. )(\|image\d+\|) (image:: images/.*.png)', icd)

icd = re.sub('\.\. \|image\d+\| image:: images/.*.png\n', "", icd)

for begin, placeholder, end in images:    
    img_name = re.search("images/(.*).png", end).group(1)
    with open(f"uml/{img_name}.plantuml") as f:
        uml_block = f.read()
    uml_block = re.sub(r"\\n", r"\\\\n", uml_block)
    uml_block = re.sub("^", "    ", uml_block, flags=re.MULTILINE)
    
    icd = re.sub(re.escape(placeholder), f".. uml::\n{uml_block}", icd)

# We need a nested toctree -- toctrees in the files for section 3 and 4

sections = re.findall("\n(.*?)\n={4,}", icd)
subsections = re.findall("\n(.*?)\n-{4,}", icd)

# Destination filenames

filenames = {s: f'{s.lower().replace(" ", "_")}.rst' for s in sections + subsections}
filenames["index"] = "index.rst"
filenames["changelog"] = "changelog.rst.txt"

# special includes for the protoc files

protoc = {
    "Control messages": "control.rst.txt",
    "Request messages": "request.rst.txt",
    "Data stream messages": "stream.rst.txt",
    "Sub-messages": "defs.rst.txt",
    "Enums": "enums.rst.txt",
}

toctree_index = """
.. toctree::
   :numbered: 3
   :caption: Contents:
"""

toctree_section = """
.. toctree::
   :caption: Contents:
"""

file_contents = defaultdict(list)
    
lines = iter(icd.split("\n"))
indexfile = filenames["index"]
sectionfile = None
currentfile = indexfile

has_toctree = {}

for line in lines:
    is_anchor = re.match(".. _(.*):", line)
    anchor = is_anchor.group(1) if is_anchor else None
    if is_anchor and anchor in filenames:
        line = f'.. _{anchor.lower().replace(" ", "-")}:'
        currentfile = filenames[anchor]
        if anchor in sections:
            sectionfile = currentfile
            if not has_toctree.get(indexfile, False):
                file_contents[indexfile].append(toctree_index)
                has_toctree[indexfile] = True
            file_contents[indexfile].append(f'   {filenames[anchor].replace(".rst", "")}')
        elif anchor in subsections:
            if not has_toctree.get(sectionfile, False):
                file_contents[sectionfile].append(toctree_section)
                has_toctree[sectionfile] = True
            file_contents[sectionfile].append(f'   {filenames[anchor].replace(".rst", "")}')
    elif line == "**Changelog**":
        file_contents[currentfile].append(f".. include:: {filenames['changelog']}")
        currentfile = filenames["changelog"]
    
    file_contents[currentfile].append(line)
    
    # protoc includes
    
    if line in protoc:
        file_contents[currentfile].append(next(lines)) # underline
        file_contents[currentfile].append("")
        file_contents[currentfile].append(f".. include:: {protoc[line]}")
    
for filename, contents in file_contents.items():
    with open(os.path.join(destdir, filename), "w") as f:
        for line in contents:
            print(line, file=f)
