#!/usr/bin/env python3

import re
import sys
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
    "orange": "#ff9900",
    "blue": "#0b5394",
    "red": "#741b47",
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
.orange { color: #ff9900 }
.blue { color: #0b5394 } 
.red { color: #741b47 }
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
for tag_name in ("body", "a", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "table", "thead", "tbody", "tr", "td", "th", "ul", "ol", "li"):
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

# Strip paragraphs and no-op rowspans and colspans from table cells
for td in soup.find_all("td"):
    for child in td.contents:
        if child.name == 'p':
            child.unwrap()
    
    for span in ("rowspan", "colspan"):
        if td.attrs.get(span) == "1":
            del td.attrs[span]

# add colour span parent to <code> or <a> if it is surrounded by the same colour siblings

def colour_of(t):
    if hasattr(t, "attrs") and "role" in t.attrs:
        has_colour = {"red", "blue", "orange"}.intersection(t["role"]) or None
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

# then merge adjacent colour spans
cells = soup.find_all("td")
for cell in cells:
    children = cell.contents
    if len(children) > 1 and all(c.name == "span" for c in children) and len(set(c["role"][0] for c in children)) == 1:
        for c in children[1:]:
            children[0].extend(c.contents)
            c.extract()

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

# Colspans and rowspans are not supported
# We can have either multiline or no manual indentation; I'm picking no manual indentation

tables = soup.find_all("table")
for table in tables:
    pos = table.parent.index(table)
    desc_head, desc, field_head, field_names, *fields = table.tbody.contents
        
    table.parent.insert(pos, desc_head.td.h5.extract())
    desc_head.extract()
    
    new_desc_head = soup.new_tag("h6")
    new_desc_head.append("Description")
    
    table.parent.insert(pos + 1, new_desc_head)
        
    new_desc = soup.new_tag("p")
    
    for child in list(desc.find_all("td")[1].contents):
        new_desc.append(child)
    
    table.parent.insert(pos + 2, new_desc)
    
    desc.extract()
    
    new_field_head = soup.new_tag("h6")
    new_field_head.append(field_head.text.strip(" :"))
    
    table.parent.insert(pos + 3, new_field_head)
    
    field_head.extract()
    
    for td in field_names.find_all("td"):
        td.name = "th"

# links outside code

for c in soup.find_all("code"):
    child = c.contents[0]
    if child.name == "a":
        c.name = "a"
        c["href"] = child["href"]
        child.name = "code"
        del child.attrs["href"]        

# Rename anchors using heading text

anchors = {}

def camel(s):
    return "".join(p.title() for p in s.split("_"))

def snake(s):
    return "_".join(p.lower() for p in s.split(" "))

anchor_replacements = {
    "[\d.]+ (.*)": r"\1",
    "(.*) \(.*\)": r"\1",
    "^([A-Z_]+)$": lambda m: camel(m.group(1)),
    "^((?:[A-Z][a-z]+){2,})$": r"CARTA.\1",
}

anchor_exceptions = {
    "Coosys": "CARTA.Coosys",
    "Moment (Enum)": "CARTA.Moment",
}

headings = soup.find_all(re.compile("h\d"))

for heading in headings:
    if "id" in heading.attrs:
        old_name, new_name = heading["id"], heading.text.strip()
        if new_name in anchor_exceptions:
            new_name = anchor_exceptions[new_name]
        else:
            for s, r in anchor_replacements.items():
                new_name = re.sub(s, r, new_name)
        anchors[old_name] = new_name
        
for heading in headings:
    if "id" in heading.attrs:
        hid = heading["id"]
        if hid in anchors:
            if not anchors[hid]:
                heading.extract()
                continue
            heading["id"] = anchors[hid]

missing_anchors = {
    "OPEN_CATALOG_FILE_ACK" : "CARTA.OpenCatalogFileAck",
    "OPEN_CATALOG_FILE" : "CARTA.OpenCatalogFileAck",
}

for a in soup.find_all("a"):
    if "href" in a.attrs:
        if a["href"].startswith("#"):
            href = a["href"].lstrip("#")
            if href in anchors:
                a["href"] = anchors[href]
            else:
                anchor_fix = missing_anchors.get(href)
                if anchor_fix:
                    a["href"] = anchor_fix
                else:
                    a.unwrap()
                    
        elif "1mD9cZri8S25hm6VTPehEXUXA_kDptlcr41ktbEZQv1k" in a["href"]:
            # fix links to catalog doc which are supposed to be anchors
            a["href"] = "#CARTA.%s" % a.text
            
# For preview purposes, style the coloured spans
for s in soup.find_all("span"):
    if "role" in s.attrs:
        s["class"] = s["role"]
                
with open(sys.argv[2], 'w') as f:
    print(str(soup), file=f)

# TODO rename images
# TODO fix missing links and links to catalog document
