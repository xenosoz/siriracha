#!/usr/bin/env python3

from flask import Flask
import json
import random

app = Flask(__name__)

@app.route('/')
def test():
    #with open('dev-python/seaborn/api-reference.json') as f:
    #with open('mooc-coursera/game-theory-1/terms.json') as f:
    #with open('nat-hanja/thousand/hanja-to-meaning.json') as f:
    with open('dev-cloud/amazon-web-services/services.json') as f:
        data = json.loads(f.read(), encoding='utf-8')
    cards = data['cards']
    card = random.choice(cards)
    source = data['source']

    trans_color = '#f4f4f4';

    rv = f'''
    <style>
      body {{
        position: relative;
        width: 100%;
        background-color: {trans_color};
        font-family: arial,sans-serif;
      }}
      .card {{
        width: 850px;
        margin: 10px auto;
        padding: 10px;
        border: 2px solid black;
        border-radius: 10px;
      }}
      .card-title {{
        font-size: 4em;
      }}
      .card-description {{
        font-size: 2.5em;
      }}
      .card-title span {{
        background-color: yellow;
      }}
      .card-source {{
        text-decoration: none;
        color: gray;
      }}
      .card-description {{
        margin: 20px auto;
        color: {trans_color};
      }}
    </style>
    <div class="card">
      <div class="card-title">
        <span>{card[0]}</span>
      </div>
      <div class="card-source">
        <a href="{source}">{source}</a>
      </div>
      <div class="card-description">
        {card[1]}
      </div>
    </div>
    '''

    return rv


app.run('localhost', 8000)
