from files import (files)
import fnmatch


def main():
    # loop through blueprint dir and build page 
        # loop through pages[] and insert correct pagechdir into input directory
    
    # this is going to hold each page as it's built
    temp = '' 
    for page in files.pages:
        # build the page from the templates
        for template in files.blueprints:
            if fnmatch.filter(template, '1*'):
                temp += open(files.input + page['filename']).read() 
                # print(temp)
                temp.replace('{{title}}', page['title'])
            # Plug in the content
            if template == '3_None':
                temp += open(files.input + page['filename']).read() 
            temp += open(template).read() 
            # write the page to content folder
            open(files.output + page['filename'], 'w').write(temp)
    
    
main()

'''
    # moving original code here to start off 
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