a = input("Введіть,будь ласка, кількість учнів в першій групі >> ")
a = int(a)
b = input("Введіть,будь ласка, кількість учнів в другій групі >> ")
b = int(b)
c = input("Введіть,будь ласка, кількість учнів в третій групі >> ")
c = int(c)
result1 = a//2 + (a - 2*(a//2))
result2 = b//2 + (b - 2*(b//2))
result3 = c//2 + (c - 2*(c//2))
print("Кількість столів, яку необхідно придбати дорівнює", result1 + result2 + result3)