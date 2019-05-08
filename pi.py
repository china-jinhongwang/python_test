# 求解pi值
# 遭遇的问题：pow(16,1000)
# 1、“Numerical result out of range” 解决方案：将pow(16, 1000)赋值给一个变量a后，越界的float值，\
# 在赋值后自动存为界内的值。再参与下一步运算。
# 2、“OverflowError: Python int too large to convert to float” 解决方案：将int转换为float后运算

k = eval(input())
pi = 0
for i in range(k+1):
    a = 1/pow(16, i)
    print("{}:{}".format(i, a))
    pi += a * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
print("{:.8f}".format(pi))
