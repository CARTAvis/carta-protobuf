#!/usr/bin/env python3

import re
import json
import sys
import glob
import os

# FUNCTIONS

def to_snake(word):
    parts = re.findall("[A-Z][a-z]+", word)
    return "_".join(p.upper() for p in parts)

def get_cssclass(parent_dir, anchor):
    cssclass = "sub"
        
    if parent_dir == "control":
        cssclass = "b2f" if anchor.endswith("ack") else "f2b"
    elif parent_dir == "request":
        cssclass = "b2f" if anchor.endswith("response") or anchor.endswith("progress") else "f2b"
    elif parent_dir == "stream":
        cssclass = "f2b" if anchor.endswith("request") else "b2f"
        
    return cssclass 

def auto_cartaref(s, exclude=None):
    search = message_names | snake_names
    if exclude:
        search -= set([exclude, to_snake(exclude)])
    for symbol in search:
        s = re.sub(f"\\b{symbol}\\b", f":carta:refc:`{symbol}`", s)
    return s

# STATE

map_info = {}
message_names = set()
anchor_parent = {}
rst = {}

proto_dir = {os.path.basename(p): os.path.basename(os.path.dirname(p)) for p in glob.glob("../../*/*.proto")}

output_map = {
    "messages": [os.path.basename(p) for p in glob.glob("../../control/*.proto") + glob.glob("../../request/*.proto") + glob.glob("../../stream/*.proto")],
    "defs": ["defs.proto"],
    "enums": ["enums.proto"],
}

# READ

with open(sys.argv[1]) as f:
    data = json.load(f)
    
output_dir = sys.argv[2]

# FIRST PASS

for file_ in data["files"]:
    file_name = file_["name"]
    parent_dir = proto_dir[file_name]
    
    for message in file_["messages"]:
        if message["name"].endswith("Entry") and "." in message["longName"]:
            map_info[message["longName"]] = message
        else:
            message_names.add(message["name"])
            anchor_parent[message["name"].lower()] = parent_dir
    for enum in file_["enums"]:
        message_names.add(enum["name"])
        anchor_parent[enum["name"].lower()] = parent_dir

snake_names = set(to_snake(n) for n in message_names)

# SECOND PASS

for file_ in data["files"]:
    file_name = file_["name"]
    parent_dir = proto_dir[file_name]
    rst[file_name] = []
    
    for message in file_["messages"]:
        output = []
        name = message["name"]
        # Skip map entries
        
        if name.endswith("Entry") and "." in message["longName"]:
            continue
        
        # Message colour
        
        anchor = name.lower()
        cssclass = get_cssclass(parent_dir, anchor)
        output.append(f".. carta:class:: carta-{cssclass} {anchor}\n")
        
        # Message heading
        
        underline = "~" * len(name)
        output.append(f".. _{anchor}:\n\n{name}\n{underline}\n")
        
        # Link to file on github
        
        output.append(f"Source file: `{parent_dir}/{file_name} <https://github.com/CARTAvis/carta-protobuf/blob/dev/{parent_dir}/{file_name}>`_\n")
        
        # Description
        
        description = message["description"]
        description = auto_cartaref(description, name)
        output.append(description)
        
        # Fields
        
        if message["hasFields"]:
        
            field_header = """
.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1
   :class: proto

   * - Field
     - Type
     - Label
     - Description"""
            
            output.append(field_header)
            
            for field in message["fields"]:
                field_name = field["name"]
                
                output.append(f"   * - {field_name}")
                
                if field["ismap"]:
                    map_message = map_info[f"{name}.{field['type']}"]
                    map_key = map_message["fields"][0]["type"]
                    map_value = map_message["fields"][1]["type"]
                    if map_value in message_names:
                        map_value = f":carta:refc:`{map_value}`"
                    field_type = f"map<key: {map_key}, value: {map_value}>"
                elif field["type"] in message_names:
                    field_type = f":carta:refc:`{field['type']}`"
                else:
                    field_type = field["type"]
                
                output.append(f"     - {field_type}")
                output.append(f"     - {field['label']}")
                
                field_desc = field["description"]
                field_desc = field_desc.replace("\n", " ")
                field_desc = auto_cartaref(field_desc, name)
                output.append(f"     - {field_desc}")
        
        output.append("")
        rst[file_name].append((name, "\n".join(output)))
        
    for enum in file_["enums"]:
        output = []
        name = enum["name"]
        
        # Enum colour
        
        anchor = name.lower()
        cssclass = get_cssclass(parent_dir, anchor)
        output.append(f".. carta:class:: carta-{cssclass} {anchor}\n")
        
        # Enum heading
        
        anchor = name.lower()
        underline = "~" * len(name)
        output.append(f".. _{anchor}:\n\n{name}\n{underline}\n")
        
        # Link to file on github
        
        output.append(f"Source file: `{parent_dir}/{file_name} <https://github.com/CARTAvis/carta-protobuf/blob/dev/{parent_dir}/{file_name}>`_\n")
        
        # Description
        
        description = enum["description"]
        description = auto_cartaref(description, name)
        output.append(description)
        
        # Values
                
        val_header = """
.. list-table::
   :widths: 33 33 33
   :header-rows: 1
   :class: proto

   * - Name
     - Number
     - Description"""
        
        output.append(val_header)
        
        for val in enum["values"]:
            val_name = val["name"]
            if name == "EventType":
                val_name = auto_cartaref(val_name)
            output.append(f"   * - {val_name}")
            output.append(f"     - {val['number']}")
            output.append(f"     - {val['description']}")
        
        output.append("")
        rst[file_name].append((name, "\n".join(output)))

# WRITE

for section, filenames in output_map.items():
    elements = []
    
    for filename in sorted(filenames):
        elements.extend(rst[filename])
    
    with open(f"{output_dir}/{section}.rst.txt", "w") as f:
        for name, element in sorted(elements):
            print(element, file=f)
