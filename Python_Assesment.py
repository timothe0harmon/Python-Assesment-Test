import csv
import json


"""
Creates initial Csv 
Loads employees.json data
Loops though and adds information of those with totp False value into variables 
Within same iteration create nested loop to search for duplicate email in engineering csv; if exist collect manager information in a variable.
Append previously created csv with all information stored in variable  
"""

f = open('Results.csv', 'w', newline='')
thewriter1 = csv.writer(f)
thewriter1.writerow(
    ["First name","Last name","Email",
     "Username","Manager","Job title"])

with open('employees.json') as employees:
    employees_data = json.load(employees)


for totp in employees_data:
    if totp["totp_enabled"] == False:
        first_name=totp["firstName"]
        last_name =totp["lastName"]
        email_emply=totp["email"]
        username=totp["username"]
        job_title = totp["jobTitle"]

        with open('engineering.csv') as engineering:
            engineering_csv = csv.reader(engineering, delimiter=",")
            for row in engineering_csv:
                if email_emply == row[2]:
                    manager=row[3]
                    f = open('Results.csv', 'a+', newline='')
                    thewriter1 = csv.writer(f)
                    thewriter1.writerow(
                        [first_name,last_name,email_emply,
                         username,manager,job_title])
                    f.close()



