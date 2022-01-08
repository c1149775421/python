with open('a.txt','at') as at:
    at.write("写入内容\n")
with open('a.txt','rt') as re:
    text=re.read()
print(text)
input()
