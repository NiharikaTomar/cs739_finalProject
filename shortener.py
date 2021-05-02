from flask import Flask, render_template, request, redirect, url_for, g
import random
import string
from db import DB


secret = 'admin:password'  # this is dummy secret, replace it with actual credentials
db_url = 'http://{}@localhost:5984/'.format(secret)
db_name = 'key_value_store'
shortener = Flask(__name__)


@shortener.before_first_request
def get_db():
    if 'db' not in g:
        g.db = DB(db_url, db_name)

    return g.db


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=7)
        rand_letters = "".join(rand_letters)
        short_url = get_db().find(short_url=rand_letters)
        if not short_url:
            return rand_letters


@shortener.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        long_url = request.form["url_form"]
        short_url = shorten_url()
        doc = {'short_url': short_url, 'long_url': long_url}
        get_db().save(doc)
        return render_template('shorturl.html', short_url_display=short_url)
    else:
        return render_template('home.html')


@shortener.route('/<short_url>')
def redirection(short_url):
    long_url = get_db().find(short_url=short_url)
    print(long_url)
    if long_url:
        return redirect(long_url)
    else:
        return f'<h1>ERROR: url doesnt exist</h1>'


@shortener.route('/display/<url>')
def display_short_url(url):
    return render_template('shorturl.html', short_url_display=url)


if __name__ == '__main__':
    shortener.run(host='0.0.0.0', port=5000, debug=True)
