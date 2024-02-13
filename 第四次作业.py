#import sfji
#list_example = [int(x) for x in input().split()]
# print(list_example )
#for item in list_example:
#    print(item)

# list = [int(x) for x in input().split()]
# for item in list:
#      print ("item", '=', list[0])     #按照循环的形式先给item赋第一个值，然后输出，再赋第二个值
#      print ("max", '=',item)

#输出列表中最大值
# n = input()
# k = 1
# list = [int (x) for x in input().split()]
# max = list[0]
# for item in list:     #构造一个循环
#     if max <= list[k]:      #list[k]表示第k+1个数
#        max = list[k]
#     k = k + 1
#     if int(k + 1) > int(n):    #两个字符比较大小，虽然字符赋了值，但还是要标明类型
#         break
# print(max)

#求阶乘之和
# d = input()
# fact = 1
# sum = 0
# for item in range(1,int(d) + 1):   #右边的数不能取到
#     for i in range(int(item),int(item) + 1):
#         fact *= int(i)
#         sum += int(fact)
# print(sum)

# n = input()
# print (n)
# print (type(n))

# list = []
# list = input().split
# print(list)

# a , b = map(int,input().split())   #减法运算
# c = a - b
# print(c)

# 输出列表最大值和最小值
# list  = [int(x) for x in input().split()]
# print(max(list))
# print(min(list))

#输出小数点后3位,并且是四舍五入
# x = 8.98978
# print('%.3f' % x)

# n = int(input())
# list = [int(x) for x in input().split()]
# print(min(list))

#阶乘之和
# k = 1
# s = 0
# n = int(input())
# for x in range(1 , n+1):
#     for i in range(1 , x+1):
#         k *= i
#     s += k
#     k = 1
# print(s)

#利用ascill码实现字符间的变换
# n = int(input())
# my_str = input()
# s_str = ""    #如果是字符串的话，不需要定义array
# k = n % 26
# for x in my_str:
#     if(ord(x) + n <= 122):
#         s_str += chr(ord(x) + n)
#     else:
#         s_str += chr(ord(x) - (26 - n))
# print(s_str)

#倒序输出列表
#my_list = [int(x) for x in input().split()]

#用reversed函数
#a = list(reversed(my_list))

#切片方法
#a = my_list[::-1]
#for i in a:
#    print(i)

#永久倒序
# my_list.reverse()
# print(my_list)

#判断偶数
# my_list = []
# list = [1 , 2 ,3 , 4 , 5 , 6 , 7 ,8 ,9 , 10]
# a = len(list)
# i = 0
# while i < a:
#     k = list[i] % 2
#     if(k == 0):
#         my_list.append(list[i])
#     i += 1
# print(my_list)

#切片的运用
my_str = "万过月薪，员序程马黑来，nohtyp学"
result = my_str[5:10][::-1]   #前面表示从哪里到哪里，不包括右边；后面表示步长，负数表示倒序
print(result)
#法二
result1 = my_str.split("，")[1].replace("来","")[::-1]
print(f"法二结果：{result1}")