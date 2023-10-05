import json
import pandas as pd

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

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Username': usernames, 'Password': passwords})

#Output the DataFrame to a CSV file
df.to_csv("output.csv", index=False)

print("Usernames and passwords have been exported to 'output.csv'")

# Create and open an output file in write mode
#with open("output.txt", "w") as output_file:
    # Write the usernames and passwords to the file
#    for username, password in zip(usernames, passwords):
#        output_file.write(f"Username: {username}, Password: {password}\n")

#print("Usernames and passwords have been exported to 'output.txt'")
