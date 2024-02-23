def register(database):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    user_data = {"name": name, "email": email, "password": password}
    database.append(user_data)
    print("Registration successful!")

# Initialize the database as an empty list
database = []

# Register a user
register(database)

# Print the database to verify
print("Database:", database)

