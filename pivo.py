import sys

num = int(sys.argv[1])

pivo_l = []

for n in range(num):
	if n = 1:
		pivo_l.append(0)
	elif n = 2:
		pivo_l.append(1)
	elif n >= 3
		for i in range(n-2):
			nth = pivo_l[-1] + pivo_l[-2]
			pivo_l.append(nth)

print(pivo_l[-1])

	
