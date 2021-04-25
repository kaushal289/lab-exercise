#Q.No.1 Write a Python function to find the Max of three numbers.
a = input('enter first num:')
b = input('enter second num')
c = input('enter third num')
def greater(a,b,c):
    if a>b or a>c:
        print(f"{a} is greater.")
    elif b>a or b>c:
        print(f"{b} is greater.")
    else:
        print(f"{c} is greater.")
greater(a,b,c)

