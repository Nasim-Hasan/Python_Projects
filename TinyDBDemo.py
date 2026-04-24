from tinydb import TinyDB, Query

# Create (or open) a database
db = TinyDB('database.json')

# Insert records
db.insert({'name': 'John', 'age': 22})
db.insert({'name': 'Michael', 'age': 16})

# Search for records
User = Query()
results = db.search(User.name == 'John')
print(results)

# Update a record
db.update({'age': 23}, User.name == 'John')
results = db.search(User.name == 'John')
print(results)

# Remove a record
db.remove(User.age < 18)