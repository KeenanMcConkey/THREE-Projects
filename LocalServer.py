#!/usr/bin/env python

# Local web server using Flask

# App is Flask object
from flask import Flask, render_template, url_for
app = Flask(__name__)

# Display index html
@app.route('/')
def index():
    return render_template('index.html')

# Add other routes here
