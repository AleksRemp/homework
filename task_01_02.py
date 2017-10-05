plates = int(input())
fairy = float(input())

while (plates > 0) and (fairy > 0):
	fairy -= 0.5
	plates -= 1

if fairy > 0:
    print('Все тарелки вымыты. Осталось ', fairy, 'ед. моющего средства')	
elif plates > 0:
    print('Моющее средство закончилось. Осталось ', plates, 'тарелок')
else:
    print('Все тарелки вымыты, моющее средство закончилось')        