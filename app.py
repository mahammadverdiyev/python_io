with open("test.txt", 'r') as fileObject:
    text = fileObject.read()
    print(f"File: {fileObject.name}")
    print(text)

with open("text_reverse.txt", "w") as fileObject:
    print(f"File: {fileObject.name}")
    text = text[::-1]
    fileObject.write(text)
    print(text)
