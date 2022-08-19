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
        'url': 'index.html',
        'heading': 'Say hello to my little blog!',
        'content': "Welcome to a small templated blog",
    },
    {
        'template'  : 'blog',
        'title': 'Blog',
        'url': 'blog.html',
        'heading': 'Blog',
        'content': "", # pull as list of items from separate file    
    },
    {
        'template'  : 'contact',
        'title': 'Contact',
        'url': 'contact.html',
        'heading': 'Say hello!',
        'content': "Submit a pr and I'll get back to you",    
    },  
]

# build navbar
navbar = []
for page in pages: 
    navbar.append({
        'link': page['url'],
        'link_title': page['title']
    })
    
# cycle through the pages list to build the output files                         
for page in pages:
    # use get_template(), which accesses /templates, and pulls in the template file using 'template' name within the current dict 
    template = env.get_template(f"{page['template']}.html")
    # render() takes in either a dict or a string. In this case, we pass in the dict and it does the work for us
    context = template.render(page, navbar=navbar)
    # Having just accessed our jinja template, we now prepare the output files in docs_filename variables                              
    if page['template'] == 'index':
        docs_filename = "./docs/index.html"
    else: 
        docs_filename = f"./docs/{page['template']}.html"    
                                
    # here's the output logic  
    with open(docs_filename, mode="w", encoding="utf-8") as output:
        output.write(context)
    # print(f"... wrote {filename}")

                                
print("files created")
