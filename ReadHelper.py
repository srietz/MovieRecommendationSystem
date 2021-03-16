def readDataIntoMatrix(fileName):
	f = open(fileName, 'r')
	i = 0
	data = []
	for line in f.readlines():
		j = 0
		row = []
		values = line.split()
		for value in values:
			row.append(int(value))
			j += 1
		data.append(row)
		i += 1
	return data