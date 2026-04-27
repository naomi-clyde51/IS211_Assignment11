from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Tasks
tasks = []

# Defining homepage
@app.route('/') # Defines single route to homepage
def index():
  return render_template ('index.html', tasks=tasks) # Renders HTML template

# Submitting a New Item
@app.route('/add', methods=['POST'])
def add_task():
  new_task = request.form.get('newTask') # Gets data submitted in HTML form
  if new_task:
    tasks.append(new_task) # If there is true data submitted, then it's added to tasks
  return redirect(url_for('index')) # Redirects user back to homepage

# Clear the list
@app.route('/clear', methods=['POST'])
def clear_tasks():
  tasks.clear()
  return redirect(url_for('index')) # Redirects user back to homepage

if __name__ == '__main__':
  app.run(debug=True) 
