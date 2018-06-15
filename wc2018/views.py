import os
from flask import Flask, request, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/images/')
def images():
    return render_template('images/')

@app.route('/css/')
def css():
    return tender_template('css/')

@app.route('/js')
def js():
    return render_template('js/')
