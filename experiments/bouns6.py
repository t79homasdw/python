contents = ["All carrots",
            "The carrots were sliced.",
            "Apples are good."]

filenames = ["doc.txt", "doc2.txt", "doc3.txt"]

for content, filename in zip(contents, filenames):
    file = open(filename, 'w')
    file.write(content)
    file.close()