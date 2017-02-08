# Given a histogram representing word frecuency distributions,
# pull words out to produce sentences that approximate English grammar.

# Part 1: Build a program that generates "sentences" from the words in
# in the histogram through random selection(stochastic sampling)

# Part 2: Introduce weighted probabilities based on histogram data

# Run: Takes a histogram and returns a single random word
# Example: $ python sampling.py onefish.txt
#            fish
import random
import sys
import string
import timeit

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


# Creates a dictionary of words and each probability
# givena histogram of type dict
def probability_distribution(histogram):
    words_probability_distr = {}
    words_count = sum(histogram.values())
    for word, count in histogram.iteritems():
        words_probability_distr[word] = float(count)/words_count
    return words_probability_distr

# Returns a random word given a histogram of type dict
def get_random_word_weigthed(histogram):
    random_int = random.randrange(1, sum(histogram.values()) + 1)
    # random_int = random.randint(1, sum(histogram.values()))
    count = 0
    for word, freq in histogram.iteritems():
        count += freq
        if count >= random_int:
            return word


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


# Test method for weighted random word
def print_sample(times, histogram):
    sample = {}
    for _ in range(times):  # doesn't include the last value
        word = get_random_word_weigthed(histogram)
        if word in sample:
            sample[word] += 1
        else:
            sample[word] = 1

    for word, freq in sample.iteritems():
        print '%-15s : %10d' % (word, freq)


# Test method for weighted selected word)
def print_sample_word(times, histogram, word):
    sample = {word: 0}
    for _ in range(times):  # doesn't include the last value
        current_word = get_random_word_weigthed(histogram)
        if current_word == word:
            sample[word] += 1

    for word, freq in sample.iteritems():
        print '%-15s : %10d' % (word, freq)

# main
if __name__ == '__main__':
    # import sys?

    if len(sys.argv) != 2:
        print "Use: $ python %s <filename>" % sys.argv[0]
        exit(0)

    # program continues
    filename = sys.argv[1]

    lines_list = get_lines_list(filename)
    words_list = get_words_list(lines_list)
    histogram = histogram(words_list)
    print get_random_word_weigthed(histogram)


    # test 'the' in histogram
    # the_frequency = frequency('the', histogram)
    # print "frequency: 'the' = ", the_frequency
    # print "probability: 'the' = ", float(the_frequency) / sum(histogram.values())
    # print_sample_word(100000, histogram, 'the')

    elapsed = timeit.default_timer() - start_time
    print "Elapsed Time: ", elapsed
