import sys
def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()

path = "file1.txt"
lis = read_file(path)
print(lis[-1][5], len(lis))