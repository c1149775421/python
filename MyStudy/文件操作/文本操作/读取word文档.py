import docx
path = "a.docx"
file = docx.Document(path)

for p in file.paragraphs:
    print(p.text)
input("")
