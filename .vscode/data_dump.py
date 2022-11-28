import pymongo
import pandas as pd
import json

data_file_path="/config/workspace/aps_failure_training_set1.csv"
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(data_file_path)
    print({df.shape})

    #convert dataframe
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #convert json into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)