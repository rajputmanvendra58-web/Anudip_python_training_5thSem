# Problem 2: Hospital Patient Record Management System 
"""
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt. 
"""
# Hospital Patient Record Management System

# List to store all patient records
patients = []

# -------------------------------
# Reading data from patients.txt
# -------------------------------
try:
    file = open("patients.txt", "r")

    for line in file:
        line = line.strip()  # Remove extra spaces/newline

        # Split data using comma
        patient_id, name, status = line.split(",")

        # Store record as a list
        patients.append([patient_id, name, status])

    file.close()

except FileNotFoundError:
    print("patients.txt file not found!")
    exit()

# -------------------------------
# Task 1 : Display All Records
# -------------------------------
print("\nALL PATIENT RECORDS")
print("-" * 30)

for patient in patients:
    print(f"ID: {patient[0]}, Name: {patient[1]}, Status: {patient[2]}")

# -------------------------------
# Task 2 : Display Critical Patients
# -------------------------------
print("\nCRITICAL PATIENTS")
print("-" * 30)

for patient in patients:
    if patient[2] == "Critical":
        print(patient[1])

# -------------------------------
# Task 3 : Count Patients by Status
# -------------------------------
normal_count = 0
stable_count = 0
critical_count = 0

for patient in patients:

    if patient[2] == "Normal":
        normal_count += 1

    elif patient[2] == "Stable":
        stable_count += 1

    elif patient[2] == "Critical":
        critical_count += 1

print("\nPATIENT COUNT")
print("-" * 30)
print("Normal :", normal_count)
print("Stable :", stable_count)
print("Critical :", critical_count)

# -------------------------------
# Task 4 : Search Patient by ID
# -------------------------------
search_id = input("\nEnter Patient ID to Search: ").upper()

found = False

for patient in patients:

    if patient[0] == search_id:

        print("\nPATIENT FOUND")
        print("-" * 30)
        print(f"ID     : {patient[0]}")
        print(f"Name   : {patient[1]}")
        print(f"Status : {patient[2]}")

        found = True
        break

if not found:
    print("Patient ID not found!")

# ------------------------------------------
# Task 5 : Save Critical Patients to File
# ------------------------------------------
file = open("critical_patients.txt", "w")

for patient in patients:

    if patient[2] == "Critical":
        file.write(f"{patient[0]},{patient[1]},{patient[2]}\n")

file.close()

print("\nCritical Patient Report Generated Successfully.")