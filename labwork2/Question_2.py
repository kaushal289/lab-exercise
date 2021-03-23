'''2. WAP which accepts marks of four subjects and display total marks, percentage and garde.
Hint: more than 70% => distinction, more than 60% => first, more than 40%=> pass less than 40%=> fail'''
math=int(input('enter marks of math:'))
science=int(input('enter marks of science:'))
computer=int(input('enter marks of computer:'))
nepali=int(input('enter marks of nepali:'))
total_marks=math+science+computer+nepali
percent=(total_marks/400)*100
#for grade
print(f"total marks = {total_marks}")
print(f"percent = {percent}%")
if percent >=70:
    print('distinction')
elif percent<=70 and percent >=60:
    print('first')
elif percent<=60 and percent >=40:
    print('pass')
else:
    print('fail')

