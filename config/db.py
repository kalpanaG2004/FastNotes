import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
if MONGO_URI:
    conn = MongoClient(MONGO_URI)
    print("Successfully connected to MongoDB.")
else:
    print("MongoDB URI not found in environment variables.")
