import json  # Import the JSON module to handle JSON data

# Define a class named User
class User:  
    # Constructor to initialize the User object
    def __init__(self, name, age):
        self.name = name  # Assign the name to the instance variable
        self.age = age    # Assign the age to the instance variable

# Create an instance(object) of the class  named User
user = User("Max", "27")  # Create User class ka object - user, with name "Max" and age "27"

# Function to encode User ke objects into a JSON-serializable format
def encode_user(o):
    if isinstance(o, User):  # Check if the object is an instance of User
        # Create a dictionary representation of the User object
        return {
            "name": o.name,        # Include the name
            "age": o.age,          # Include the age
            o.__class__.__name__: True  # Include the class name with a True value
        }
    else:
        # Raise an error if the object is not a User instance
        raise TypeError("Object of Type User is not json serializable")  

# Convert the user object to JSON format using the custom encoder
userJSON = json.dumps(user, default=encode_user)  

# Print the resulting JSON string
print(userJSON)  
