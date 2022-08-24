import os, glob
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

''' 
    # PackageLoader not working; not sure how to import 'blog' (the name of this app/project folder) as a module. Tried below:
    path.join(path.dirname(__file__), 'templates'),
    loader=PackageLoader('blog', 'templates'),
'''

env = Environment(loader=FileSystemLoader("templates/"))

#  List of dicts, each a component of a template
def pages(): 
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
    return pages

# TODO
# 2. open content in page_builder() and populate within pages
# 3. restructure notes file so the posts are a list of dicts 


# cycle through the pages list to build the output files                         
def page_builder(pages=pages()): 
    for page in pages:
        template = env.get_template(f"{page['template']}.html") # get_template() accesses child templates from /templates 
        context = template.render(page, pages=pages) # render() takes in a dict or string
                                    
        if page['template'] == 'index':          # prepare the output files in docs_filename variables                              
            docs_filename = "./docs/index.html"
        else: 
            docs_filename = f"./docs/{page['template']}.html"    

        # here's the output logic  
        with open(docs_filename, mode="w", encoding="utf-8") as output:
            output.write(context)
        # print(f"... wrote {filename}")

# print(navbar)                                
print("files created; utils works")
