from pymongo import MongoClient
from urllib.parse import quote_plus
username = "PriyankaSahoo"
password = quote_plus("MySQL@2025")
uri = f"mongodb+srv://{username}:{password}@cluster0.1ncugbu.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully!")
except Exception as e:
    print(e)