f = open('StudentsPerformance.csv') 
males = 0
females = 0
for line in f:
    info = line.split(',')
    gender = info[0][1:-1]
    if gender == 'female':
        females += 1
    elif gender == 'male':
        males +=1
#print('Мальчиков: {}, девочек: {}'.format(males, females))


#Определение количества бакалавров

f = open('StudentsPerformance.csv')
bachelors = 0
for line in f:
    info = line.split(',')
    degree = info[2][1:-1]
    if degree == "bachelor's degree":
        bachelors += 1
#print('Из них бакалавров: {}'.format(bachelors))


#Количество вариантов в столбце "parental level of education"

f = open('StudentsPerformance.csv')
from collections import Counter
p_levels = []
for line in f:
    info = line.split(',')
    p_levels.append(info[2])
p_levels_count = len(Counter(p_levels).keys()) - 1
#print ('Количество вариантов в столбце "parental level of education" {}'.format(p_levels_count))


#Процент абитуриентов, полноценно пообедавших перед экзаменом

f = open('StudentsPerformance.csv')
all_lunches = 0
standard_lunches = 0
for line in f:
    info = line.split(',')
    lunch = info[3][1:-1]
    all_lunches += 1
    if lunch == "standard":
        standard_lunches += 1
i = standard_lunches/(all_lunches-1)*100
#print ("Процент абитуриентов, полноценно пообедавших перед экзаменом: {}".format(i))


#Количество абитуриентов, относящихся к этнической группе "group C"

f = open('StudentsPerformance.csv')
i = 0
for line in f:
    info = line.split(',')
    group = info[1][1:-1]
    if group == "group C":
        i += 1
#print ('Количество абитуриентов, относящихся к этнической группе "group C": {}'.format(i))


f = open('StudentsPerformance.csv')
groups_count = 0
from collections import Counter
groups = []
for line in f:
    info = line.split(',')
    groups.append(info[1])
groups_count = len(Counter(groups).keys()) - 1
#print ('Количество разных этнических групп в файле {}'.format(groups_count))


import re
pattern = re.compile('\d+')

exams = []
f = open('StudentsPerformance.csv')
