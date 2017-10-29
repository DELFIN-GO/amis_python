'''
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
'''
a = int(input("Введіть номер рядку, де розташувана 1 клітинка - "))
b = int(input("Введіть номер стовпчика, де розташувана 1 клітинка - "))
c = int(input("Введіть номер рядку,де розташувана 2 клітинка - "))
d = int(input("Введіть номер стовпчика,де розташувана 2 клітинка - "))
if (a<1 or a>8) or (b<1 or b>8) or (c<1 or c>8) or (d<1 or d>8):
    answer = "NO"
elif ((b-d)%2==0 and (a-c)%2==0) or ((a-c)%2==1 and (b-d)%2==1):
    answer ="YES"
else:
    answer = "NO"
print(answer)
   
