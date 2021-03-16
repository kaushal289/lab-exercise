'''Write a python program to convert seconds to day,hours, minutes and seconds.'''
second=int(input("enter the second you like"))
minute=second//60
hours=minute//60
day=hours//24
print(f"The day is {day}.The hour is{hours}.The minute is {minute}.The second is {second}")