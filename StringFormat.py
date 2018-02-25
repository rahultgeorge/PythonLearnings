if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks=student_marks.get(query_name)
    query_marks=("{0:.2f}".format((query_marks[0]+query_marks[1]+query_marks[2])/3))
    print(query_marks)