students = {}

f = open('StudentsPerformance.csv')

for line in f:
	info = line.split(',')
	if info[0] == "'gender'":
		continue
    else:
     	lunche = info[3][1:-1]
		gender = info[0][1:-1]
		test_prep_course = info[4][1:-1]
		if gender in students:
			if test_prep_course in students[gender]:
				students[gender][test_prep_course] += 1
			else:
				students[gender][test_prep_course] = 1
		else:
			students[gender]={}
			students[gender][test_prep_course] = 1
#print (students)

for line in f:
    	info = line.split(',')
	if info[0] == "'gender'":
		continue
	else:
		gender = info[0][1:-1]
		prntal_lvl_edu = info[2][1:-1]
		if prntal_lvl_edu in students[gender]:
			students[gender][prntal_lvl_edu] += 1
		else:
			students[gender][prntal_lvl_edu] = 1
		
print (students)