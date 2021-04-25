'''Q.No.2 Write a function called fizz_buzz that takes a number.
if the number is divisible by 3, it should return"Fizz".
if it is divisible by 5, it should return "Buzz".
if it is divisible by both 3 and 5, it should retirn "FizzBuzz".
Otherwise, it should return the same number.
'''
def f_b(a):
    if (a%3==0 and a%5!=0):
        return 1
    elif (a%5==0 and a%3!=0):
        return 2
    elif (a%3 and a%5)==0:
        return 3
    else:
        return 4
a=int(input("enter any number"))
x=f_b(a)
if x==1:
    print("fizz")
elif (x==2):
    print("buzz")
elif (x==3):
    print("fizz buzz")
else:
    print("error")