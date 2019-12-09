from flask import Flask,jsonify
from flask_restplus import Resource, Api,fields
from flask import request,json

app = Flask(__name__)
api = Api(app)
#new_language = api.model('language',{'language':fields.String('the language')})

#school_list = []
new_list=[{'id':1,
          'name':'nithitn',
        'devision':'5d',
          'bllod':'o-'},
{'id':2,
 'name':'kannan',
 'devishion':"6D0",
 'blood':'a-'},
          {'id':3,
           'name':'jithu',
           'division':'4D',
           'blood':'b-'}]
#school_list.append(new_list)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'school_list':new_list}

@app.route('/newmethod', methods=['POST'])
class post(Resource):
    def post(self):
        new_list ={
            'id':new_list[-1]['id']+1
            'name':request.()
            'divishion':request.json()
            'blood':request.json()



        }


    '''
    def post(self):
        api.payload()
        return {}


   # @api.expect(new_language)
   # def post(self):
   #     new_language.append(api.payload)
    #    return ({'result':'language_added'}),201


'''


if __name__ == '__main__':
    app.run(debug=True)
