from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')

client = MongoClient(MONGO_CONNECTION_STRING)

db_client = client['crud-mongo']