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


def osg2313():
    for student in data["student_data"]:
        if student.get("email") == "osg2313@kaist.ac.kr":
            print('========================================')
            print('osg2313 favorite_sport: ' + student["favorite_sport"])


osg2313()


def seokhan5464():
    for student in data["student_data"]:
        if student.get("email") == "seokhan5464@kaist.ac.kr":
            print('========================================')
            print('seokhan5464 hobby: ' + student["hobby"])


seokhan5464()

def javokhiraliev():
    for student in data["student_data"]:
        if student.get("email") == "javokhiraliev@kaist.ac.kr":
            print('====================================')
            print('javokhiraliev favorite sport: ' + student["favorite_sport"])

javokhiraliev()


def c_woozzai_13():
    for student in data["student_data"]:
        if student.get("email") == "c.woozzai_13@kaist.ac.kr":
            print("========================================")
            print("c.woozzai_13 favorite_food: " + student["favorite_food"])


c_woozzai_13()



def kcj06():
    for student in data["student_data"]:
        if student.get("email") == "kcj06@kaist.ac.kr":
            print("========================================")
            print("kcj06 favorite_food: " + student["favorite_food"])
            return


kcj06()

def hahan1kaist1mail():
    for student in data["student_data"]:
        if student.get("email") == "hahan1kaist1mail@kaist.ac.kr":
            print("========================================")
            print("hahan1kaist1mail's hobby: " + student["hobby"])
            return

hahan1kaist1mail()


def aitashina():
    for student in data["student_data"]:
        if student.get("email") == "aitashina@kaist.ac.kr":
            print("========================================")
            print("aitashina favorite food: " + student["favorite_food"])
            return


aitashina()
