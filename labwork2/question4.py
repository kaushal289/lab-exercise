'''Given three integers, print the smallest one.(Three integers should be user input)'''
first_num=int(input('enter first number:'))
second_num=int(input('enter second number:'))
third_num=int(input('enter third number:'))
if first_num<second_num and first_num<third_num:
    print(f"{first_num} is the smallest than {second_num} and {third_num}")
elif second_num<first_num and second_num<third_num:
    print(f"{second_num} is the smallest than {first_num} and {third_num}")
else:
    print(f"{third_num} is the smallest {first_num} and {second_num}")