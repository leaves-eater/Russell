# print("1 + 1 = " , 1 + 1)
# print("11 // 2 = " , 11 // 2)  #取整除，即结果有小数的话去掉
# print("4 / 2 = " , 4 / 2)      #两个int相除，得到float
# name = "黑马程序员"
# print("黑马程序员")
# print(name)
# num = 11.345
# print("num = %.2f" % num)
# # 快速格式化表达式
# print(f"我是：{name}")

# 递归
n = int(input())
def fact(n):

    if n == 0:
        return 1
    return 1.2 * fact(n - 1)

over = 19.99 * fact(n)
print("%.2f" % over)

