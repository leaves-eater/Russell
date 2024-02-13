#a, b = map(int, input().split())
#print(a * b)

#t, n = map(float, input().split())
#a = t / n
#print("%.3f" % a)
#print(int(2 * n))


#A = int(input())
    #if 0 < A < 100
        #print(A)
            #else:
            #print ("错误")
# num = input()   #数组
# sec = num.split(' ')
# final = float(sec[0])*0.2+float(sec[1])*0.3+float(sec[2])*0.5

# A, B, C = map(int, input().split())
# D = A * 0.2 + B * 0.3 + C * 0.5
# print(D)     #输出为浮点型

#s, v = map (float,input().split())
#d = s % v % 60
#if 7 - d > 0 and  s / v - 60 * d < 50:
#    print(7 - d , ":" , 50 - s / v - 60 * d)
#elif 7 - d < 0 and s / v - 60 * d < 50:
 #   print(24 + 7 - d , ":" , 50 - s / v - 60 * d)
#elif 7 - d > 0 and s / v - 60 * d > 50:
#    print(7 - d - 1 , ":" , 50 - s / v - 60 * d)
#elif 7 - d < 0 and s / v - 60 * d > 50:
 #   print(24 + 7 - d - 1 , ':' , s / v - 60 * d)

#a, b=map (float, input().split())
#c = (a * 10 + b) / 19
#print(int(c))

#a, b ,c=map(float,input().split())
#p = 0.5 * (a + b + c)
#s = (p * (p - a) * (p - b) * (p -c))**0.5
#print("%.1f" % s)

s, v = map (int,input().split())
t = s / v + 10
h = (24 * 60 + (60 * 8 - t)) % (24 * 60)
H = h // 60
m = h -(H * 60)
print("%02d:%02d"%(H,m))


