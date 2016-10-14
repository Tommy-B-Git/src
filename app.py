
from flask import Flask, redirect, url_for, abort, request
app = Flask(__name__)

@app.route('/')
def home():
  return 'Home page'

@app.route('/genre/<query>')
def genre(query):
  return 'This is the %s page' % query



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

