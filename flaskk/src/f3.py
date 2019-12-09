from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from requests import put, get
from flask import abort

app = Flask(__name__)
api = Api(app)

todos = [
    {'todo1':'get the milk',
     'todo_id':1},
    {'todo2':'do not get the milk',
     'todos_id':2}

]

class TodoSimple(Resource):
    def get(self):
        return jsonify({'todos':todos})

    def put(self):
        


api.add_resource(TodoSimple,'/todo',methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)