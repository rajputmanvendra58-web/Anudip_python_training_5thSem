# Student Performance Analytics System
"""
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary.
Example Structure students = {     
"S101": {"name": "Anuj", "marks": 85},     
"S102": {"name": "Rahul", "marks": 72} } 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
    o A (90+)  
    o B (75–89)  
    o C (50–74)  
    o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
    • Nested Dictionaries  
    • Dictionary Traversal  
    • Searching  
    • Aggregation  
    • Report Generation  
"""
# ==========================================================
# Student Performance Analytics System
# Function Free Program
# ==========================================================

# Dictionary to store student records

students = {}

# ==========================================================
# Input Details of 30 Students
# ==========================================================

print("Enter Details of 30 Students")

for i in range(30):

    print(f"\nStudent {i+1}")

    # Student ID Validation

    while True:

        sid = input("Enter Student ID (Example: S101): ").upper()

        if sid in students:
            print("Student ID already exists.")

        elif sid.startswith("S") and sid[1:].isdigit() and len(sid) == 4:
            break

        else:
            print("Invalid Student ID. Example: S101")

    # Student Name

    name = input("Enter Student Name: ")

    # Marks Validation

    while True:

        try:

            marks = float(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                break

            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Enter numeric marks only.")

    # Store Record

    students[sid] = {
        "name": name,
        "marks": marks
    }

print("\n30 Student Records Stored Successfully.")

# ==========================================================
# Menu Driven Program
# ==========================================================

while True:

    print("\n========== MENU ==========")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper and Lowest Scorer")
    print("7. Calculate Class Average")
    print("8. Count Pass and Fail Students")
    print("9. Generate Grades")
    print("10. Display Students Above Average")
    print("11. Display Top 5 Performers")
    print("12. Scholarship Students")
    print("13. Exit")

    choice = input("Enter Your Choice: ")

    # ======================================================
    # Display All Students
    # ======================================================

    if choice == "1":

        if len(students) == 0:

            print("No Records Found.")

        else:

            print("\nStudent Records")

            for sid, details in students.items():

                print("-" * 30)
                print("Student ID :", sid)
                print("Name       :", details["name"])
                print("Marks      :", details["marks"])

    # ======================================================
    # Search Student
    # ======================================================

    elif choice == "2":

        sid = input("Enter Student ID: ").upper()

        if sid in students:

            print("\nStudent Found")
            print("Name  :", students[sid]["name"])
            print("Marks :", students[sid]["marks"])

        else:

            print("Student ID not found.")

        # ======================================================
    # Add New Student
    # ======================================================

    elif choice == "3":

        sid = input("Enter Student ID: ").upper()

        if sid in students:

            print("Student ID already exists.")

        elif not (sid.startswith("S") and
                  sid[1:].isdigit() and
                  len(sid) == 4):

            print("Invalid Student ID.")

        else:

            name = input("Enter Student Name: ")

            try:

                marks = float(input("Enter Marks (0-100): "))

                if 0 <= marks <= 100:

                    students[sid] = {
                        "name": name,
                        "marks": marks
                    }

                    print("Student Added Successfully.")

                else:

                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Invalid Marks Input.")

    # ======================================================
    # Update Student Marks
    # ======================================================

    elif choice == "4":

        sid = input("Enter Student ID: ").upper()

        if sid not in students:

            print("Student ID not found.")

        else:

            try:

                marks = float(input("Enter New Marks: "))

                if 0 <= marks <= 100:

                    students[sid]["marks"] = marks

                    print("Marks Updated Successfully.")

                else:

                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Invalid Marks Input.")

    # ======================================================
    # Delete Student
    # ======================================================

    elif choice == "5":

        sid = input("Enter Student ID: ").upper()

        if sid in students:

            del students[sid]

            print("Student Deleted Successfully.")

        else:

            print("Student ID not found.")

    # ======================================================
    # Find Topper and Lowest Scorer
    # ======================================================

    elif choice == "6":

        topper = None
        lowest = None

        for sid in students:

            if topper is None:

                topper = sid
                lowest = sid

            if students[sid]["marks"] > students[topper]["marks"]:

                topper = sid

            if students[sid]["marks"] < students[lowest]["marks"]:

                lowest = sid

        print("\nTopper Details")
        print("Student ID :", topper)
        print("Name       :", students[topper]["name"])
        print("Marks      :", students[topper]["marks"])

        print("\nLowest Scorer Details")
        print("Student ID :", lowest)
        print("Name       :", students[lowest]["name"])
        print("Marks      :", students[lowest]["marks"])

    # ======================================================
    # Calculate Class Average
    # ======================================================

    elif choice == "7":

        total = 0

        for details in students.values():

            total += details["marks"]

        average = total / len(students)

        print(f"\nClass Average = {average:.2f}")

    # ======================================================
    # Count Pass and Fail Students
    # ======================================================

    elif choice == "8":

        passed = 0
        failed = 0

        for details in students.values():

            if details["marks"] >= 50:

                passed += 1

            else:

                failed += 1

        print("\nPassed Students :", passed)
        print("Failed Students :", failed)
        # ======================================================
    # Generate Grades
    # ======================================================

    elif choice == "9":

        print("\nStudent Grades")

        for sid, details in students.items():

            marks = details["marks"]

            if marks >= 90:

                grade = "A"

            elif marks >= 75:

                grade = "B"

            elif marks >= 50:

                grade = "C"

            else:

                grade = "F"

            print(
                sid,
                details["name"],
                "Marks =", marks,
                "Grade =", grade
            )

    # ======================================================
    # Display Students Above Average
    # ======================================================

    elif choice == "10":

        total = 0

        for details in students.values():

            total += details["marks"]

        average = total / len(students)

        print(f"\nClass Average = {average:.2f}")

        print("\nStudents Scoring Above Average")

        found = False

        for sid, details in students.items():

            if details["marks"] > average:

                print(
                    sid,
                    details["name"],
                    details["marks"]
                )

                found = True

        if found == False:

            print("No student found.")

    # ======================================================
    # Display Top 5 Performers
    # Without sorted() and sort()
    # ======================================================

    elif choice == "11":

        temp_students = students.copy()

        print("\nTop 5 Performers")

        count = 0

        while count < 5 and len(temp_students) > 0:

            topper = None

            for sid in temp_students:

                if topper is None:

                    topper = sid

                elif temp_students[sid]["marks"] > \
                     temp_students[topper]["marks"]:

                    topper = sid

            print(
                f"{count + 1}.",
                topper,
                temp_students[topper]["name"],
                temp_students[topper]["marks"]
            )

            del temp_students[topper]

            count += 1

    # ======================================================
    # Scholarship Students
    # Marks Greater Than 85
    # ======================================================

    elif choice == "12":

        scholarship = {}

        for sid, details in students.items():

            if details["marks"] > 85:

                scholarship[sid] = details

        print("\nScholarship Students")

        if len(scholarship) == 0:

            print("No Scholarship Students Found.")

        else:

            for sid, details in scholarship.items():

                print(
                    sid,
                    details["name"],
                    details["marks"]
                )

    # ======================================================
    # Exit Program
    # ======================================================

    elif choice == "13":

        print("\nProgram Terminated Successfully.")
        break

    # ======================================================
    # Invalid Choice
    # ======================================================

    else:

        print("Invalid Choice. Please Enter 1 to 13.")