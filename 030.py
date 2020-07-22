
Seq = "AGTTTATAG"

for i in range(len(Seq)):
	if Seq[i:i+2] == 'TT':
		print(i)

