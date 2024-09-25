"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_data = {"Student_name": "Vishnuteja",
                "age": 18,
                "roll_no": 74,
                "class": "2nd year DEEE",
                "section": "B",
                "percentage": 80.0,
                "college_name": "Nuzvid polytechnic collage"}
print(student_data["percentage"])

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
student_info = {"student_names": ("ravi", "sandeep", "shiva"),
                'ages': [20, 21, 20],
                "roll_nos": (74, 45, 69),
                "section": ['A', "B", "A"],
                "classes": ["2nd year EEE", "2nd year Mech", "2nd year ECE"],
                "percentages": [87.9, 78.0, 89.7],
                "university_names": ("YVU", "JNTUA", "JNTUK")}
print(student_info["classes"][-1])

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employe = {"Employe_1": {"employe_name": "suresh", "salary": 20000.0, "Designation": "Tester"},
           "Employe_2": {"employe_name": "Ganesh", "salary": 30000.0, "Designation": "Developer"},
           "Employe_3": {"employe_name": "sai", "salary": 26000.0, "Designation": "validation Engineer"}}
print(employe["Employe_3"]["Designation"])
