import json

# Read the contents of the "tak_users.txt" file
with open("tak_users.txt", "r") as file:
    json_data = file.read()

# Parse the JSON string into a Python list of dictionaries
data = json.loads(json_data)

# Initialize empty lists to store usernames and passwords
usernames = []
passwords = []

# Iterate through the list of dictionaries and extract usernames and passwords
for entry in data:
    usernames.append(entry["username"])
    passwords.append(entry["password"])

# Now, you have the usernames and passwords in separate lists
print("Usernames:", usernames)
print("Passwords:", passwords)
