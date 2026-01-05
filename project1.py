import json
 
 #load json data
def load_data(filename):
     with open(filename , "r") as file:
         data= json.load(file)
     return data
 #display data 
def display_users(data):
     print("Users and Their Connection:\n")
     for user in data["users"]:
         print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")
         print("\n Pages\n")
     for pages in data["pages"]:
         print(f"{pages['id']}: {pages['name']}")
         
 #load and dispaly data
data = load_data("codebook_data.json")
display_users(data)        