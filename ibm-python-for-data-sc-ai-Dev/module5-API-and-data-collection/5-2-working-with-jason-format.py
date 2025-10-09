# Working with json files
import json
#  To handle the data flow in a file, the JSON library in Python uses the 'dump()' or 'dumps()' function to convert the Python objects
#  into their respective JSON object. This makes it easy to write data to files.
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# * serialization using dump() function:
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)
# *serialization using dumps() function

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
print(json_object)
