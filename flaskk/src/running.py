from flask import Flask,request
from flask import jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask_restplus import Api,Resource
from flask_restplus import reqparse



app =Flask(__name__)
api =Api(app)
client =MongoClient('mongodb://localhost:27017')
db =client['db']
col = db['star']
empolye_list = [{'id':1,'name':'nithin','comapny':'pixdynamic','blood':'o-'},
{'id':2,'name':'kukku','comapny':'pixdynamic','blood':'0+'},
{'id':3,'name':'kannan','company':'pixdynamic','blood':'A-'}]


@api.route('/enter')
class Name(Resource):
    def __init__(self,*args):
        self.parser = reqparse.RequestParser()

    def get(self):
        return jsonify({'emp_list':empolye_list})

    def post(self):
        #self.parser = reqparse.RequestParser()
        self.parser.add_argument('id')
        self.parser.add_argument('name')
        self.parser.add_argument('blood')
        self.parser.add_argument('comapny')
        args=self.parser.parse_args()
        col.insert_one(args)
        #return jsonify({'postlist':empolye_list})

#myrecord = db.client.insert(args)
    #newlist =[v for v in empolye_list ]

    # def delete(self):

    #     self.parser.remove_argument('id')
    #     self.parser.remove_argument('blood')
    #     self.parser.remove_argument('name')
    #     self.parser.remove_argument('company')
    #     args = self.parser.parse_args()
    #     empolye_list.append(args)
    #     return jsonify({'new_name':empolye_list})
    #
    # def put(self,id):
    #     self.parser =reqparse.RequestParser()
    #     self.parser.add_argument('id',)
    #     self.parser.add_argument('name',type=str)
    #     self.parser.add_argument('company',type=str)
    #     self.parser.add_argument('blood',type=str)
    #     args =self.parser.parse_args()
    #     empolye_list.append(args)




if __name__ =='__main__':
    app.run(debug=True)








