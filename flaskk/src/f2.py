from flask import Flask, request
from flask_restful import Resource, Api
#from requests import put, get
from flask.views import MethodView

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        self.todo_id=todo_id
        return {'you sent some file': 1}


    def put(self, todo_id):
        self.todo_id=todo_id
        todos[todo_id] = request.form['data']
        return {'i dont sent a file':2}

api.add_resource(TodoSimple, '/<string:todo_id>',view_func=TodoSimple.as_view('todosample'))

if __name__ == '__main__':
    app.run(debug=True)