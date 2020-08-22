# ask the following inputs from the user
#  first name
#  last name
#  birth year
#  monthly salary
#  employment status
# store the inputs in a dictionary
# append the following information to the dictionary
#  compute their age based on bitrh year
#  Compute their annual salary
#  compute their payroll tax is given that the tax is 10% of the annual salary

# ask for up to three sets inputs
# store them in the list

import datetime
current_year = datetime.datetime.now()
    
employee_list = []
for index in range(3):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birth_year = int(input("Birth year: "))
    monthly_salary = int(input("Monthly salary: "))
    employment_status = input("Employment status: ")
    employee = {"First name": first_name, "Last name": last_name, "Birth year": birth_year,
                "Monthly salary": monthly_salary, "Employment status": employment_status}
    employee["Age"] = current_year.year - birth_year
    employee["Annual salary"] = monthly_salary * 12
    employee["Payroll tax"] = 0.1 * (monthly_salary * 12)
    employee_list.append(employee)

for employee_all_list in employee_list:
        print(employee_all_list)