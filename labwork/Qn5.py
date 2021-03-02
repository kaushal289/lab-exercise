''' A school decided to replace the desks in three classroom. Each desk sits two students.
Given the number of students in each class. Print the smallest possible number of desks that can be
purchased.
The program should read three integers: the number of students in each of the three classes, a,b and c respectively.
 '''
first_class=int(input('enter the number of students in first class'))
second_class=int(input('enter the number of students in second class'))
third_class=int(input('enter the number of students in third class'))
'''Desk for first classroom'''
first_divider=first_class//2
first_remainder=first_class%2
'''Desk for second classroom'''
second_divider=second_class//2
second_remainder=second_class%2
'''Desk for third classroom'''
third_divider=third_class//2
third_remainder=third_class%2
desk_in_firstclass=first_divider+first_remainder
desk_in_secondtclass=second_divider+second_remainder
desk_in_thirdclass=third_divider+third_remainder
print('the no of deskes that should bought in first class=',desk_in_firstclass)
print('the no of deskes that should bought in second class=',desk_in_secondtclass)
print('the no of deskes that should bought in third class=',desk_in_thirdclass)