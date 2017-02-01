# Analyze Word Frequency in Text
# Create a histogram
# Given a source body of text, we perform the following:
# What is the least/most frequent word(s)?
# How many different words are used?
# What is the average(mean/median/mode) frequency of words in the text?


def get_words_list():
    with open('siddh10.txt', 'r') as file:
        document_file = file.readlines()
        words_list = parse_sentences(document_file)
        return words_list
    # file close


def parse_sentences(text_file):
    words_list = []
    for line in text_file:
        words_list.extend(line.strip().split(' '))
    return words_list


# Takes a text source as a list and returns a histogram of word frequency.
def histogram(source_text):
    words_dictionary = set(source_text)
    return {word: source_text.count(word) for word in words_dictionary}


# Takes a histogram argument and returns the count of unique words.
def unique_words(histogram):
    return len(histogram)  # total count of unique words


# Takes a word and histogram and returns the total count for such word.
def frequency(word, histogram):
    return histogram[word] if word in histogram else 0


if __name__ == "__main__":
    import sys

    words_list = get_words_list()
    histo = histogram(words_list)
    print frequency('yellow', histo)
    print frequency('fish', histo)
    print unique_words(histo)
