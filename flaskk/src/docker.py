from flask import Flask
from flask_restplus import Api,reqparse,Resource
from pymongo import MongoClient


app =Flask(__name__)
api =Api(app)
Clienet =MongoClient('mongodb://localhost:27017')
db =Clienet['data_flask']



