from flask import Flask, url_for
from framelib import frame

app = Flask(__name__)

@app.route('/')
def home():
    return frame(
        image='https://opengraph.githubassets.com/0x/devinaconley/python-frames',
        button1='next',
        post_url=url_for('second_page', _external=True),
    )

@app.route('/test')
def about():
    return 'Test'
