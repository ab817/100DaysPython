#fibonacci series

a, b = 0, 1
n = 10

for i in range(n):
    print(b)
    a, b = b, a+b

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55