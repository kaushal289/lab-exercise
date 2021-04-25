'''Qno3). Write a function called showNumbers that takes a parameter called limit.
 It should print all the numbers between 0and limit with a label to identify
  the even and odd numbers. For example, if the limit is 3, it should print:
* 0 EVEN
* 1 ODD
* 2 EVEN
'''
import math
num=int(input("enter a number"))
def find(num):
    for i in range(num):
        if i==0:
            print('0 is even.')
        elif i % 2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd.")
find(num)