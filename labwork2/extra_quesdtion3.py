'''If name is less than 3 characters long- name must be at least 3 characters otherwise if it's more than
50 characters-name must maximum of 50 characters otherwise-name looks good!'''
name=input("enter name:")
character_length= len(name)
if character_length<=3:
    print('name must be at least 3 characters')
elif character_length>=3 and character_length<=50 :
    print(f'looks good. your name is{name}')
else:
    print('name must maximum of 50 characters')
