from flask import Flask
from flask_pymongo import PyMongo
from flask_restplus import Api,resource,Resource,reqparse
from flask import jsonify,json
from pymongo import MongoClient
app =Flask(__name__)
api =Api(app)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

empolye_list = [{'id':1,'name':'nithin','comapny':'pixdynamic','blood':'o-'},

                {'id':2,'name':'kukku','comapny':'pixdynamic','blood':'0+'},

                {'id':3,'name':'kannan','company':'pixdynamic','blood':'A-'}]


@api.route('/enter',methods=['POST'])
class posting(Resource):



    def __init__ (self):
        self.parser =reqparse.RequestParser()


    def get(self):
        self.parser = reqparse.RequestParser()
        return jsonify({'employe': empolye_list})


    def post(self):
        pass




# result_1 = customers.insert_one(empolye_list)
# result_2=customers.insert_one(empolye_list)





    #
    # def put(self,emp_id):
    #     emp_id_ = [emp_id_ for emp_id_ in empolye_list if emp_id_['id']==emp_id_]
    #     emp_id_[0][empolye_list]=






if __name__ == "__main__":
    app.run(debug=True)




