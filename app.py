from flask import Flask, redirect, url_for, abort, request, render_template, json
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html'), 200

@app.route('/browse')
def browse():
  return render_template('browse.html'), 200

@app.route('/browse', methods=['POST', 'GET'])
def genre():
  error = None
  my_genre = request.form['my_genre'].lower()
  if my_genre == "":
    error = 'You must enter a search term - try again'
    return render_template('/browse.html', error=error)
  else:
    json_data = open('static/json/' + my_genre + '.json').read()
    result = json.loads(json_data)
    return render_template('results.html', my_genre=my_genre, result=result)

# Validate admin logon
def auth_logon(username, password):
  if username == password:
    return True
  else:
    return False

# If form is POST-ed and validated, grab u/n and p/w via request.form 
@app.route('/admin', methods=['GET', 'POST'])
def admin():
  #Set up error handler below
  error = None
  if request.method == 'POST':
    if auth_logon(request.form['username'], request.form['password']):
      return redirect(url_for('welcome', username=request.form.get('username')))
    else:
      error = 'Wrong username or password - CLICK HERE to try again'
  return render_template('admin.html', error=error)

@app.route('/welcome/<username>')
def welcome(username):
  return render_template('welcome.html', username=username)

#Image upload view function
@app.route("/upload/", methods=['POST', 'GET'])
def upload():
  error = None
  if request.method =='POST':
    f = request.files['datafile']
    new_file = f.filename
    if new_file == "":
      error = "Please select a file to upload"
      return render_template('upload.html', error=error)
    f.save('static/img/' + new_file)
    return redirect(url_for('success'))
  else:
    return render_template('upload.html'), 200

@app.route('/success')
def success():
  return render_template('success.html'), 200

@app.route('/logout')
def logout():
  return render_template('logout.html')

# comment out below - only for testing
@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
