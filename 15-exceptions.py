def main():
    try:
        for line in readfile("lines.txt"): print(line.strip())
    except IOError as e:
        print ("cannot read file")
    except ValueError as e:
        print ("bad filename", e)

def readfile(filename):
    if filename.endswith(".txt"):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError("Filenames must end with .txt")

if __name__ == "__main__": main()
