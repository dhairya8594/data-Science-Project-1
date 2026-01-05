📘 CodeBook Data Analysis – Introduction Task
🚀 Internship Task Overview

Congratulations! 🎉
You’ve been hired as a Data Scientist Intern at CodeBook – The Social Media for Coders, a Delhi-based startup. On successful completion of this 1-month internship, you stand a chance to receive a ₹10 LPA job offer.

Your first assignment, given by your manager Puneet Kumar, is to analyze a dataset of CodeBook users using pure Python only—no external libraries like Pandas, NumPy, or any other advanced tools.

🧠 Objective

The goal of this task is to:

Load user data stored in JSON format

Understand the structure of the data

Display users, their connections (friends), and liked pages in a readable format using Python’s built-in modules

📂 Dataset Description

The dataset consists of two main components:

👤 Users

Each user contains:

id: Unique user ID

name: User name

friends: List of friend IDs

liked_pages: List of page IDs the user has liked

📄 Pages

Each page contains:

id: Unique page ID

name: Page name

🔗 Connections

Users can have multiple friends

Users can like multiple pages

🗃 Sample Data (JSON Format)
{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 3, "name": "Rahul", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2], "liked_pages": [104]}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Dev Hub"}
    ]
}

📝 Task Breakdown
✅ Task 1: Load the User Data

Save the data in a file named codebook_data.json

Read the JSON file using Python

✅ Task 2: Display the Data

Print user details along with:

Friends list

Liked pages

Print all available pages

🧑‍💻 Code Implementation
import json

# Load the JSON file
def load_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Display users and their connections
def display_users(data):
    print("Users and Their Connections:\n")
    for user in data["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")

    print("\nPages:\n")
    for page in data["pages"]:
        print(f"{page['id']}: {page['name']}")

# Load and display the data
data = load_data("codebook_data.json")
display_users(data)

📤 Expected Output
<img width="426" height="520" alt="Screenshot 2026-01-05 224937" src="https://github.com/user-attachments/assets/ea904c77-6b5e-4b6d-a84a-d88d98321f7b" />

🏁 Conclusion

This task demonstrates:

Reading and parsing JSON data using Python

Understanding relational data (users, friends, pages)

Displaying structured information without external libraries

This forms the foundation for deeper data analysis tasks ahead in the internship. 💡💻
