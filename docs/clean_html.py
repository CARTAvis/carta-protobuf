import re
from collections import defaultdict
from bs4 import BeautifulSoup

with open("CARTABackendFrontendInterfaceControlDocument.html") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

css_entries = re.findall(r"([^{]+)\{(.*?)\}", soup.style.text)
css_entries[:10]

c_classes = [(k, v) for (k, v) in css_entries if re.match("\.c\d+", k)]

mapping_search = {
    "strong": "font-weight:700",
    "code": "Courier New",
    "em": "font-style:italic",
    "orange": "#ff9900",
    "blue": "#0b5394",
    "red": "#741b47",
}

mapping = defaultdict(list)

for k, v in c_classes:
    for new, old in mapping_search.items():
        if old in v:
            mapping[k.replace('.', '')].append(new)

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
        for k, v in mapping.items():
            if k in tag["class"]:
                for newclass in v:
                    if newclass in ("blue", "red", "orange"):
                        new_span = soup.new_tag("span")
                        new_span["class"] = [newclass]
                        tag.wrap(new_span)
                    else:
                        tag.wrap(soup.new_tag(newclass))
                
    tag.unwrap()

for tag in soup.find_all("img"):
    tag.attrs = {"src": tag["src"]}

for tag in soup.find_all("p"):
    if not tag.contents or (not tag.get_text().strip() and not tag.find_all("img")):
        tag.extract()

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

for i in range(4):
    nest(second[i], second[i].find_next("p"))
    second[i].p.unwrap()

merge(second[0], second[1])
merge(second[0], second[2])
merge(second[0], second[3])

for e in soup.find_all():
    e.smooth()

for t in soup.find_all(None, text=re.compile(".+")):
    t.replace_with(t.replace('\xa0', ' '))

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
        s.extract()
        parts = re.split("( )", s)
        for p in parts:
            if caps_text.match(p):
                c = soup.new_tag("code")
                c.append(p)
                parent.append(c)
            else:
                parent.append(p)

# TODO TODO TODO

# TABLE FIXES
# * Strip paragraphs from cells

# Normalize order of code and colour tags

# Split into sections
# Rename the section anchors / links
# Rename the images

print(str(soup))

