from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

shortener = Flask(__name__)
shortener.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
shortener.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(shortener)

@shortener.before_first_request
def create_tables():
    db.create_all()

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=7)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@shortener.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["url_form"]
        found_url = Urls.query.filter_by(long=url_received).first()

        if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
            # return f"{found_url.short}
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
            # return short_url
    else:
        return render_template('home.html')

@shortener.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>ERROR: url doesnt exist</h1>'

@shortener.route('/display/<url>')
def display_short_url(url):
    return render_template('shorturl.html', short_url_display=url)


if __name__ == '__main__':
    shortener.run(host='0.0.0.0', port=5000, debug=True)