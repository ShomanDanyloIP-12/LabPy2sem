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
                l = pickle.load(file)
                for i in range(len(l)):
                    list_of_lines.append(l[i])
                print(list_of_lines)
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
            "To end the input | input ---> 'end'")
        line = input()
        while line:
            if line == "end":
                break
            list_of_lines.append(line)
            line = input()

        pickle.dump(list_of_lines, file)


def if_flow_already_exists(flow_list, flow):
    for i in range(len(flow_list)):
        if flow_list[i] == flow:
            return 1
    return 0


def min_marks(name):
    with open(name, 'rb') as fileif:
        students = pickle.load(fileif)
        flow_list = []
        students_with_min = []
        for i in range(len(students)):
            index = 0
            student = Student(students[i])
            flow = student.flow
            min = student.average
            if if_flow_already_exists(flow_list, flow) == 0:
                for j in range(len(students)):
                    student2 = Student(students[j])
                    if flow == student2.flow:
                        if min >= student2.average:
                            min = student2.average
                            index = j
                flow_list.append(flow)
                students_with_min.append(students[index])
    for i in range(len(students_with_min)):
        student = Student(students_with_min[i])
        print("Student with the smallest mark on the '" + str(student.flow) + "' flow: " +
              str(student.PIB) + " Group: " + str(student.group) + " Mark: " +
              str(student.average))


def new_list(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        strg = []
        bal = int(input("Enter min average mark: "))
        for i in range(len(temp)):
            stud = Student(temp[i])
            if stud.group // 10 == 4 and stud.edForm == "day" and stud.average >= bal:
                strg.append(temp[i])
        strg = sorted(strg, key=str.lower)
        with open("output_file.txt", 'wb') as fileof:
            pickle.dump(strg, fileof)


def print_students(st):
    stud = Student(st)
    print(stud.PIB, stud.birth, stud.flow + "-" + str(stud.group), stud.edForm, stud.average)


def output(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        for i in range(len(temp)):
            print_students(temp[i])
