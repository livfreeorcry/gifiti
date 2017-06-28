import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from gif import gif

app = Flask(__name__)


@app.route('/')
def hello_world():
    term=request.args.get('text',methods=['GET','POST'])
    if term:
        imglink=gif(term)
    else:
        imglink=gif("failure")
    response = { 
    "response_type" : "in_channel",
    "attachments" : [
        {"fallback": "Image search found "+imglink,
        "image_url":imglink }
        ]
    } 
    if len(imglink) > 5:
        return jsonify(**response)
    else:
        return "No gif found :("
