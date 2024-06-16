#!/usr/bin/env python3
"""
Python script that analyzes Nginx logs stored in MongoDB and prints statistics.
"""

import pymongo

def print_collection_stats(collection):
    # Total number of logs
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count for method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

def main():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    # Print statistics
    print_collection_stats(collection)

    # Close MongoDB connection
    client.close()

if __name__ == "__main__":
    main()
