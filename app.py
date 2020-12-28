from flask import Flask
import bitly_api

app = Flask(__name__)

BITLY_ACCESS_TOKEN = 'd88405c8b374e9aa3d981ff64ff7f09450e700af'
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

# This needs to be inserted into the HTML as a form with a button to return the shortened link
full_link = input()
short_url = access.shorten(full_link)
print('Short URL = ', short_url['url'])
# Basic functionality, needs to be wrapped around as a flask function to satisfy a GET request from the user

@app.route('/')
def index():

