from docutils.parsers.rst.directives.misc import Class
from sphinx.domains import Domain
from sphinx.roles import XRefRole
from sphinx.util.docutils import SphinxDirective

class CartaClass(Class, SphinxDirective):
    """This wraps the docutils directive for adding a CSS class to a block,
    also associating that class with the given symbol name."""
    required_arguments = 2
    
    def run(self):
        cssclass, symbol = self.arguments
        carta = self.env.get_domain('carta')
        carta.add_class(symbol, cssclass)
        
        return super().run()

class CartaXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        """Strip underscores from the reference target and lowercase it,
        so that MSG_NAME is automatically redirected to MsgName"""
        target = target.lower().replace("_", "")
        refnode['refexplicit'] = True
        return title, target

class CartaDomain(Domain):
    name = 'carta'
    label = 'CARTA'
    
    roles = {
        'ref': CartaXRefRole(), # For references without a colour
        'refc': CartaXRefRole(), # For references with a colour
    }
    
    initial_data = {
        'classes': {},
    }
    
    directives = {
        'class': CartaClass,
    }
    
    def add_class(self, symbol, cssclass):
        self.data['classes'][symbol] = cssclass
    
    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        """Delegate the actual reference resolution to :std:ref:, and modify
        the resolved node to add custom css classes."""
        domain = env.get_domain('std')
        resolved = domain.resolve_xref(env, fromdocname, builder, 'ref', target, node, contnode)
        if resolved:
            resolved.children[0]["classes"] = ["carta", "carta-ref"]
            if typ == "refc":
                # Colour the reference
                cssclass = self.data['classes'].get(target)
                if cssclass:
                    resolved.children[0]["classes"].append(cssclass)
                else:
                    logger.warning(__('could not find css class for CARTA symbol %r.'), target)
        else:
            pass # This delegates to :std:ref:, which should print its own warning
        return resolved
    
def setup(app):
    app.add_domain(CartaDomain)
