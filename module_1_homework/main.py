import marks

dict = {}
counter = 0
grades = marks.grades
students = list(marks.students)

for person in students:
    dict.update({person:(sum(grades[counter])/len(grades[counter]))})
    counter += 1
counter = 0
print(dict)