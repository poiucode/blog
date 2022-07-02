# Create variables for each page 
# Write those to new files in docs

index = open("./templates/head.html").read()
index += open("./templates/nav.html").read()
index += open("./content/index.html").read()
index += open("./templates/footer.html").read()
open("./docs/index.html", "w").write(index)

blog = open("./templates/head.html").read()
blog += open("./templates/nav.html").read()
blog += open("./content/notes.md").read()
blog += open("./templates/footer.html").read()
open("./docs/blog.md", "w").write(blog)

contact = open("./templates/head.html").read()
contact += open("./templates/nav.html").read()
contact += open("./content/contact.html").read()
contact += open("./templates/footer.html").read()
open("./docs/contact.html", "w").write(contact)
