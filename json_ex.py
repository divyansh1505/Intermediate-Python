import json

person = {
"name" : "divyansh",
"age" : "18",
"city" : "New Delhi",
"has children" : False,
"titles" : ["Engineer", "Programmer"]
}

personJSON = json.dumps(person, indent=4, sort_keys = True)
# the s in dumps stands for string, mtlb i dumped the person
#as a string
print(personJSON)

with open ("person.json", "w") as f:
    json.dump(person, f, indent=4)

#We converted python object to json data.

# Now lets convert json data to python object (decoding)

person = json.loads(personJSON)
print(person)


