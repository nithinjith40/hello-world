from flask import Flask,jsonify,json,request
from flask_restplus import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

empolye_list = [{'id':1,'name':'nithin','comapny':'pixdynamic','blood':'o-'},
{'id':2,'name':'kukku','comapny':'pixdynamic','blood':'0+'},
{'id':3,'name':'kannan','company':'pixdynamic','blood':'A-'}]

@api.route('/hello/<int:id>')
class getit(Resource):
    def get(self):
        return jsonify({'employee':empolye_list})

    def put(name):
        put_values=[put_values for put_values in empolye_list if put_values['name']==name]
        put_values[0]['name'] = request.json['name']
        return jsonify({'employe_list':put_values[0]})
        

    

if __name__ == '__main__':
    app.run(debug=True)