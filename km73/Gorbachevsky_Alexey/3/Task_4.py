n = int(input("Введіть кількість студентів: "))
k = int(input("Введіть кількість яблук: "))

result = "Кількість яблук у студента: " + str(k//n) + "\nКількість яблук в кошику: " + str(k%n)

print(result)
