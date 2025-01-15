#import pymongo


#uri = "mongodb+srv://ssevgi349:@cluster0.cnf9u.mongodb.net/?appName=Cluster0"

# myclient = pymongo.MongoClient(uri)

# mydb = myclient["mydatabase"]

from pymongo.mongo_client import MongoClient
import csv
import pandas as pd
import json
import urllib,io,json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI


uri = "mongodb+srv://user2:sifre@cluster0.cnf9u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["mydatabase"]

mycol = mydb["SpotifyMusics"]

unique_fields = set()

# Koleksiyondaki tüm belgeleri iterasyonla dolaş
for doc in mycol.find():
    for key in doc.keys():
        unique_fields.add(key)

# Benzersiz alanları liste olarak yazdır
# print(list(unique_fields))
# fields = 

prompt="""
you are a very intelligent AI assitasnt who is expert in identifying relevant questions fro user
from user and converting into nosql mongodb agggregation pipeline query.
Note: You have to just return the query as to use in agggregation pipeline nothing else. Don't return any other thing
Please use the below schema to write the mongodb queries , dont use any other queries.
schema:
the mentioned mogbodb collection talks about Spotify data .The schema for this document represents the structure of the data, describing various properties related
to with this fields :{unique_fields} 
your job is to get python code for the user question.

Below are several sample user questions related to the MongoDB document provided, 
and the corresponding MongoDB aggregation pipeline queries that can be used to fetch the desired data.
Use them wisely.
.
As an expert you must use them whenever required.
Note: You have to just return the query nothing else. Don't return any additional text with the query.Please follow this strictly
input:{question}
output:
"""
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-fNrYR9Otfk3LoNAhjW8UT3BlbkFJxHayU6zlR9FCVhhHW1z3"

query_with_prompt=PromptTemplate(
    template=prompt,
    input_variables=["unique_fields","question"]
)
question = "get the  artists names is Ben Woodward"

llm=ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"],temperature=0.0)
 
llmchain=LLMChain(llm=llm,prompt=query_with_prompt,verbose=True)

response=llmchain.invoke({
            "question":question,
            "unique_fields":unique_fields
        })

print(response)

query=json.loads(response["text"])
results=mycol.aggregate(query)
print(query)
# list = []
# with open("spotify.csv", 'r') as file:
#     data = csv.reader(file,delimiter = '\n')  # extracting one row 
#     for i in data:
#         list.append(i[0].split(';')) #splitting the data with delimiter ;

# with open('new_updated.csv', 'w',newline='') as data:
#     writer = csv.writer(data)
#     writer.writerows(list)

# with open("spotify.csv", mode='r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
#         mycol.insert_one(row)

# data = pd.read_csv("spotify.csv")
# data_json = json.loads(data.to_json(orient='records'))
# mycol.remove()
# mycol.insert(data_json)


# def convert_age_to_int():
#     documents = mycol.find({"popularity": {"$type": "int"},
#                             "danceability": {"$type": "double"},
#                             })
#     for doc in documents:
#         new_popularity= int(doc["popularity"])
#         mycol.update_one({"_id": doc["_id"]}, {"$set": {"popularity": new_popularity}})

#         new_danceability= int(doc["danceability"])
#         mycol.update_one({"_id": doc["_id"]}, {"$set": {"danceability": new_danceability}})



#         print(f"Updated document ID {doc['_id']}")
# convert_age_to_int()
# myquery = { "artists": "Ben Woodward" ,
#              "track_genre": "acoustic"}

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)


