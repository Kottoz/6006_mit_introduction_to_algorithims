# @author Kotoz
# @email mohamed.t.elshetry@mail.com
# @create date 2020-04-17 01:40:37
# @modify date 2020-04-17 01:40:37  

# @desc This program computes the "distance" between two text files
# as the angle between their word frequency vectors (in radians).

#   For each input file, a word-frequency vector is computed as follows:
#    (1) the specified file is read in
#    (2) it is converted into a list of alphanumeric "words"
#        Here a "word" is a sequence of consecutive alphanumeric
#        characters.  Non-alphanumeric characters are treated as blanks.
#        Case is not significant.
#    (3) for each word, its frequency of occurrence is determined
#    (4) the word/frequency lists are sorted into order alphabetically
#
# The "distance" between two vectors is the angle between them.
# If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i)
# and y = (y1, y2, ..., yn) is the second vector,
# then the angle between them is defined as:
#    d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where:
#    inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norm(x) = sqrt(inner_product(x,x))
import sys
####################################################################
# the specified file is read in
####################################################################
def read_file(file_name):
    try:
        f = open(file_name, 'r')
        return f.readlines()
    except IOError:
        print("Error opening")
        sys.exit()
# lst = read_file("lec02_code/file1.txt")
####################################################################
# is converted into a list of alphanumeric "words"
####################################################################
def get_words_in_lines(lines):
    for line in lines:
        




