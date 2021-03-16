def dotProduct(VecA, VecB):
	r_dot = 0
	for i in range(0,len(VecA)):
		r_dot += int(VecA[i])*int(VecB[i])
	return r_dot

def magnitude(Vec):
	#sum squares
	if len(Vec) != 0:
		sumSquares = 0
		for i in range(0,len(Vec)):
			sumSquares += Vec[i]**2
		#root sum
		return sumSquares**(1/2)

def vecMinusZeros(Vec):
	returnVec = []
	for value in Vec:
		if value != 0:
			returnVec.append(value)
	return returnVec

def average(Vec):
	sum = 0
	for i in range(0,len(Vec)):
		sum += Vec[i]
	return sum/len(Vec)

def weightedAverage(VecA, VecU):
	avgRatingOfUserA = average(vecMinusZeros(VecA))
	avgRatingOfUserU = average(vecMinusZeros(VecU))
	numerator, den1, den2 = 0
	for i in range(0,len(VecA)):
		numerator += (VecA[i]-avgRatingOfUserA)*(VecU[i]-avgRatingOfUserU)
		den1 += (VecA[i]-avgRatingOfUserA)**2
		den2 += (VecU[i]-avgRatingOfUserU)**2
	den1 = den1**(1/2)
	den2 = den2**(1/2)
	return numerator/(den1*den2)
	
def cosSim(VecA, VecB):
	return dotProduct(VecA,VecB)/(magnitude(VecA)*magnitude(VecB))