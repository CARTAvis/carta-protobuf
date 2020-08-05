#!/usr/bin/env python3

import re
import sys
import subprocess
from bs4 import BeautifulSoup

with open(sys.argv[1]) as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

# get styles
css_entries = re.findall(r"([^{]+)\{(.*?)\}", soup.style.text)
c_classes = [(k, v) for (k, v) in css_entries if re.match("\.c\d+", k)]

# map old styles to new semantic tags and colours
mapping_search = {
    "strong": "font-weight:700",
    "code": "Courier New",
    "em": "font-style:italic",
}


colour_search = {
    "comment": "#ff9900",
    "f2b": "#0b5394",
    "b2f": "#741b47",
}

mapping = {}
colour = {}

for k, v in c_classes:
    for new, old in mapping_search.items():
        if old in v:
            mapping[k.replace('.', '')] = new
    for new, old in colour_search.items():
        if old in v:
            colour[k.replace('.', '')] = new

# styles (placeholders for legibility)
soup.style.clear()
soup.style.append("""
.comment { color: #ff9900 }
.f2b { color: #0b5394 } 
.b2f { color: #741b47 }
td {
    border: solid 1px black;
    padding: 10px;
}
table {
    border: solid 1px black;
    border-collapse: collapse;
    margin: 10px 0;
}
""")

# strip styles
for tag_name in ("body", "a", "h1", "h2", "h3", "h4", "h5", "h6", "table", "thead", "tbody", "tr", "td", "th", "ul", "ol", "li"):
    for tag in soup.find_all(tag_name):
        if "class" in tag.attrs:
            del tag.attrs["class"]
        if "style" in tag.attrs:
            del tag.attrs["style"]

# convert title
for tag in soup.find_all("p"):
    if "class" in tag.attrs:
        if "title" in tag["class"]:
            tag.name = "h1"
        
        del tag["class"]
        
# remove rules
for hr in soup.find_all("hr"):
    hr.extract()

# convert old style spans to semantic tags and colours
for tag in soup.find_all("span"):
    if "class" in tag.attrs:
        for k, v in colour.items():
            if k in tag["class"]:
                new_span = soup.new_tag("span")
                new_span["role"] = [v]
                tag.wrap(new_span)
        
        for k, v in mapping.items():
            if k in tag["class"]:
                tag.wrap(soup.new_tag(v))
                
    tag.unwrap()

# strip styles
for tag in soup.find_all("img"):
    tag.attrs = {"src": tag["src"]}

# remove empty paragraphs
for tag in soup.find_all("p"):
    if not tag.contents or (not tag.get_text().strip() and not tag.find_all("img")):
        tag.extract()

        
# merge and nest specific lists correctly

# nests under first li (that's all we need)
def nest(l1, l2):
    l1.li.append(l2.extract())

# only merges first li (also all we need)
def merge(l1, l2):
    l1.append(l2.li)
    l2.extract()

lists = soup.find_all("ol")
first, second = lists[:6], lists[6:]

nest(first[0], first[1])
nest(first[2], first[3])
nest(first[4], first[5])

merge(first[0], first[2])
merge(first[0], first[4])

for i in range(5):
    nest(second[i], second[i].find_next("p"))
    second[i].p.unwrap()

merge(second[0], second[1])
merge(second[0], second[2])
merge(second[0], second[3])
merge(second[0], second[4])

# merge adjacent text elements
for e in soup.find_all():
    e.smooth()

# remove non-breaking spaces
for t in soup.find_all(None, text=re.compile(".+")):
    t.replace_with(t.replace('\xa0', ' '))

# fix unformatted event names
caps_text = re.compile("[A-Z]{2,}_[A-Z]{2,}")

def has_ancestor(element, name):
    if element.parent.name == "html":
        return False
    if element.parent.name == name:
        return True
    return has_ancestor(element.parent, name)

strings = soup.find_all(None, text=caps_text)

for s in strings:
    if not has_ancestor(s, "code"):
        parent = s.parent
        pos = parent.contents.index(s)
        s.extract()
        parts = re.split("( )", s)
        for i, p in enumerate(parts):
            if caps_text.match(p):
                c = soup.new_tag("code")
                c.append(p)
                parent.insert(pos + i, c)
            else:
                parent.insert(pos + i, p)

# add colour span parent to <code> or <a> if it is surrounded by the same colour siblings

def colour_of(t):
    if hasattr(t, "attrs") and "role" in t.attrs:
        has_colour = {"b2f", "f2b", "comment"}.intersection(t["role"]) or None
        if has_colour:
            return has_colour.pop()
    if t.name == 'html':
        return None
    return colour_of(t.parent)

links = soup.find_all("a")
for link in links:
    tag = link
    if tag.parent.name in ("code", "em", "strong"):
        tag = tag.parent
    c = [colour_of(t) for t in (tag.previous_sibling, tag.next_sibling) if t and colour_of(t)]
    if len(c) == 1 or len(c) == 2 and c[0] == c[1]:
        new_span = soup.new_tag("span")
        new_span["role"] = [c[0]]
        tag.wrap(new_span)

