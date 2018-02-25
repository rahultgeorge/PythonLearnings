if __name__ == '__main__':
    studentsMarks=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentsMarks.append([])
        studentsMarks[len(studentsMarks)-1].append(name);
        studentsMarks[len(studentsMarks)-1].append(score); 
    studentsMarks.sort(key=lambda item:item[1])
    Marks=set(student[1] for student in studentsMarks)
    Marks=list(Marks)
    Marks.sort()
    students=[students[0] for students in studentsMarks if students[1]==Marks[1]]
    students.sort()
    for student in students:
        print(str(student))