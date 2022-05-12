def new_var():
    name = input()
    return name


def get_input(name):
    mode = 'r'
    while mode != 'q' and mode != 'w':
        mode = input("If you want to append ur input,press q.Otherwise press w")
        if mode == 'q':
            file = open(name, "a")
        if mode == 'w':
            file = open(name, "w")
        if (mode != 'q' and mode != 'w'):
            mode = input("Enter correct letter:")
    print("Enter text:\n Next line ---> press ENTER \n Close file ---> press Ctrl + X")
    while(1):
        line = input()
        if line == "end":
            break
        file.write(line + "\n")
    file.close()


def output(name):
    file = open(name,"r")
    print(file.read())
    file.close()


def get_list(name):
    file = open(name,"r")
    list = file.readlines()
    print(list)
    return list


def new_name_file2():
    print("Enter name of parni file: ")
    name1 = input()
    print("Enter name of neparni file: ")
    name2 = input()
    return name1, name2


def par_or_nep(list, n, name1, name2):
    lst_par = []
    lst_nep = []
    file1 = open(name1,"a")
    file2 = open(name2,"a")
    for i in range(n):
        if i % 2 == 1:
            line = "".join(list[i])
            file1.write(line)
        if i % 2 == 0:
            line = "".join(list[i])
            file2.write(line)
    file1.close()
    file2.close()


def output2(name1, name2):
    file1 = open(name1,"r")
    file2 = open(name2,"r")
    print("Parni lines:\n", file1.read())
    print("Neparni lines:\n", file2.read())
    file1.close()
    file2.close()


def sort(lst_nep, k, name2):
    file2 = open(name2,"w")
    sn = []
    for i in range(k):
        sn.append(lst_nep[i])
    sorted_nep = sorted(sn, key=str.lower)
    for i in range(k, len(lst_nep)):
        sorted_nep.append(lst_nep[i])
    for i in range(len(sorted_nep)):
        file2.write(sorted_nep[i])
    file2.close()