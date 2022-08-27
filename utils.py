import os, glob
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

''' 
    # PackageLoader not working; not sure how to import 'blog' (the name of this app/project folder) as a module. Tried below:
    path.join(path.dirname(__file__), 'templates'),
    loader=PackageLoader('blog', 'templates'),
'''

env = Environment(loader=FileSystemLoader("templates/"))

def index_check(tag):
    if tag == 'index':
        return 'Home'
    else: 
        return tag

def read_file(item):
    f = open(item).read()
    return f
    
def get_content():
    pages = []
    folder = glob.glob('./content/*')
    for path in folder:
        file_name = os.path.basename(path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            'template': name_only,
            'title': index_check(name_only).capitalize(),
            'url': file_name,
            'heading': index_check(name_only).capitalize(),
            'content': read_file(path)  # open file and write to variable
         })
    return pages
    
# cycle through the pages list to build the output files                         
def page_builder(pages=get_content()): 
    for page in pages:
        template = env.get_template(f"{page['template']}.html") # get_template() accesses child templates from /templates 
        context = template.render(page, pages=pages) # render() takes in a dict or string
                                     
        docs_filename = f"./docs/{page['template']}.html"    

        # here's the output logic  
        with open(docs_filename, mode="w", encoding="utf-8") as output:
            output.write(context)