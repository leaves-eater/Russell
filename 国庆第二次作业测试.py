# a, b, c = map(int,input().split())
# d = (a+b)*c
# print(d)

#商取整，求余数
# a, b = map(int,input().split())
# c = int(a / b)
# d = a % b
# print(c,d)

#保留几位小数
# a , b = map (int,input().split())
# c = a / b
# print(round(c,9))

#elif的用法
# a, b, c = map(int,input().split())
# if a < 60 and b >= 60 and c >= 60:
#     print(1)
# elif a >= 60 and b < 60 and c >= 60:
#     print(1)
# elif a >= 60 and b >= 60 and c < 60:
#     print(1)
# else:
#     print (0)

#一元二次方程求解
a,b,c = map(float,input().split())
if b**2 - 4 * a *c < 0:
    print("No answer!")
elif b**2 - 4*a *c == 0:
    x1 = - b / (2 * a)
    print("x1=x2={:.5f}".format(x1))
elif b**2 - 4*a *c > 0:
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    if x1 < x2:
        print ("x1=%.5f x2=%.5f" % (x1,x2))
    else :
        print ("x1=%.5f x2=%.5f" % (x2,x1))

