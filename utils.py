import os
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

''' 
    # PackageLoader not working; not sure how to import 'blog' (the name of this app/project folder) as a module. Tried below:
    path.join(path.dirname(__file__), 'templates'),
    loader=PackageLoader('blog', 'templates'),
'''

env = Environment(loader=FileSystemLoader("templates/"))

''' 
    # FileSystemLoader test: passes
    t = env.from_string("Hello, {{ name }}!")
    print(t.render(name="World"))
'''


#  a list of dicts with each being components of a template
pages = [
    {
        'template'  : 'index',
        'title': 'Home',
        'heading': 'Say hello to my little blog!',
        'content': "Welcome to a small templated blog",
    },
    {
        'template'  : 'blog',
        'title': 'Blog',
        'heading': 'Blog',
        'content': "", # pull as list of items from separate file    
    },
    {
        'template'  : 'contact',
        'title': 'Contact',
        'heading': 'Say hello!',
        'content': "Submit a pr and I'll get back to you",    
    },
]

                            
for page in pages:
    # consider assigning each template from the context
    template = env.get_template(f"{page['template']}.html")
    context = template.render(
        page        
    )
    if page['template'] == 'index':
        docs_filename = "./docs/index.html"
    else: 
        docs_filename = f"./docs/{page['template']}.html"    
                                
    # have filename be the outputted file in docs folder   
    with open(docs_filename, mode="w", encoding="utf-8") as message:
        message.write(context)
    # print(f"... wrote {filename}")
