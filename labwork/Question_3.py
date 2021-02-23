'''N students takes K apples and distribute them among each other evenly. The remaning
(the undivisible) part remains in the basket.How many apples will each single students get?
 How many apples remain in the basket? The program reads the number N and K. It should print the two
   answers for the question above.'''
N=int(input('enter no of students'))
A=int(input('enter no of apples in total'))
D=(A//N)
R=(A%N)
print(f'each student got{D}')
print(f'the remaining apple are{R}')

