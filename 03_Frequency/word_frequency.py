# Analyze Word Frequency in Text
# Create a histogram
# Given a source body of text, we perform the following:
# What is the least/most frequent word(s)?
# How many different words are used?
# What is the average(mean/median/mode) frequency of words in the text?
import timeit
import string

start_time = timeit.default_timer()

def get_words_list(filename):
    with open(filename, 'r') as file:
        filein_list = file.readlines()
        words_list = parse_words(filein_list)
        return words_list
    # file close

# parse_file -> parse_lines -> parse_words

# Takes a list of lines as arguments and returns a list of words.
# It cleans up a word by removing whitespace and punctuation.
def parse_words(input_list):

    words_list = []
    for line in input_list:
        # returns list with words
        clean_line = line.translate(None, string.punctuation)
        words_list.extend(clean_line.strip().split(' '))
    return words_list


# Takes a text source as a list and returns a histogram of word frequencies.
def histogram(source_text):
    # words_dictionary = set(source_text)
    # # Does count function traverse the list each time?
    # return {word: source_text.count(word) for word in words_dictionary}

    # implementation two: a lot fastaer.
    dictionary = dict()
    for word in source_text:
        lowercase_word = word.lower()
        if lowercase_word == '':
            continue
        if lowercase_word not in dictionary:
            dictionary[lowercase_word] = 1
        else:
            dictionary[lowercase_word] += 1
    return dictionary


# Takes a histogram argument and returns the count of unique words.
def unique_words(histogram):
    return len(histogram)


# Takes a word and histogram and returns the total count for such word.
def frequency(word, histogram):
    return histogram[word] if word in histogram else 0
    # histogram.get(word, 0)

def print_histogram_alphabetized(histogram):
    # keys = histogram.keys()
    # keys.sort()
    # for key in keys:
    #     print '%-15s : %5s' % (key, histogram[key])

    for key in sorted(histogram):
        print '%-15s : %5s' % (key, histogram[key])

def print_descending_frequency(histogram):
    for key, value in sorted(histogram.iteritems(), key=lambda (k, v): (v, k), reverse = True):
        print '%-15s : %5s' % (key, value)

# main
if __name__ == "__main__":
    import sys

    # program use message to user
    if len(sys.argv) != 2:
        print "Use: $ python %s <filename>" % sys.argv[0]
        exit(0)

    # continue execution
    filename = sys.argv[1]

    words_list = get_words_list(filename)
    histo = histogram(words_list)
    print 'Analysis: ', filename

    print 'yellow: %d' % frequency('yellow', histo)
    print 'fish: %d' % frequency('fish', histo)
    print 'Unique words: ', unique_words(histo)

    elapsed = timeit.default_timer() - start_time
    print "Elapsed Time: ", elapsed

    print_histogram_alphabetized(histo)
    print '--------------'
    print_descending_frequency(histo)
