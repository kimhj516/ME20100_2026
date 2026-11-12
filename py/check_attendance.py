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


def limgaram0831():
    for each_student_data in data["student_data"]:
        if each_student_data["name"] == "Garam Lim":
            print('========================================')
            print('limgaram0831 hobby: ' + each_student_data["hobby"])


limgaram0831()
def enkhtur_munkh_erdene():
    for student in data["student_data"]:
        if student.get("email") == "enkhtur.munkh-erdene@kaist.ac.kr":
            print("========================================")
            print("Enkhtur Munkh-erdene hobby: " + student["hobby"])
            return


enkhtur_munkh_erdene()


def azizbekalijonov():
    for student in data["student_data"]:
        if student.get("email") == "azizbekalijonov@kaist.ac.kr":
            print('========================================')
            print('azizbekalijonov hobby: ' + student["hobby"])


azizbekalijonov()


def seyun003():
    for student in data["student_data"]:
        if student.get("email") == "seyun003@kaist.ac.kr":
            print('========================================')
            print('seyun003 hobby: ' + student["hobby"])


seyun003()


def kimyejun0113():
    for student in data["student_data"]:
        if student.get("email") == "kimyejun0113@kaist.ac.kr":
            print('========================================')
            print('kimyejun0113 favorite_programming_language: ' + student["favorite_programming_language"])


kimyejun0113()


def joshualisky():
    for student in data["student_data"]:
        if student.get("email") == "joshualisky@kaist.ac.kr":
            print('========================================')
            print('joshualisky favorite_food: ' + student["favorite_food"])


joshualisky()
