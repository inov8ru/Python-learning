students = {}

f = open('StudentsPerformance.csv')



#print (students)

parental_level_of_education = {}
for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        prntl_edu_lvl = info [2][1:-1]
        gender = info [0][1:-1]
        if gender in students:
            if prntl_edu_lvl in students[gender]:
                students[gender][prntl_edu_lvl] += 1
            else:
                students[gender][prntl_edu_lvl] = 1
        else:
            students[gender] = {}
            students[gender][prntl_edu_lvl] = 1
#print (students)

f = open('StudentsPerformance.csv')
for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        parents = info[2][1:-1]
        if ethnicity in students:
            if parents in students[ethnicity]:
                students[ethnicity][parents] += 1
            else:
                students[ethnicity][parents] = 1
        else:
            students[ethnicity] = {}
            students[ethnicity][parents] = 1 
print (students)

