from pymongo import MongoClient
from pymongo.server_api import ServerApi
import logging
import os

logger = logging.getLogger(__name__)

MONGODB_URI = "mongodb+srv://sutgJxLaXWo7gKMR:sutgJxLaXWo7gKMR@cluster0.2ytii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_NAME = "Hospital_login_system"

try:
    client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
    client.admin.command('ping')
    logger.info("Successfully connected to MongoDB Atlas!")

    db = client[MONGODB_NAME]
    users_collection = db["patients"]
    admins_collection = db["admins"]
    doctors_collection = db["doctors"]

    # Create indexes
    users_collection.create_index("email", unique=True)
    admins_collection.create_index("email", unique=True)
    doctors_collection.create_index("email", unique=True)

except Exception as e:
    logger.error(f"Error connecting to MongoDB Atlas: {str(e)}", exc_info=True)
    raise 