# Function returning multiple pieces of data packed inside a dictionary
def get_user_info():
    return {
        "name": "Alice",
        "age": 22,
        "department": "BBA"
    }

# Storing and accessing the returned dictionary
user_data = get_user_info()
print("Student Name:", user_data["name"])
print("Department:", user_data["department"])


def get_person_info():
    return {
        "name": "Amit",    
        "age": 90,
        "city": "Dhaka"
    }

info = get_person_info()
print (info["name"]) 
print(info["age"])
print(info["city"])




def print_user_info(user):
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")    
    print(f"City: {user.get('city', 'Unknown')}")

user_data = {"name": "Bob", "age": 25}
print_user_info (user_data)