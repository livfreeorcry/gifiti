import os
from flask import Flask, render_template, request, redirect, url_for
from gif import gif

app = Flask(__name__)

@app.route('/')
def hello_world():
    return gif("dickbutt")