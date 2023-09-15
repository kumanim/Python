'''
Create dummy dictionary with scores
Print x has been awarded distinction class (if score is above 80)
Print x has been awarded first class if score is above 65 and below 80
Print x has just passed if score is below 65
'''
scores=[90,95,80,76,91,82]
for i in scores:
    if i > 80:
        print(i)
scores={'rohit':90, 'vishal':80, 'jack':76, 'jenny':82}
for i in scores:
    print(i, 'has scored', scores[i])

for student, score in scores.items():
    if score > 80:
        print(student, 'has been awarded distinction class')
    elif score > 65 and score <= 80:
        print(student, 'has been awarded first class')
    else:
        print(student,'has just passed')