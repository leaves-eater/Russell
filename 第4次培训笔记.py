# import math
# n,m = map(int,input().split())
# math.pow(n,m)
# print(math.pow(n,m))


# def abs (s):
#     flat = 1
#     if s < 0:
#         flat = -1
#         return (s * flat)
#     else:
#         return s
# s = int(input())
# a = abs (s)
# print (a)

# def power(a):
#     return a * a
#
# def power2(a)
#
# a = int(input())
# print(power(a))

# def fact(a):
#     if a == 1:
#         return 1
#     else:
#         return a * fact(a - 1)
#
# a = int(input())
# ans = fact(a)
# print (ans)

def f(n):
    if n == 1 or n == 2:   #先写递归结束条件
        return 1
    i = f(n - 1) + f(n - 2)
    return i


n = int(input())
fb = f(n)
print(fb)