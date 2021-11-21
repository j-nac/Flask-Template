from flask import render_template, url_for
from flaskr import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home')