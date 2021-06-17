from flask_pymongo import PyMongo
import flask

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb+srv://kumarangokul:DevChn606%@cluster0.rcdty.mongodb.net/todolist?retryWrites=true&w=majority")
db = mongodb_client.db

@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")

if __name__ == "__main__":    
    
    app.run()