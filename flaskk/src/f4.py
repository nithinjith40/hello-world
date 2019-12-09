from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask import abort
app = Flask(__name__)
api = Api(app)
languages = [{'name':'python','id':1,
              'usage':'programming',},
              {'name':'java','id':'2',
               'usage':'programmimg'}]
class language(Resource):
    def get(self,lang_id,first_one):
        pass

    def put(self,first_one):
        first_one = [first_one for first_one in languages if first_one['id']== lang_id]
        languages[0]=
        return jsonify({'languages': languages[0]})


api.add_resource(language,'/program/')
api.add_resource(language,'/get_id')
if __name__ == '__main__':
    app.run(debug=True)

