#Student Management System 
#1. Add student
#2.Show
#3. Update
#4. Delete
#5. Exit
#select my choice 
#Enter student ID : 101
#Enter student roll number : 11
#Enter student name : Prashant
#Enter student city : Nagpur
#while updating : 
#enter student id : 
#Matched studetn record are given below select an option to update :
#1. update name
#2. update roll
#3. update city
#4. don't update
#while deleting : 
#enter student id : 
#Matched studetn record are given below select an option to delete :
#1. delete name
#2. delete roll
#3. delete city
#4. delete the id
#5. don't delete
students = {}
while True:
    print("\n# Student Management System")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = int(input("Select your choice: "))
    # Add Student
    if choice == 1:
        sid = int(input("Enter student ID: "))
        roll = int(input("Enter student roll number: "))
        name = input("Enter student name: ")
        city = input("Enter student city: ")
        students[sid] = {
            "roll": roll,
            "name": name,
            "city": city
        }
        print("Student added successfully!")
    # Show Students
    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            for sid, data in students.items():
                print("\nStudent ID:", sid)
                print("Roll:", data["roll"])
                print("Name:", data["name"])
                print("City:", data["city"])
    # Update Student
    elif choice == 3:
        sid = int(input("Enter student ID: "))
        if sid in students:
            print("\nMatched student record:")
            print(students[sid])
            print("\nSelect an option to update:")
            print("1. Update Name")
            print("2. Update Roll")
            print("3. Update City")
            print("4. Don't Update")
            uchoice = int(input("Enter choice: "))
            if uchoice == 1:
                new_name = input("Enter new name: ")
                students[sid]["name"] = new_name
                print("Name updated successfully!")
            elif uchoice == 2:
                new_roll = int(input("Enter new roll: "))
                students[sid]["roll"] = new_roll
                print("Roll updated successfully!")
            elif uchoice == 3:
                new_city = input("Enter new city: ")
                students[sid]["city"] = new_city
                print("City updated successfully!")
            elif uchoice == 4:
                print("No update done.")
            else:
                print("Invalid choice!")
        else:
            print("Student ID not found!")
    # Delete Student
    elif choice == 4:
        sid = int(input("Enter student ID: "))
        if sid in students:
            print("\nMatched student record:")
            print(students[sid])
            print("\nSelect an option to delete:")
            print("1. Delete Name")
            print("2. Delete Roll")
            print("3. Delete City")
            print("4. Delete Entire ID")
            print("5. Don't Delete")
            dchoice = int(input("Enter choice: "))
            if dchoice == 1:
                students[sid]["name"] = ""
                print("Name deleted!")
            elif dchoice == 2:
                students[sid]["roll"] = ""
                print("Roll deleted!")
            elif dchoice == 3:
                students[sid]["city"] = ""
                print("City deleted!")
            elif dchoice == 4:
                del students[sid]
                print("Student record deleted!")
            elif dchoice == 5:
                print("No deletion done.")
            else:
                print("Invalid choice!")
        else:
            print("Student ID not found!")
    # Exit
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")