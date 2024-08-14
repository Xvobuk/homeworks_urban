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

#Я попросил ChatGPT дописать ещё учеников и их оценки и запихнул это всё в отдельный файл, чтобы тут не мусорить.