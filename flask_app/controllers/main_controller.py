from flask_app import app
from flask import render_template, redirect, session, request, flash


# home/index route
@app.route('/')
def index():
    page = 'home'
    return render_template('index.html', page = page)

# Request Page
@app.route('/request')
def request_quote():
    page = 'request'
    return render_template('request.html', page = page)

# Calculator Page
# @app.route('/calculator')
# def calculator():
#     page = 'calculator'
#     return render_template('calculator.html', page = page)

# Gallery
@app.route('/gallery')
def gallery():
    page = 'gallery'
    return render_template('gallery.html', page = page)