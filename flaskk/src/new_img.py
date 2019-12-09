from flask import Flask
from flask import jsonify
from flask_restplus import Api,Resource
from flask_restplus import reqparse,fields
app = Flask(__name__)
api = Api(app)


languages=[{'id':1,'name':'python','usage':'programming'},{'id':2,'name':'java','usage':'programming'},{'id':1,'name':'python','usage':'programming'}]

@api.route('/language')
class list_language(Resource):
    def __init__(self,*args):
        self.parser=reqparse.RequestParser()
    def get(self):
        return jsonify({'language_list':languages})

    def put(self):
        self.parser.add_argument('id',type=int)
        self.parser.add_argument('name',type=str)
        self.parser.add_argument('usage',type=int)
        args= self.parser.parse_args()
        languages.append(args)
        return jsonify({'append':languages})

if __name__ == '__main__':
    app.run(debug=True)
