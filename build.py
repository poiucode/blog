from files import (files)
import fnmatch


def main():
    # Loops through page dictionary from files object and based on concatenated strings, accesses the file
    # Site based on a template built from 3 parts in Blueprints (head,nav,and footer) folder 
    # With the actual page content pulled from Content folder. 
    # Notes.md doesn't work yet since it's markdown and github pages doesn't have. This will be enabled with Jinja
        
    # loop through pages in pages dictionary
    for page in files.pages:
        
        # Store each page as it's built
        temp = '' 

        # build the page from the templates
        for template in files.blueprints: 
            if fnmatch.filter(template, '3*'):
                temp += open(files.input + page['filename']).read() 
            else: 
                temp += open(template).read() 
            
            # replace <title>
            temp = temp.replace('{{title}}', page['title'])
            # write the page to content folder
            open(files.output + page['filename'], 'w').write(temp)

    
main()

'''
    # This is the original code so you see how each page is actually built 
    index = open("./blueprints/head.html").read()
    index += open("./blueprints/nav.html").read()
    index += open("./content/index.html").read()
    index += open("./blueprints/footer.html").read()
    open("./docs/index.html", "w").write(index)

    blog = open("./blueprints/head.html").read()
    blog += open("./blueprints/nav.html").read()
    blog += open("./content/notes.md").read()
    blog += open("./blueprints/footer.html").read()
    open("./docs/blog.md", "w").write(blog)

    contact = open("./blueprints/head.html").read()
    contact += open("./blueprints/nav.html").read()
    contact += open("./content/contact.html").read()
    contact += open("./blueprints/footer.html").read()
    open("./docs/contact.html", "w").write(contact)
 '''