import numpy as np
x1=float(input())
y1=float(input())
z1=float(input())
x2=float(input())
y2=float(input())
z2=float(input())
x3=float(input())
y3=float(input())
z3=float(input())
d1=float(input())
d2=float(input())
d3=float(input())




a = array([[x1,y1,z1], [x2,y2,z2], [x3,y3,z3]])
b = array([d1,d2,d3])
x = np.solve(a, b)
print x
