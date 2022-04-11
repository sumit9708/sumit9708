from flask import Flask , request , jsonify
import pymysql.cursors
import pymongo

# for sql connection

connection = pymysql.connect( host ='localhost',
                              user ='root',
                              password = 'changedpassword',
                              database= 'cardataset',
                              charset= 'utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)

# for mongodb connection
client = pymongo.MongoClient("mongodb+srv://sumit112:sumit112@clustersam.zhmes.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Changed DB name

app = Flask(__name__)
@app.route("/getsqldata",methods=['GET'])
def getsqldata():
    result=""
    with connection.cursor() as cursor:
        sql = "select * from data1 limit 10"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = str(result)
    return str(result)

@app.route("/getmongodbdata",methods =['POST'])
def getmongodbdata():
    coll = db.newtab
    data={"result":str(list(coll.find().limit(100)))}
    return data
if (__name__=="__main__"):
    app.run(port=7000)

