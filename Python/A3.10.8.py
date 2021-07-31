# Задание 3.10.8
# Какой средний балл, полученный мальчиками на экзамене по чтению? Ответ округлите до трёх цифр после разделителя. В качестве разделителя используйте точку.

# students = {}
# score_sum = 0
# males = 0

# f = open('StudentsPerformance.csv')

# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         if info[0] == '"male"':
#             score_sum += int(info [-2][1:-1])
#             males += 1
# print (score_sum/males)


# Задание 3.10.9
# Какой средний балл на экзамене по чтению набрали ученики, набравшие максимальный балл на экзамене по математике? Ответ округлите до трёх цифр после разделителя. В качестве разделителя используйте точку.


# max_math_score = 0
# f = open('StudentsPerformance.csv') # Загружаем читаемый файл
# math_score = []
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         math_score.append(int(info[-3][1:-1]))
# max_math_score = max(math_score)

# f = open('StudentsPerformance.csv')
# students = 0
# reading_score = 0
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         if int(info[-3][1:-1]) == max_math_score:
#             students += 1
#             reading_score += int(info[-2][1:-1])
# print (reading_score/students)


# Задание 3.10.10
# Какой средний балл на экзамене по письму набрали ученики, которые плохо пообедали перед экзаменом (lunch = free/reduced)? Ответ округлите до двух цифр после разделителя. В качестве разделителя используйте точку.

f = open('StudentsPerformance.csv')
num = 0
lunches_and_scores = []
students = {}
for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        lunches_and_scores = []
        lunches_and_scores.append(info[3])
        lunches_and_scores.append(int(info[-1][1:-2]))
        students[num] = lunches_and_scores
        num += 1
num = 1
score = 0
st_count = 0
for num in students:
    if students[num][0] == '"free/reduced"':
        score += students[num][1]
        st_count += 1
    else:
        continue
print (score/st_count)
print (num)
