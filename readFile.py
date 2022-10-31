filename="writefilepy.tx";

def writeFile(filename):
        with open(filename, "r") as f:
            for line in f:
                if(line):
                    print(line)

            f.close()

writeFile(filename);
