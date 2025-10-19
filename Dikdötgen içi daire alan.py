p = 3
x =float(input("Dikdörtgen kısa kenarı için bir sayı giriniz:"))
y =float(input("Dikdörgenin uzun kenarı için bir sayı giriniz:"))
while x>=y :
    y += 1
else :
    m=x*y
    print(m)


z =float(input("Dairenin yarıçapı için bir sayı giriniz:"))
while 2*z>=x:
     z-= 0.5
else :
    n=2*z*p
    print(n)
print(m-n)