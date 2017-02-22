from flask import Flask
app = Flask(__name__)

from sampling import *

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word')
def get_word():
    lines_list = get_lines_list('sidd_clean.txt')
    words_list = get_words_list(lines_list)
    histo = histogram(words_list)
    word = get_random_word_weigthed(histo)
    return word

@app.route('/sentence')
def get_sentence():
    lines_list = get_lines_list('sidd_clean.txt')
    words_list = get_words_list(lines_list)
    histo = histogram(words_list)

    sentence = ''
    for _ in range(15):
        word = get_random_word_weigthed(histo)
        sentence += word + ' '
    return sentence


if __name__ == '__main__':
    # needs a file name
    if len(sys.argv) != 2:
        print "Use: $ python %s <filename>" % sys.argv[0]
        exit(0)
