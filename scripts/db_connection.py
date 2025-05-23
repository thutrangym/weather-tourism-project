
# db_connection.py

from pymongo import MongoClient

def get_mongo_collection(
    db_name="weather_tourism",
    collection_name="weather_data",
    host="127.0.0.1",
    port=27017
):
    """
    Kết nối đến MongoDB local và trả về đối tượng collection.

    Parameters:
        db_name (str): Tên database.
        collection_name (str): Tên collection.
        host (str): Địa chỉ server MongoDB.
        port (int): Cổng kết nối.

    Returns:
        collection: Đối tượng pymongo.collection.Collection
    """
    try:
        client = MongoClient(f"mongodb://{host}:{port}/")
        db = client[db_name]
        collection = db[collection_name]
        print(f"Connection success: {db_name}.{collection_name}")
        return collection
    except Exception as e:
        print(f"Connection error: {e}")
        return None
