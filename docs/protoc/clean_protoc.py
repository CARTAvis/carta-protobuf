#!/usr/bin/env python3

import re
import json
import sys
import glob
import os

with open(sys.argv[1]) as f:
    data = json.load(f)

map_info = {}
message_names = set()

for file_ in data["files"]:
    for message in file_["messages"]:
        if message["name"].endswith("Entry"):
            map_info[message["longName"]] = message
        else:
            message_names.add(message["name"])
    for enum in file_["enums"]:
        message_names.add(enum["name"])

def to_snake(word):
    parts = re.findall("[A-Z][a-z]+", word)
    return "_".join(p.upper() for p in parts)

snake_names = set(to_snake(n) for n in message_names)

rst = {}

proto_dir = {os.path.basename(p): os.path.basename(os.path.dirname(p)) for p in glob.glob("../../*/*.proto")}

for file_ in data["files"]:
    file_name = file_["name"]
    parent_dir = proto_dir[file_name]
    output = []
    
    for message in file_["messages"]:
        name = message["name"]
        # Skip map entries
        
        if name.endswith("Entry"):
            continue
        
        # Message colour
        
        anchor = name.lower()
        cssclass = None
        
        if parent_dir == "control":
            cssclass = "b2f" if anchor.endswith("ack") else "f2b"
        elif parent_dir == "request":
            cssclass = "b2f" if anchor.endswith("response") or anchor.endswith("progress") else "f2b"
        elif parent_dir == "stream":
            cssclass = "f2b" if anchor.endswith("request") else "b2f"
        
        if cssclass:
            output.append(f".. cssclass:: {cssclass}\n")
        
        # Message heading
        
        underline = "^" * len(name)
        output.append(f".. _{anchor}:\n\n{name}\n{underline}\n")
        
        # Link to file on github
        
        output.append(f"Source file: `{parent_dir}/{file_name} <https://github.com/CARTAvis/carta-protobuf/blob/dev/{parent_dir}/{file_name}>`_\n")
        
        # Description
        
        description = message["description"]
        for symbol in message_names | snake_names - set([name, to_snake(name)]):
            description = re.sub(f"\\b{symbol}\\b", f":carta:`{symbol}`", description)
        output.append(description)
        
        # Fields
        
        if message["hasFields"]:
        
            field_header = """
.. list-table::
   :widths: 25 25 10 40
   :header-rows: 1

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
                        map_value = f":carta:`{map_value}`"
                    field_type = f"map<key: {map_key}, value: {map_value}>"
                elif field["type"] in message_names:
                    field_type = f":carta:`{field['type']}`"
                else:
                    field_type = field["type"]
                
                output.append(f"     - {field_type}")
                output.append(f"     - {field['label']}")
                
                field_desc = field["description"]
                field_desc = field_desc.replace("\n", " ")
                for symbol in message_names | snake_names - set([name, to_snake(name)]):
                    field_desc = re.sub(f"\\b{symbol}\\b", f":carta:`{symbol}`", field_desc)
                
                output.append(f"     - {field_desc}")
        
            output.append("")
        
    for enum in file_["enums"]:
        name = enum["name"]
        
        # Enum heading
        
        anchor = name.lower()
        underline = "^" * len(name)
        output.append(f".. _{anchor}:\n\n{name}\n{underline}\n")
        
        # Link to file on github
        
        output.append(f"Source file: `{parent_dir}/{file_name} <https://github.com/CARTAvis/carta-protobuf/blob/dev/{parent_dir}/{file_name}>`_\n")
        
        # Description
        
        description = enum["description"]
        for symbol in message_names | snake_names - set([name, to_snake(name)]):
            description = re.sub(f"\\b{symbol}\\b", f":carta:`{symbol}`", description)
        output.append(description)
        
        # Values
                
        val_header = """
.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - Name
     - Number
     - Description"""
        
        output.append(val_header)
        
        for val in enum["values"]:
            output.append(f"   * - {val['name']}")
            output.append(f"     - {val['number']}")
            output.append(f"     - {val['description']}")
        
        output.append("")
        
    rst[file_name] = "\n".join(output)

output_map = {
    "control": [os.path.basename(p) for p in glob.glob("../../control/*.proto")],
    "request": [os.path.basename(p) for p in glob.glob("../../request/*.proto")],
    "stream": [os.path.basename(p) for p in glob.glob("../../stream/*.proto")],
    "defs": ["defs.proto"],
    "enums": ["enums.proto"],
}

for section, filenames in output_map.items():
    with open(f"../{section}.rst.txt", "w") as f:
        for filename in sorted(filenames):
            print(rst[filename], file=f)
