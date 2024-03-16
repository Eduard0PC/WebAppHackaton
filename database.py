from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://gerardomecott:i7DXLqEhhzjFvs3Y@cluster0.mdglzfu.mongodb.net/DB_EJAD?retryWrites=true&w=majority'
ca = certifi.where()
def dbConnection():
    try: 
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["DB_EJAD"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db