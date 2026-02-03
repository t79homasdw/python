import glob

myfiles = glob.glob("*.txt")
print("Files found:")
for filepath in myfiles:
    print("filename: " + filepath + "\n")
    with open(filepath, "r") as file:
        print(file.read() + "\n")
print(myfiles)