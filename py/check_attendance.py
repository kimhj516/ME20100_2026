import json


with open('student_data.json', 'r') as file:
    data = json.load(file)

for each_student_data in data["student_data"]:
    print('========================================')
    for key, value in each_student_data.items():
        print(str(key) + ': ' + str(value))


def khs8170():
    for each_student_data in data["student_data"]:
        if each_student_data["name"] == "Hyeonsu Kim":
            print('========================================')
            print('khs8170 favorite_restaurant: ' + each_student_data["favorite_restaurant"])
            print('khs8170 Hobby: ' + each_student_data["Hobby"])


khs8170()
