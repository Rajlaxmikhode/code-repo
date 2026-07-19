employees = {
    "Alice": 45000,
    "Bob": 38000,
    "Charlie": 52000,
    "David": 47000
}

for key, value in employees.items():
    print(key,"-", value)

l=len(employees)
print(l)
salary_of_emp_above_avg = {}
max_salary = 0
max_salary_emp = ""
total = 0

for key, value in employees.items():
        if value > max_salary:
            max_salary = value
            max_salary_emp = key
       
print("Maximum salaried employee is ",max_salary_emp, max_salary)

#Average salary
for key, value in employees.items():
    total += value
    average_salary = total/l

print("average salary of employes is", average_salary)


#Employess whose salary is above average:
for key, value in employees.items():
    if value > average_salary:
        salary_of_emp_above_avg[key] = value
                
print("salary above avg ", salary_of_emp_above_avg)



    





    

