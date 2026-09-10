import math

#переписываем функцию из задания
def f(x):
    return math.sqrt(2*x**2+1.2-math.cos(x))-1

l = 0
r = 1
e = 0.0001

def polovin(l, r, e): #метод половинчатого деления
    if f(l) * f(r) > 0:
        print('корня нет')
    else:
        while (r - l) > e:
            b = (l + r) / 2
            if f(l) * f(b) < 0: #проверка, в какой стороне находится корень
                r = b
            else:
                l = b
    return (r+l)/2

def hordy(l, r, e):
    while True:
        xk = l - (f(l) * (r - l)) / (f(r) - f(l))
        if f(xk) == 0 or abs(f(xk)) < e:
            break
        if f(xk) * f(r) > 0:
            r = xk
        else:
            l = xk
    return xk

print(polovin(l,r,e))
print(hordy(l,r,e))
