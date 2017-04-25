import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from gif import gif

app = Flask(__name__)


@app.route('/')
def hello_world():
    term=request.args.get('text')
    if term:
        imglink=gif(term)
    else:
        term=gif("failure")
    response = { 
    "response_type" : "in_channel",
    "attachments" : [
        {"fallback": "Image search found http://i.imgur.com/cZDQXQ3.gif",
        "image_url":imglink }
        ]
    } 
    if len(imglink) > 5:
        return jsonify(**response)
    else:
        return "No gif found :("
