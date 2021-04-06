'''Weight conveter:
Input the weight of a person in either kg or lbs.
if the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.'''
weight=int(input('enter your weight:'))
system=input('is it in lbs or in kg:')
if  system=="kg":
    weight_kg=weight*1.5
    print(f'the weight in lbs is {weight_kg}lbs')
elif system=="lbs":
    weight_kg = weight / 1.5
    print(f'the weight in lbs is {weight_kg}kg')
else:
    print('enter correct system')

