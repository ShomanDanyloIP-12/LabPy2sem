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