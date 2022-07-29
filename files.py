import glob

class Files:
    def __init__(self):
        self.input = './content/'   # use import os to change into directory
        self.output = './docs/'     # use import os to change into directory
        self.blueprints = glob.glob('./blueprints/*')
        self.blueprints.sort()
        self.pages = [
            {
                'filename'  : "index.html",
                'title'     : 'Home',

            },
            {
                'filename'  : "notes.md",
                'title'     : 'Blog'
                # consider a markdown function that takes a list of markdown elements and swaps with html elements via replace()
            },
            {   
                'filename': "contact.html",
                'title'   : 'Contact'
            },
        ]

files = Files()