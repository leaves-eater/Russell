# n = int(input())
# k = 11 + 3 * n
# s = 5 * n
# if(k < s):
#     print("Luogu")
# else:
#     print("Local")

# my_str = input()
# my_str1 = my_str[::-1]
# print(my_str1, end = ' ')

# slist = [x for x in input().split()]
# my_list = list(reversed(slist))
# print(my_list)

# m , h = map(float,input().split())
# k = m / h ** 2
# if(k < 18.5):
#     print("Underweight")
# elif(18.5 <= k < 24):
#     print("Normal")
# elif(k > 24):
#     k = round(k , 6)
#     print("%.6g" %k)
#     print("Overweight")

# p = float(input())
#
# q = int(p * 10)
#
# a = q // 1000
#
# b = q // 100 % 10
#
# c = q // 10 % 10
#
# d = q % 10
#
# print("%d" % d, end='.')
# print(c, end='')
# print(b, end='')
# print(a, end='')

# K = int(input())
# n = 1.0
# count = 0.0
# while(1):
#     count += 1 / n
#     if(count > K):
#         print(int(n))
#         break
#     n += 1.0

my_str = input()
k = 0
for s in my_str:
    if(s == 'a' or s == 'd' or s == 'g' or s == 'j' or s =='m' or s == 'p' or s == 't' or s == 'w'):
        k += 1
    elif(s == 'b' or s == 'e' or s == 'h' or s == 'k' or s == 'n'or s == 'q' or s == 'u' or s == 'x'):
        k += 2
    elif(s == 'c' or s == 'f' or s == 'i' or s == 'l' or s == 'o' or s == 'r' or s == 'v' or s == 'y'):
        k += 3
    elif(s =='s' or s == 'z'):
        k += 4
    elif(s == ' '):
        k += 1
print(k)

