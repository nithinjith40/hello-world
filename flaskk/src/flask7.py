from flask import Flask,jsonify,json
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

empolye_list = [{'id':1,'name':'nithin','comapny':'pixdynamic','blood':'o-'},
{'id':2,'name':'kukku','comapny':'pixdynamic','blood':'0+'},
{'id':3,'name':'kannan','company':'pixdynamic','blood':'A-'}]

@api.route('/employes')
class empolye(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument('age')
        args = self.parser.parse_args()
        return jsonify({'employe_list':empolye_list})




    def put(self):
        self.parser.add_argument('name')
        args = self.parser.parse_args()
        ##new_put = [new_put for new_put in empolye_list if new_put['name']==argsname]
        return jsonify({'new_name': args})

    # def post(self):
    #     self.parser.add_argument('companie')
    #     args =self.parser.parse_args()
    #     return jsonify({'})



    #def post(self,)

    # def post(self)
    #     post = []

# @api.route('/get_one')
# class employee (Resource):
#     def get(self):
#         one_list =[one_list for one_list in empolye_list if one_list['name']=name]
#         return jsonify({'one_list':one_list[0]})



if __name__ == '__main__':
    app.run(debug=True)