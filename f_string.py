student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
max=0
top_student=""
for name,score in student_scores.items():
    if score>max:
        max=score
        top_student=name
print(f"{top_student} scored {max} with maximum marks in the class")