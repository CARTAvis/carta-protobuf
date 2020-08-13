from sphinx.roles import XRefRole

def carta_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    normalized = text.lower().replace("_", "")
    text = f"{text} <{normalized}>"
    xref = XRefRole()
    return xref('std:ref', rawtext, text, lineno, inliner, options, content)

def setup(app):
    app.add_role('carta', carta_role)
