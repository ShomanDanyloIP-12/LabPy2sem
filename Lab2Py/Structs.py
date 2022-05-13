class Student():
    PIB = None
    birth = None
    flow = None
    group = None
    edForm = None
    average = None

    def __init__(self, line):
        parts = line.split(" ")
        self.PIB = parts[0] + " " + parts[1] + " " + parts[2]
        self.birth = parts[3]
        self.flow = (parts[4].split('-')[0])
        self.group = (parts[4].split('-')[1])
        self.edForm = parts[5]
        self.average = int(parts[6])
