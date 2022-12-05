import pymongo
import pandas 
import json
import os 
from dataclasses import dataclass

# Provide the mongodb localhost url to connect python to mongodb.

@dataclass
class EnvironmentVariable:
    mongo_db_url : str = os.getenv("mongodb_url")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

