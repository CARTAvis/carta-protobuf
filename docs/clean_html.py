#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

colours = {
    "c0": "red",
    "c16": "blue",
    "c84": "orange",
}

replacements = {
    "c4": "strong",
    "c5": "code",
    "c19": "code",
    "c36": "code",
    "c57": "code",
    "c79": "em",
    "c95": "em",
}

soup.style.clear()
soup.style.append(".orange { color: #ff9900 } .blue { color: #0b5394 } .red { color: #741b47 }")

for tag_name in ("body", "a", "h1", "h2", "h3", "table", "thead", "tbody", "tr", "td", "th", "ul", "ol", "li"):
    for tag in soup.find_all(tag_name):
        if "class" in tag.attrs:
            del tag.attrs["class"]
            
for tag in soup.find_all("p"):
    if "class" in tag.attrs:
        if "title" in tag["class"]:
            tag.name = "h1"
        
        del tag["class"]

for tag in soup.find_all("span"):
    if "class" in tag.attrs:
        for k, v in colours.items():
            if k in tag["class"]:
                new_span = soup.new_tag("span")
                new_span["class"] = [v]
                tag.wrap(new_span)
        
        for k, v in replacements.items():
            if k in tag["class"]:
                tag.wrap(soup.new_tag(v))
                
    tag.unwrap()
    
for tag in soup.find_all("img"):
    tag.attrs = {"src": tag["src"]}

# TODO fix FOO_BAR_BAZ text which doesn't have the right code formatting
# TODO fix messed-up consecutive lists (by hand?)
# TODO some of the images are huge -- different resolution? Fix.

print(soup.prettify())

