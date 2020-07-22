
def read_csv(file_name: str) -> str:
	ret = []

	with open(file_name,'r') as handle:
		for line in handle:
			if line.startswith("#"):
				header = line.strip().split(',')
				continue

			splitted = line.strip().split(',')
			d = dict(zip(header,splitted))
			ret.append(d)
	return ret

result = read_csv('read_sample.csv')

print(result)


