import re
pattern = re.compile('\d+')

exams = []
f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        new_line = []
        for item in info:
            if pattern.search(item) != None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])
        exams.append(new_line)


#А3.4.2.1 Задание 1
#Вычислите средний балл абитуриентов на экзамене по чтению (reading score).

#Введите ответ в виде одного числа. Не округляйте полученное значение.

reading_scores1 = 0
reading_scores2 = []
avg_reading_score = 0
abithurients_count=0
for line in exams:
    reading_scores1 += (line[6])
    reading_scores2.append(line[6])
    abithurients_count += 1
#print (reading_scores1, sum (reading_scores2), abithurients_count)
avg_reading_score = reading_scores1/abithurients_count
#print (avg_reading_score)


#А3.4.2.2 Задание 2
#Сколько абитуриентов получили на экзамене по чтению (reading score) оценку ниже среднего?
#Введите количество абитуриентов в окно для ответа.

abithurients_count = 0
for line in exams:
    if line[6] < avg_reading_score:
        abithurients_count += 1
print ('{} абитуриентов получили на экзамене по чтению (reading score) оценку ниже среднего'.format(abithurients_count))


#А3.4.2.3 Задание 3
#Какой средний балл экзамене по чтению (reading score) получили девочки?
#Ответ округлите до трёх знаков после запятой. Используйте точку в качестве разделителя.

girls_reading_scores = []
girls_avg_reading_score = 0
for line in exams:
    if line[0] == 'female':
        girls_reading_scores.append(line[6])
girls_avg_reading_score = (sum(girls_reading_scores))/len(girls_reading_scores)
print ('Девочки на экзамене по чтению получили средний бал {}'.format(girls_avg_reading_score))



#А3.4.2.4 Задание 4
#Сколько абитуриентов получили на экзамене по письму (writing score) оценку выше 90?
#Введите количество абитуриентов в окно для ответа.

abithurients_count = 0
for line in exams:
    if line[7] > 90:
        abithurients_count += 1
print ('{} абитуриентов получили на экзамене по письму (writing score) оценку выше 90'.format(abithurients_count))


#А3.4.2.5 Задание 5
#Сколько процентов абитуриентов, получивших на экзамене по письму (writing score) оценку более 90, хорошо пообедали перед экзаменом (lunch = standard)?
#Ответ округлите до одного знака после запятой и введите без знака процента.

high_level_abithurients_count = 0

standard_lunches = 0
for line in exams:
    if line [3] == 'standard' and line [7] > 90:
        high_level_abithurients_count += 1
print ('{} процентов абитуриентов получили на экзамене по письму (writing score) оценку более 90 и хорошо пообедали перед экзаменом (lunch = standard)'.format(high_level_abithurients_count/abithurients_count*100))
