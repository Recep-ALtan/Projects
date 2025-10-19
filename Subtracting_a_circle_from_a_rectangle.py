p = 3
x =float(input("Enter a number for the shortest side of the rectangle:"))
y =float(input("Enter a number for the longest side of the rectangle:"))
while x>=y :
    y += 1
else :
    m=x*y
    print(m)


z =float(input("Enter a number for the radius of the circle:"))
while 2*z>=x:
     z-= 0.5
else :
    n=2*z*p
    print(n)
print(m-n)

