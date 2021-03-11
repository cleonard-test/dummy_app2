import json
import random

from flask import Flask, jsonify

app = Flask(__name__)

with open('./terms.json') as json_file:
    terms = json.load(json_file)


@app.route("/")
def insult():
    insult = generate_insult()
    return jsonify({'insult': insult})


@app.route("/ping")
def ping():
    return jsonify({'hello': 'world'})


def generate_insult():
    insult_terms = [random.choice(terms['terms'][i]) for i in range(3)]
    return '{} {} {}'.format(*insult_terms)
