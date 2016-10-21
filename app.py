from flask import Flask, redirect, url_for, abort, request, render_template, json
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html'), 200

@app.route('/browse')
def browse():
  return render_template('browse.html'), 200

@app.route('/browse', methods=['POST', 'GET'])
def genre():
  my_genre = request.form['my_genre']
  return render_template('results.html', my_genre=my_genre)

@app.route('/admin')
def admin():
  return render_template('admin.html')

@app.route("/upload/", methods=['POST', 'GET'])
def upload_img():
  if request.method =='POST':
    f = request.files['datafile']
    my_filename = f.getvalue()
    f.save('static/img/' + my_filename)
    return render_template('success.html'), 200
  else:
    return render_template('upload.html'), 200

# comment out below - only for testing
@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Could not find the page you requested.", 404

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
