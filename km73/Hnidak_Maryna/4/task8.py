'''
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі
на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки.
Визначити, чи може король перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер
рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два
числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
'''
a = int(input("Введіть номер рядку, де розташуваний король - "))
b = int(input("Введіть номер стовпчика, де розташуваний король - "))
c = int(input("Введіть номер рядку,куди король повинен перейти - "))
d = int(input("Введіть номер стовпчика,куди король повинен перейти - "))
if (a<1 or a>8) or (b<1 or b>8) or (c<1 or c>8) or (d<1 or d>8):
    answer = "NO"
elif (abs(a-c)==1 and abs(b-d)==1) or (a==c and abs(b-d)==1) or (b==d and abs(a-c)==1):
    answer = "YES"
else:
    answer = "NO"
print (answer)