import cmath
a, b, c = map(float, input().split())
d = (b**2)-4*a*c
if d < 0 :
    print("Complex Root")
elif d == 0 or d > 0:
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print(sol1, sol2)
    

