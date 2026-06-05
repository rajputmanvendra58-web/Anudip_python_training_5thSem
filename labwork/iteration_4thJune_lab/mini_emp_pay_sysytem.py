# Mini Employee Payroll System

# Taking employee name as input
employee_name = input("Enter Employee Name: ")

# Taking basic salary as input
basic_salary = float(input("Enter Basic Salary: "))

# Calculating HRA (House Rent Allowance) as 20% of basic salary
hra = basic_salary * 0.20

# Calculating DA (Dearness Allowance) as 10% of basic salary
da = basic_salary * 0.10

# Calculating PF (Provident Fund) deduction as 12% of basic salary
pf = basic_salary * 0.12

# Calculating Gross Salary
# Gross Salary = Basic Salary + HRA + DA
gross_salary = basic_salary + hra + da

# Calculating Net Salary
# Net Salary = Gross Salary - PF Deduction
net_salary = gross_salary - pf

# Determining employee grade based on Net Salary
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Displaying payroll details
print("\n========== Employee Payroll Details ==========")
print("Employee Name :", employee_name)
print("Basic Salary  :", basic_salary)
print("HRA (20%)     :", hra)
print("DA (10%)      :", da)
print("PF (12%)      :", pf)
print("Gross Salary  :", gross_salary)
print("Net Salary    :", net_salary)
print("Grade         :", grade)