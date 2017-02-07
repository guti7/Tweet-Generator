from flask import Flask
app = Flask(__name__)

from sampling import *

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word')
def get_word():
    words_list = get_words_list('siddh10.txt')
    histo = histogram(words_list)
    complete =  get_complete_list(histo)
    word = get_random_word(complete)
    return word


if __name__ == '__name__':
    app.run()
