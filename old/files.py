# Deprecated
# The idea behind this page was to build a files object which would build each page by appending a few "templates" to each other
# ... but these templates were actually just html snippets so this was all basically just a complicated way of concatenating files
# This was done before working with jinja. 
# In the end, I realized there's no need to do this because I could put the entire html in the base.html file then change up certain 
# sections (e.g. nav/footer) using child templates

import glob, json, os

class Files:
    def __init__(self):
        self.templates = glob.glob('./templates/*')
        self.content = glob.glob('./content/*')
        self.template_order = ['head', 'nav', 'content', 'footer']     # The order of templates used to build pages
        self.page_dict = {}
        self.pages = []
        
    def build_content(self):
        for template_name in self.template_order:
            page_content = ''
            # find the filename based on the keyword in the self.content list. 
            if template_name == 'content':
                file_name = ''.join(list(filter(lambda a: template_name in a, self.content)))
                page_content += open(file_name).read()
            else: 
                file_name = ''.join(list(filter(lambda a: template_name in a, self.templates)))
                page_content += open(file_name).read()
        
            name_only, ext = os.path.splitext(os.path.basename(file_name))
            self.pages.append({
                'filename'  : file_name,
                'title'     : name_only,
                'content'   : page_content
            })
            
            # output results into a textfile to see if working
        with open('output.txt', 'w+') as fout:
            json.dump(self.pages, fout)
                
        return self.pages
            
'''            
            file_path = template
            file_name = os.path.basename(file_path)
            print(file_name)
            name_only, extension = os.path.splitext(file_name)
            print(name_only)
'''            
            
               
        
        
'''
class Files:
    def __init__(self):
        self.input = './content/'   # use import os to change into directory
        self.output = './docs/'     # use import os to change into directory
        self.blueprints = glob.glob('./blueprints/*')
        self.content    = glob.glob('./content/*')
        self.blueprints.sort()
        self.pages = [
            {
                'filename'  : "index.html",
                'title'     : 'Home',

            },
            {
                'filename'  : "notes.md",
                'title'     : 'Blog'
            },
            {   
                'filename': "contact.html",
                'title'   : 'Contact'
            },
        ]
'''

files = Files()

files.build_content()
