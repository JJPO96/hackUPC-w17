from eventlift import app, models
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')
