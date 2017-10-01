# сумма квадратов длин катетов равна квадрату длины гипотенузы
print('координаты первой вершины')
x1,y1 = int(input()), int(input())
print('координаты второй вершины')
x2,y2 = int(input()), int(input())
print('координаты третьей вершины')
x3,y3 = int(input()), int(input())

len_12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
len_13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
len_23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

s1 = len_12 ** 2
s2 = len_13 ** 2
s3 = len_23 ** 2

if (s1 + s2 == s3) or (s1 + s3 == s2) or (s2 + s3 == s1):
    print('Прямоугольный')
else:
    print('Не прямоугольный')