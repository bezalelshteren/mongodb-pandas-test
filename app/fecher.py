import pandas as pd
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient("mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
print(client)
class cech_data:
    def __init__(self):
        self.conection = os.getenv("CONNECTION")
        self.db_name = os.getenv("DB_NAME","IranMalDB")
        self.client = pymongo.MongoClient(self.conection)
        self.data = None
        self.df = None

    def connect_and_read(self):
        my_db = client[self.db_name]
        my_coll = my_db["tweets"]
        self.data = my_coll.find().limit(15).to_list()
        self.df = pd.DataFrame(self.data)
        self.df["_id"] = self.df["_id"].astype(str)
        return self.df


# x = cech_data()
# x.connect_and_read()
#
# cech_data1 = cech_data()
# cech_data1.connect_and_read()