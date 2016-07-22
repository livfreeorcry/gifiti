import os
from flask import Flask, render_template, request, redirect, url_for
from gif import gif

app = Flask(__name__)


@app.route('/')
def hello_world():
    imglink=gif("pepe")
    response="""{{text:"{0}"}}"""
    return response.format( imglink )