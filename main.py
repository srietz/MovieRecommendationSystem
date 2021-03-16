






import Math
import ReadHelper

							
#print( 'Cosine Similarity Between User ' + str(u) + ' And User ' + str(i) + ' = ' + str(Math.cosSim(simTerms[1], simTerms[2])) ) 
#print('\nBetween User ' + str(u) + ' and ' + str(i) + ', both rated movies ')
#print(simTerms[0])
		
#	if len(simTerms[0]) != 0:
#	simTerms = similarTerms(trainingData[u],trainingData[i])
#if u != i:
		
#for i in range(0,len(trainingData)):
#print('---Cosine similarity between user 0 and all others')
#print('Average of (1,2,3) is ' + str(Math.average([1,2,3])))
#print('Dot product of (1,2,3) and (4,-5,6) is ' + str(Math.dotProduct([1,2,3],[4,-5,6])))
#print('Magnitude of (-7,2) is ' + str(Math.magnitude([-7,2])))
#u = 0
	
	
	

def similarTerms(VecA,VecB):
	movies = []
	newVecA = []
	newVecB = []
	for i in range(0,len(VecA)):
		if VecA[i] != 0 and VecB[i] != 0:
			movies.append(i)
			newVecA.append(VecA[i])
			newVecB.append(VecB[i])

	return [movies, newVecA, newVecB]
	
def kNearestNeighbors(user, k, trainingData):
	kNN = []
	for i in range(0,len(trainingData)):
		if i != user:
			print('Find Movies User ' + str(user) + ' And User ' + str(i) + ' Both Rated')
			simTerms = similarTerms(trainingData[user],trainingData[i])
			if len(simTerms[0]) != 0:
				print('\tSimilar Terms: ' + str(simTerms))
				similarity = Math.cosSim(simTerms[1], simTerms[2])
				print('\tCosine Similarity: ' + str(similarity))
				if len(kNN) < k:
					kNN.append([i, similarity])
				else:
					for value in kNN:
						print('Value: ' + str(value))
						if value[1] < similarity and value[0] != i:
							print('\tReplaced ' + str(value) + ' With User ' + str(i) + ',Similarity of ' + str(similarity))
							value[0] = i
							value[1] = similarity
							break
	return kNN

def pearson():
	pass

def main():
	print('Reading Training Data...')
	trainingData = ReadHelper.readDataIntoMatrix('train.txt')
	print('Done with read')

	print('kNN of User 0: ' + str(kNearestNeighbors(0, 6, trainingData)))

	return







main()