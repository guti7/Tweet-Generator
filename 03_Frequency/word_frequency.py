# Analyze Word Frequency in Text by creating a histogram.
# Given a source body of text, can you perform the following?:
# What is the least/most frequent word(s)?
# How many different words are used?
# What is the average(mean/median/mode) frequency of words in the text?

import timeit
import string

start_time = timeit.default_timer()


# Reads from file one line at a time and returns a list of lines.
def get_lines_list(filename):
    with open(filename, 'r') as file:
        filein_lines_list = file.readlines()
        return filein_lines_list
    # file close


# Reads from a list of lines and returns a list of individual words.
def get_words_list(lines_list):
    words_list = parse_words(lines_list)
    return words_list


# Takes a list of lines as an argument and returns a list of words.
# It cleans up a word by removing whitespace and punctuation.
def parse_words(input_list):
    words_list = []
    for line in input_list:
        clean_line = line.translate(None, string.punctuation)
        words_list.extend(clean_line.strip().split(' '))
    return words_list


# Takes a list of words and returns a histogram
# as a dict type of word frequencies.
def histogram(words_list):
    dictionary = dict()
    for word in words_list:
        lowercase_word = word.lower()
        if lowercase_word == '':
            continue
        if lowercase_word not in dictionary:
            dictionary[lowercase_word] = 1
        else:
            dictionary[lowercase_word] += 1
    return dictionary


# Returns the count of unique words of the given histogram.
def unique_words(histogram):
    return len(histogram)


# Takes a word and histogram and returns the total count for such word.
def frequency(word, histogram):
    return histogram[word] if word in histogram else 0
    # histogram.get(word, 0)


# Print the histogram in alphabetical order
def print_histogram_alphabetized(histogram):
    sorted_listogram = sorted(histogram.items())
    print_histogram(sorted_listogram)


# Print the histogram in descending frequency order:
def print_descending_frequency(histogram):
    # order only by count - not by count then word
    frequency_listogram = sorted(histogram.iteritems(), key= lambda (word, count): (count), reverse = True)
    print_histogram(frequency_listogram)


# Print histogram in table format.
# Listogram is an ordered list version of the histogram
def print_histogram(listogram):
    for word, count in listogram:
        print '%-15s : %5s' % (word, count)

# main
if __name__ == "__main__":
    import sys

    # program use message to user
    if len(sys.argv) != 2:
        print "Use: $ python %s <filename>" % sys.argv[0]
        exit(0)

    # continue execution
    filename = sys.argv[1]

    lines_list = get_lines_list(filename)
    words_list = get_words_list(lines_list)
    histo = histogram(words_list)

    print 'Analysis: ', filename
    # print 'histogram:'
    # print histo

    print 'yellow: %d' % frequency('yellow', histo)
    print 'fish: %d' % frequency('fish', histo)
    print 'Unique words: ', unique_words(histo)

    elapsed = timeit.default_timer() - start_time
    print "Elapsed Time: ", elapsed

    print 'Alphabetical:'
    # print_histogram_alphabetized(histo)
    print '--------------'
    print 'Descending Frequency:'
    print_descending_frequency(histo)
