filename="writefilepy.tx";

def writeFile(filename):
    with open(filename, "w") as f:
        f.write("Hello world!")
        f.write("This is another line!")

        f.close()

writeFile(filename);
