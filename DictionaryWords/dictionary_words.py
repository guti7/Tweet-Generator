# Generate new sentences using a body of text(corpus) as the source.
# Practice generating "sentences" from a body of text in a text file.

# Read in a text file, select a random set of words from the file, and
# put those words together into a "sentence".
# Ex: $ python dictionary_words.py 2
# print: "<word> <word>"

# Note: Sentences do not have to make grammatical sense.
#       The word order does not matter
#       Word selection can be completely random
#       We use the file located in macOS at /usr/share/dict/words
import random

def get_data():
    with open('workfile.txt', 'r') as file:
        # words = list(file.read().strip())
        filedata = file.readlines()
        print "fildedata:\n %r" % filedata


        print get_random_words(filedata, 1)
    # file closed


def get_random_words(array, count):
    collection = []
    for i in range(0, count):
        random_index = random.randint(0, (len(array) - 1) * 1000) % len(array)
        collection.append(array[random_index].strip())
    return collection


if __name__ == "__main__":
    import sys

    # only accepts one argument
    if len(sys.argv) != 2:
        print "Use: $ python %s <integer>" % sys.argv[0]
        print "<integer> is the number of words to be selected."
        exit(0)

    # program continues
    get_data()
