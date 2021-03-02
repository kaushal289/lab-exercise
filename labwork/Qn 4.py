''' 4 Given the integer N - the number of minutes that is passed science midnight - how many hours and
minutes are displayed on the 24h digital clock? The program should print two numbers: the number of
hours (between 0 and 23) and the number of minutes (between 0 and 59).
For example, if N=150, than 150 minutes have passed since midnight - i .e. now is 2:30 am.
So, the program should print 2:30.
'''
N=int(input('enter minutes passed since midnight:'))
hours=(N//60)
minutes=(N%60)
print("the hours is",hours)
print("the minut is",minutes)
print(f'its {hours}:{minutes} now')