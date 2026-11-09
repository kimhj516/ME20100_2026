import json


with open('student_data.json', 'r') as file:
    data = json.load(file)

for each_student_data in data["student_data"]:
    print('========================================')
    for key, value in each_student_data.items():
        print(str(key) + ': ' + str(value))
