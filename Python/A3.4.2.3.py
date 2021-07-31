#Какой средний балл экзамене по чтению (reading score) получили девочки?
#Ответ округлите до трёх знаков после запятой. Используйте точку в качестве разделителя.


import re
pattern = re.compile('\d+')

exams = []
f = open('StudentsPerformance.csv')

girls_reading_scores = []
girls_avg_reading_score = 0
girls = 0
for line in f:
    info = line.split(',')
    if info == "'gender'":
        continue
    else:
        new_line = []
        for item in info:
            if pattern.search(item) != None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])
        exams.append(new_line)

