n = input()
num = input()
for i in range(0, len(num)):
    if ord(num[i]) + int(n) > ord('z'):      #如果int('n')则是n的阿斯克码值
        a = ord(num[i]) + int(n - 26)
    else:
        a = ord(num[i]) + int(n)
    # ord(n)
    # a-z-a a-b 1 b-c 1
    print(chr(a))