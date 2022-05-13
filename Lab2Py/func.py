import pickle
from Structs import *


def set_name_of_file():
    name = input("Введите название файла: ")
    return name


def get_input(name):
    list_of_lines = []
    mode = input("Would you like to append your input?If so,enter 'a'.Otherwise enter 'w' ")
    while True:
        if mode == 'a':
            with open(name, 'rb') as file:
                pickle.load(file)
                break
        if mode == 'w':
            with open(name, 'wb') as file:
                file.truncate()
                break
        while mode != 'a' and mode != 'w':
            mode = input("Enter correct letter (a or w): ")
    with open(name, 'wb') as file:
        print(
            "Enter the student information as \n Surname Initials Day.Month.Year(of birth) Group-Flow EducationForm "
            "AverageGrade \n Example: Ivaniv I. I. 15.12.2003 IK-9 day 89 \n To end the line | press ---> ENTER\n "
            "To end the input | input ---> 'end'\n")
        line = input()
        while line:
            list_of_lines.append(line)
            line = input()
        pickle.dump(list_of_lines, file)


def min_marks(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        list_of_students = []
        for i in range(len(temp)):
            stud = Student(temp[i])
            list_of_students.append(stud)



def new_list(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        strg = []
        bal = input("Enter min average mark: ")
        for i in range(len(temp)):
            stud = Student(temp[i])
            if stud.group / 10 == 4 and stud.edForm == "day" and stud.average >= bal:
                strg.append(temp[i])
        strg = sorted(strg, key = str.lower)
        with open("output_file.txt", 'wb') as fileof:
            pickle.dump(strg, fileof)


def print_students(st):
    stud = Student(st)
    print(stud.PIB, " ", stud.birth, " ", stud.flow, "-", stud.group, " ", stud.edForm, " ", stud.average)


def output(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        for i in range(len(temp)):
            print_students(temp[i])