# merge adjacent code tags; move trailing spaces inside code tags to the outside
code = soup.find_all("code")
for c in code:    
    if not c.parent:
        continue # extracted
    
    for s in c.next_siblings:
        if s.name == "code":
            c.extend(s.contents)
            s.extract()
        else:
            break
    
    pos = c.parent.contents.index(c)
    
    if c.text.endswith(" "):
        c.parent.insert(pos + 1, " ")
    if c.text.startswith(" "):
        c.parent.insert(pos, " ")
    c.parent.smooth()
    
    first = last = c
    
    while first.name:
        first = first.contents[0]
    first.replace_with(first.lstrip(" "))
    
    while last.name:
        last = last.contents[-1]
    last.replace_with(last.rstrip(" "))

# links outside code

for c in soup.find_all("code"):
    child = c.contents[0]
    if child.name == "a":
        c.name = "a"
        c["href"] = child["href"]
        child.name = "code"
        del child.attrs["href"]        

# Rename anchors using heading text

def camel(s):
    return "".join(p.title() for p in s.split("_"))

def snake(s):
    return "_".join(p.lower() for p in s.split(" "))

anchor_replacements = {
    "[\d.]+ (.*)": r"\1",
    "(.*) \(.*\)": r"\1",
    "^([A-Z_]+)$": lambda m: camel(m.group(1)),
}
            
            
# Speed up id:heading text mapping
anchors = {h["id"]: h.text.strip() for h in soup.find_all(re.compile("h\d")) if "id" in h.attrs}

missing_anchors = {
    "OPEN_CATALOG_FILE_ACK" : "OpenCatalogFileAck",
    "OPEN_CATALOG_FILE" : "OpenCatalogFileAck",
}

for a in soup.find_all("a"):
    if "href" in a.attrs:
        if a["href"].startswith("#"):
            href = a["href"].lstrip("#")
            
            heading_text = anchors.get(href)
            
            if not heading_text:
                anchor_fix = missing_anchors.get(href)
                if anchor_fix:
                    a["href"] = "#%s" % anchor_fix
                    print(a)
                else:
                    a.unwrap()
                continue
            
            new_name = heading_text
            for s, r in anchor_replacements.items():
                new_name = re.sub(s, r, new_name)
            new_name = new_name.lower().replace(" ", "-")
            a["href"] = "#%s" % new_name
                    
        elif "1mD9cZri8S25hm6VTPehEXUXA_kDptlcr41ktbEZQv1k" in a["href"]:
            # fix links to catalog doc which are supposed to be anchors
            a["href"] = "#%s" % a.text
            
        else:
            m = re.match("https://www\.google\.com/url\?q=(.*)&sa=.&ust=.*&usg=.*", a["href"])
            if m:
                # Fix Google redirects
                a["href"] = m.group(1)
    
    # strip nested coce formatting from links (this is a rst limitation)
    if a.contents and a.contents[0].name == "code":
        a.contents[0].unwrap()

# Strip out the manual protobuf tables

tables = soup.find_all("table")
for table in tables:
    table.extract()

# Remove manual section numbering, fix broken heading levels and hack in IDs
for heading in soup.find_all(re.compile("h\d")):
    if heading.text == "CARTA Interface Control Document":
        del heading.attrs["id"]
        continue
    
    heading["id"] = re.sub("[\d.]+ (.*)", r"\1", heading.text).strip()
    
    if re.match("4\.\d+ ", heading.text):
        heading.name = "h2"
    elif re.match("4\.\d+\.\d+ ", heading.text):
        heading.name = "h3"
    elif heading.name == "h5":
        heading.name = "h4"
    elif heading.name == "h6":
        heading.name = "h5"
    
    if not heading.string:
        heading.extract()
    else:
        heading.string.replace_with(re.sub("[\d.]+ ", "", heading.text))
            
# For preview purposes, style the coloured spans
for s in soup.find_all("span"):
    if "role" in s.attrs:
        s["class"] = s["role"]

# Rename images

seen = set()

for img in soup.find_all("img"):
    src = img["src"]
    plantuml = subprocess.run(["plantuml", "-metadata", src], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = plantuml.stdout.decode('ascii')
    m = re.search("title (.*)", result)
    if m:
        new_name = m.group(1).strip()
        new_name = re.sub("[()]", "", new_name)
        new_name = new_name.replace(r"\n", " ")
        new_name = re.sub(",.*", "", new_name)
        new_name = re.sub("-", "_", new_name)
        new_name = "_".join(new_name.lower().split())
        if new_name in seen:
            new_name += "_2" # we only need this for one image
        seen.add(new_name)
        subprocess.run(["cp", src, "../images/%s.png" % new_name ])
        img["src"] = "images/%s.png" % new_name
    else:
        print("No metadata for image", src)
                
with open(sys.argv[2], 'w') as f:
    print(str(soup), file=f)

