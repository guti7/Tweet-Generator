# Given a histogram representing word frecuency distributions,
# pull words out to produce sentences that approximate English grammar.

# 1st: Build a program that generates "sentences" from the words in
# in the histogram through random selection(stochastic sampling)

# 2nd: Introduce weighted probabilities based on histogram data

# Takes a histogram and returns a single random word
# Note: Do not take distributions into consideration yet.
# Example: $ python sampling.py onefish.txt
#            fish
import random
import sys
import timeit

start_time = timeit.default_timer()

def probability_distribution(histogram):
    words_probability_distr = {}
    word_count = sum(histogram.values())
    for word, count in histogram.iteritems():
        words_probability_distr[word] = float(count)/word_count
    return words_probability_distr


def get_random_word(words_list):
    word = random.choice(words_list)
    return word

def get_complete_list(histogram):
    words = [k for k in histogram for _ in range(histogram[k])]
    return words


# Document arguments
def get_words_list(filename):
    with open(filename, 'r') as file:
        document_file = file.readlines()
        words_list = parse_sentences(document_file)
        return words_list
    # file close


def parse_sentences(text_file):
    words_list = []
    for line in text_file:
        words_list.extend(line.strip().split(' '))
    return words_list


def histogram(source_text):
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

def print_sample(times, words_list):
    sample = {}
    for _ in range(times):
        word = get_random_word(words_list)
        if word in sample:
            sample[word] += 1
        else:
            sample[word] = 1

    for key, value in sample.iteritems():
        print '%-15s : %5s' % (key, value)

# main
if __name__ == '__main__':
    # import sys?

    if len(sys.argv) != 2:
        print "Use: $ python %s <filename>" % sys.argv[0]
        exit(0)

    # program continues
    filename = sys.argv[1]

    words_list = get_words_list(filename)
    histogram = histogram(words_list)
    probabilities = probability_distribution(histogram)
    # for k, v in probabilities.iteritems():
        # print "%-20s => %5.10f" % (k, v) # '{} {}'.format(k, v)

    complete_list = get_complete_list(histogram)
    print_sample(100000, complete_list)

    elapsed = timeit.default_timer() - start_time
    print "Elapsed Time: ", elapsed
