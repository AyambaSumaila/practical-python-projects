def square(x):
    y=x*x
    return y

def sum_of_squares(x, y, z):
    a=square(x)
    b=square(y)
    c=square(z)
    return a+b+c
a=4
b=5
c=2

result=sum_of_squares(a, b, c)
print(result)