
from flask import Flask, redirect, url_for, abort, request
app = Flask(__name__)

@app.route('/')
def home():
  return 'Home page'

@app.route('/genre/<query>')
def genre(query):
  return 'This is the %s page' % query

# comment out below - only for testing
@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Could not find the page you requested.", 404



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

