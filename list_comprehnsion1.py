#list comphrension: Find the student with second highest  grade 
students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

grades = [student[1] for student in students]

grades = sorted(set(grades))   # Remove duplicates and sort

second = grades[1]

names = []

for student in students:
    if student[1] == second:
        names.append(student[0])

names.sort()

for name in names:
    print(name)