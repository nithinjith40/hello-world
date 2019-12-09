from flask import Flask,jsonify,json
from flask import make_response
from flask import request
#from flask_restplus import Api
#from flask import Flask
#from flask_restful import Resource, Api
from flask import Flask
from flask_restplus import Resource, Api
from requests import put, get



app = Flask(__name__)
api = Api(app)
#api.init_app(app)

todoapp =[
    {
        'id': 1,
        'title': 'todo app one',
        'description':'find better language',
        'done':'undone'

    },
    {
        'id': 2,
        'title':'nothing',
        'description': u'Need to find a good Python tutorial on the web',
        'done': 'nothing2'
    }
]

@api .route('/enter',methods=['GET'])
class todo(Resource):
    def get(self):
        return jsonify({'todoapp':todoapp})

@api.route('/enter/new/<int:id>',methods=['PUT'])
class todo1(Resource):
    def put(self,task_id):
        def update_task(task_id):
            import pdb; pdb.set_trace()
            task = [tasks for tasks in todoapp if tasks['id'] == task_id]
            task[0]['title'] = request.json.get('title', task[0]['title'])
            task[0]['description'] = request.json.get('description', task[0]['description'])
            task[0]['done'] = request.json.get('done', task[0]['done'])
            return jsonify({'task': task[0]})


        # task = [task for task in todoapp if task['id'] == task_id]
        # task[0]['title'] = request.json.get('title', task[0]['title'])
        # return jsonify({'task': task[0]})

        # new_task = [new_task for new_task in todoapp if new_task['id'] == new_task]
        # new_task[0]['title'] = request.put('title', new_task[0]['title'])
        # new_task[0]['description'] = request.put('description', new_task[0], ['description'])
        # new_task[0]['id'] = request('id', new_task[0], ['id'])
        # return jsonify({'todoapp':new_task[0]})




    '''
    def put(self,todo_id):
        new_task = [new_task for new_task in todoapp if new_task['id']==todo_id]
        new_task[0]['title']= json.request.get('title',new_task[0]['title'])
        new_task[0]['description']= json.request('description',new_task[0],['description'])
        new_task[0]['id']=json.request('id',new_task[0],['id'])

        return jsonify({'newtask':new_task[0]})

    def delete(self,todo_id):
        new_id =[new_task for new_task in todoapp if new_task['id']==todo_id]
        todoapp.remove(new_id[0])
        return jsonify({'todoapp':todoapp})
'''

if __name__== '__main__':
    app.run(debug=True)




