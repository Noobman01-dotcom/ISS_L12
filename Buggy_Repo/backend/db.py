from motor.motor_asyncio import AsyncIOMotorClient
import os

def init_db():
    """
    Initializes the MongoDB client and returns the collections used in the app.
    """
    # Get the MongoDB URI from environment variable or use default
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")

    # Initialize the async MongoDB client
    client = AsyncIOMotorClient(MONGO_URI)

    # Select the database
    db = client["testdb"]

    # Return a dictionary of collections needed by the app
    return {
        "items_collection": db["item"],  # Access 'item' collection
        "users_collection": db["users"]  # Access 'users' collection
    }

# ✅ NOTES:
# - Using environment variable makes this portable across dev/prod.
# - Returning dictionary makes usage cleaner and centralized.
# - Collection names are consistent (e.g., "item" and "users").
# - Comments are added to explain each section.
