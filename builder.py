from files import (files)
import fnmatch

def builder(self, files):
    # loop through blueprint dir and build page 
        # loop through pages[] and insert correct pagechdir into input directory
    
    # this is going to hold each page as it's built
    temp = '' 
    for page in files.pages:
        # build the page
        for template in files.blueprints:
            if fnmatch.filter(template, '1*'):
                temp += open(files.input + page['filename']).read() 
                temp.replace('{{title}}', page['title'])
            # Plug in the content
            if template == '3_None':
                temp += open(files.input + page['filename']).read() 
            temp += open(template).read() 
            # write the page to content folder
            open(files.output + page['filename'], 'w').write(temp)
            