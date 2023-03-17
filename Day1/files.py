filename="file.txt"
try:
    with open(filename) as myFile:
        for line in myFile:
            print(line)
except IOError:
    print("file not found")