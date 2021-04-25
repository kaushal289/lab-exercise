'''Given a positive real number.print its fractional part.'''
import math
number=float(input('enter a real number'))
fraction=math.modf(number)
print(fraction)