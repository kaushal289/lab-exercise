'''Given a three-digit number. Find the sum of its digits.'''
number=int(input('enter a number:'))
add=0
for i in range(3):
    rem=number%10
    n=number//10
    add=rem+add
    number=n
print(add)