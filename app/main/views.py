from . import main
from flask import render_template

@main.route('/')
def home():
    '''Home route'''

    return render_template('index.html', message='Lorem Ipsum')
