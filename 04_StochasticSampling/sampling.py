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

def probability_distribution(histogram):
    words_probability_distr = {}
    word_count = sum(histogram.values())
    for word, count in histogram.iteritems():
        words_probability_distr[word] = float(count)/word_count
    return words_probability_distr


def get_random_word(histogram):
    # range_max = len(histogram) - 1
    # random_index = random.randint(0, range_max)
    # # better than histogram.keys() ? returns list of keys(words)
    # list_histogram = histogram.items()
    # word_tuple = list_histogram[random_index]
    # word = word_tuple[0]
    word = random.choice([k for k in histogram for _ in range(histogram[k])])
    return word


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
    words_dictionary = set(source_text)
    return {word: source_text.count(word) for word in words_dictionary}

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
    print get_random_word(histogram)
    print histogram
    probabilities = probability_distribution(histogram)
    for k, v in probabilities.iteritems():
        print "%-4s => %5.3f" % (k, v) # '{} {}'.format(k, v)
