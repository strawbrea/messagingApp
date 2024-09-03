from mongita import MongitaClientDisk

quotes_data = quotes_data = [
    {"text": "I'm hungry. When's lunch?", "author": "Dorothy", "owner": "Greg", "allow_comments": True},
    {"text": "You threw that ball. You go get it.", "author": "Suzy", "owner": "Dorothy", "allow_comments": False},
]

user_data = [
    {"username": "Dorothy", "hashed_password": "<hashed_pw>", "salt": "<salt>", "bio": "Loves quotes!", "avatar_url": "url_to_avatar"},
    {"username": "Greg", "hashed_password": "<hashed_pw>", "salt": "<salt>", "bio": "Enjoys hiking.", "avatar_url": "url_to_avatar"}
]

messages_data = [
    {"sender": "Dorothy", "receiver": "Greg", "message": "Hi Greg!", "timestamp": "2024-09-02 10:00:00"},
    {"sender": "Greg", "receiver": "Dorothy", "message": "Hello Dorothy!", "timestamp": "2024-09-02 10:05:00"},
]

# create a mongita client connection
client = MongitaClientDisk()

# create user database and collection
user_db = client.user_db
user_collection = user_db.user_collection

# create messages collection
messages_db = client.messages_db
messages_collection = messages_db.messages_collection

# create a quote database
quotes_db = client.quotes_db

# create a quotes collection
quotes_collection = quotes_db.quotes_collection

# create comments collection
comments_collection = quotes_db.comments
quotes_collection.create_index([("text", "text")])

# empty the collection
quotes_collection.delete_many({})
user_collection.delete_many({})
messages_collection.delete_many({})

# put the users in the database
user_collection.insert_many(user_data)

# put the messages in the database
messages_collection.insert_many(messages_data)

# put the quotes in the database
quotes_collection.insert_many(quotes_data)

# make sure the quotes are there
print(user_collection.count_documents({}))
print(messages_collection.count_documents({}))
print(quotes_collection.count_documents({}))
