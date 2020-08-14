from sphinx.domains import Domain
from sphinx.roles import XRefRole


class CartaXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        target = target.lower().replace("_", "")
        refnode['refexplicit'] = True
        return title, target

class CartaDomain(Domain):
    name = 'carta'
    label = 'CARTA'
    roles = {
        'ref': CartaXRefRole(),
        'f2b': CartaXRefRole(),
        'b2f': CartaXRefRole(),
        'sub': CartaXRefRole(),
    }
    
    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        domain = env.get_domain('std')
        resolved = domain.resolve_xref(env, fromdocname, builder, 'ref', target, node, contnode)
        if resolved:
            resolved.children[0]["classes"] = ["carta", f"carta-{typ}"]
        return resolved
    
def setup(app):
    app.add_domain(CartaDomain)
