
from flask import Flask,request,jsonify,make_response
import pymongo
from config import MONGO_URI
import os
from flask_jwt import JWT, jwt_required, current_identity
app = Flask(__name__, static_folder='./client1/build', static_url_path='/')
app.secret_key = 'secret'
#jwt = JWT(app)
""", authenticate, identity)"""
try:
    myclient = pymongo.MongoClient(MONGO_URI)
    db = myclient["data"]  
    # Collection name  
    col = db["segment"]
    user=db["user"]
    myclient.server_info()
    print('###########Database Connected!##########')
except:
    print("Can't connect to DB")

def most_frequent(List): 
    return max(set(List), key = List.count) 



@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/list',methods=["GET"])
def lists():
    output = []
    for s in col.find():
        if s["location"]:
            output.append(s['location'])
    #que=list(set(output))
    
    return jsonify({'place' : output})


@app.route('/count',methods=["GET"])
def count():
    sum=col.find().count()
    return jsonify({'Total' : sum})


@app.route('/stats',methods=["GET"])
def stats():
    attacker_king=[]
    defender_king=[]
    region=[]
    name=[]
    Attacker_outcome = []
    defender_size=[]
    battle_type=[]
    win=0
    loss=0
    for s in col.find():
        if s["attacker_king"]:
            attacker_king.append( s['attacker_king'])
        if s["defender_king"]:
            defender_king.append( s['defender_king'])
        if s['region']:
            region.append( s['region'])
        if s['name']:
            name.append( s['name'])
        if s['attacker_outcome']:
            Attacker_outcome.append( s['attacker_outcome'])
        if s['battle_type']:
            battle_type.append( s['battle_type'])
        if s['defender_size']:
            defender_size.append( s['defender_size'])
    most_frequent_attacker_king=most_frequent(attacker_king)
    most_frequent_defender_king=most_frequent(defender_king)
    most_frequent_region=most_frequent(region)
    most_frequent_name=most_frequent(name)
    most_active=[
        {
        'attacker_king':most_frequent_attacker_king,
        'defender_king':most_frequent_defender_king,
        'region':most_frequent_region,
        'name':most_frequent_name
        }]
    for i in range(0,len(Attacker_outcome)):
        if Attacker_outcome[i]=="win":
            win=win+1
        elif Attacker_outcome[i]=="loss":
            loss=loss+1
        winloss=[{"win":win},{"loss":loss}]
    uni=set(battle_type)
    que=(list(uni))
    defender_size=[int(i) for i in defender_size]
    defender_size.sort()
    minDefender_size=defender_size[0]
    maxdefender_size=defender_size[-1]
    avgdefender_size=(sum(defender_size)/len(defender_size))
    defenderInfo=[
        {'average':avgdefender_size},
        {'min':minDefender_size},
        {'max':maxdefender_size}]
    stats=[
        {
        "most_active":most_active,
        'Attacker_outcome' : winloss,
        "battle_type":que,
        'defender_size':defenderInfo
        }
        ]
    return jsonify({"stats":stats})

@app.route('/search', methods=['GET'])
def get_query_string():
    output = []
    user = request.query_string.decode("utf-8") 
    Dict = dict((x.strip(), y.strip()) 
             for x, y in (element.split('=')  
             for element in user.split('&'))) 
    var=col.find(Dict,{'_id': 0})
    for s in var:
        output.append(s)
    return jsonify({'place' : output})

   
