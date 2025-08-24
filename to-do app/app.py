import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# --- Database Connection ---
# Get the MongoDB host from the environment variable set in docker-compose.yaml
mongo_host = os.getenv('MONGO_HOST', 'localhost')
client = MongoClient(host=mongo_host, port=27017)
db = client.tododb

@app.route('/')
def index():
    """Main page: Fetches all to-do items and displays them."""
    todos = db.todos.find()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """Handles adding a new to-do item."""
    new_todo = request.form.get('todoitem')
    if new_todo:
        db.todos.insert_one({'text': new_todo})
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete_todo(id):
    """Handles deleting a to-do item by its ID."""
    db.todos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)