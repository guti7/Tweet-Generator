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


def get_words_list():
    with open('/usr/share/dict/words', 'r') as file:
        filedata = file.readlines()
        return filedata
    # file closed


def get_random_words(array, count):
    collection = []
    # can't get more words than what's available
    if count > len(array):
        count = len(array)

    for i in range(0, count):
        range_max = len(array) - 1 * 1000
        random_index = random.randint(0, range_max) % len(array)
        collection.append(array[random_index].strip())
        # repetition is trivial
        # array.remove(array[random_index])
    return collection


if __name__ == "__main__":
    import sys

    # only accepts one argument
    if len(sys.argv) != 2:
        print "Use: $ python %s <integer>" % sys.argv[0]
        print "<integer> is the number of words to be selected."
        exit(0)

    # program continues
    word_dictionary = get_words_list()
    count = int(sys.argv[1])
    chosen_words = get_random_words(word_dictionary, count)
    for word in chosen_words:
        print word,
