from flask import Flask, render_template
app = Flask(__name__)

# Defining homepage
@app.route('/') # Defines single route to homepage
def index():
  return render_template 'index.html' # Renders HTML template

if __name__ == '__main__':
  app.run(debug=True) 
