import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from gif import gif

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        term=request.args.get('text')
    except:
        term="pepe"
    imglink=gif(term)
    response = { "response_type" : "in_channel", "attachments" : [ { "text":imglink } ] } 
    if len(imglink) > 5:
        return jsonify(**response)
    else:
        return "No gif found :("