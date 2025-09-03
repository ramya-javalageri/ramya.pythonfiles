with open('mindmap.png','rb') as file:
    data=file.read()
with open('image.jpg','wb') as file1:
    file1.write(data)