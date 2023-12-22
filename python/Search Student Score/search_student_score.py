import csv
import os


# dictionaries to store student data
all_students = {}
high_score_students = {}
low_score_students = {}

# read the CSV file
with open(r'C:\Users\Dell\OneDrive\Desktop\hw\hw3\students.csv', mode='r') as file:
    dict_file = csv.DictReader(file)
    for item in dict_file:
        keys = item['Name']
        values = int(item['Score'])  # Convert the 'Score' value to an integer

        # Dictionary of all students
        all_students[keys] = values

        # check score range high and low
        if 17 <= values <= 20:
            high_score_students[keys] = values
        elif 0 <= values <= 10:
            low_score_students[keys] = values


# function to search for students
def search_student_score(student_name):
    if student_name in all_students:
        score = all_students[student_name]
        if student_name in high_score_students:
            return f"{student_name} scored {score}. Great job!"
        elif student_name in low_score_students:
            return f"{student_name} scored {score}. You can do better."
        else:
            return f"{student_name} scored {score}."
    else:
        return f"Student {student_name} not found."

print(all_students)
student_name = input("Please enter the student's name: ")
output_search = search_student_score(student_name)
print(output_search)
try:
    print("location file ", os.getcwd())
except OSError:
    print("ERROR!!! Cannot get location")
except NameError:
    print("ERROR!!! Name is not defined")


