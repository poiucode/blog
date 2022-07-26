# Create variables for each page 
# Write those to new files in docs

def main():
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
    
    
main()

