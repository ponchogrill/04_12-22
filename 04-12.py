##import random
##def power_a3(a):
##    cube = a * a * a
##    return cube
##for i in range(5):
##    x = random.randint(-5,5)
##    print('x=' + str(x) + ' x^3=' + str(power_a3(x)))

##import random
##def power_a2(a):
##    kvad = a * a
##    return cube
##def power_a4(a):
##    fors = a * a * a * a
##    return cube
##for i in range(5):
##    x = random.randint(-5,5)
##    print('x=' + str(x) + ' x^2=' + str(power_a2(x)))
##    print('x=' + str(x) + ' x^4=' + str(power_a4(x)))
    
##import random
##import math
##from math import sqrt
##def a_mean(x,y):
##    aref = (x + y) / 2
##    return aref
##def g_mean(x,y):
##    geam = sqrt(x * y)
##    return geam
##for i in range(10):
##    x = random.randint(1,10)
##    y = random.randint(1,10)
##    print('x=' + str(x) + ' y= ' + str(y) + " среднее арефметическое = " + str(a_mean(x,y)))
##    print('x=' + str(x) + ' y= ' + str(y) + " среднее геометрическое = " + str(g_mean(x,y)))
    
import random
import math
from math import sqrt
def triangle_p(a):
    perim = 3 * a
    return perim
def triangle_s(a):
    plosh = (a * a * sqrt (3)) / 4
    return plosh
for i in range(1):
    a = int(input())
    print(' a= ' + str(a) + " периметр = " + str(triangle_p(a)))
    print(' a= ' + str(a) + " пдощадь = " + str(triangle_s(a)))
