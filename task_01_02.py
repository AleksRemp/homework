plates = int(input())
fairy = float(input())

while (plates > 0) and (fairy > 0):
	fairy -= 0.5
	plates -= 1

if fairy > 0:
    print('Plates washed. We have ', fairy, 'fairy')	
elif plates > 0:
    print('Fairy was ended. We have ', plates, 'dirty plates')
else:
    print('All plates washed, fairy was ended')        