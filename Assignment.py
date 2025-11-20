#NAME: MOHIT MISHRA
#ENROLLMENT NO.0157CY231068
#BATCH: 5
#BATCH TIME: 10:30 AM

students = []
logged_in_user = None

def register():
    print("\n--- Register Student ---")
    name = input("Enter Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")

    # storing as dictionary
    student = {
        "name": name,
        "username": username,
        "password": password,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year
    }

    students.append(student)
    print("Registration successful!\n")

def login():
    global logged_in_user
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    for student in students:
        if student["username"] == username and student["password"] == password:
            logged_in_user = student
            print("Login successful!\n")
            return
    print("Invalid credentials!\n")

def show_profile():
    if logged_in_user is None:
        print("Please login first!\n")
    else:
        print("\n--- Profile ---")
        for key, value in logged_in_user.items():
            if key != "password":
                print(f"{key.capitalize()}: {value}")
        print()

def update_profile():
        if logged_in_user is None:
            print("Please login first!\n")
        else:
            print("\n--- Update Profile ---")
            for key in logged_in_user.keys():
                if key != "username" and key != "password":
                    new_value = input(f"Enter new {key} (leave empty to keep same): ")
                    if new_value != "":
                        logged_in_user[key] = new_value
            print("Profile updated!\n")

def logout():
    global logged_in_user
    logged_in_user = None
    print("Logged out!\n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Show Profile")
    print("4. Update Profile")
    print("5. Logout")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        show_profile()
    elif choice == "4":
        update_profile()
    elif choice == "5":
        logout()
    elif choice == "6":
       print("exiting selected but you are still in the system.\n ")
    else:
        print("Invalid choice!\n")
