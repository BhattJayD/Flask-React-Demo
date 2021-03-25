from flask import Flask,request,jsonify,make_response
import pymongo
from config import MONGO_URI
import os
from flask_jwt import JWT, jwt_required, current_identity
from Route import app
#from Settings.security import authenticate, identity





if __name__ == '__main__':
   app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)