from PIL import Image


def mode(s):
	ans = s[0]
	for x in s:
		if (s.count(x) > s.count(ans)):
			ans = x
	return ans


def find_pos_min(d):
	ans = 0
	for x in range(0,len(d)):
		if (d[x] < d[ans]):
			ans = x
			
	return ans


def findPosKlowest(distances,a):
	Klowest = []
	distancesCopy = distances[:]
	for i in range(0,a):
		Klowest.append(find_pos_min(distancesCopy))
		distancesCopy[find_pos_min(distancesCopy)] = 1025
		
	return Klowest



def createData(filename):

	fr = open(filename)

	listOfLines = fr.readlines()
	print len(listOfLines)

	mydata = []

	for x in xrange(0,len(listOfLines)-32,33):
		myInstance = []
		for i in range(x,x+33):
			myLine = listOfLines[i]
			myLine.strip()
			myCharacters = myLine[0:32]
			for j in myCharacters:
				myInstance.append(j)
			
		myInstance.append(listOfLines[x+32].strip()[0])
	
		mydata.append(myInstance)
	
	for x in mydata:
		del x[1026]
		del x[1025]
		del x[1024]
		
	return mydata
	
def createTestVector(filename):

	fr = open(filename)

	listOfLines = fr.readlines()
	
	myInstance = []
	
	for x in listOfLines:
		myLine = x.strip()
		for i in myLine:
			myInstance.append(i)
			
	return myInstance
	

def classifyUsingKNN(trainData,testVector,k):
	myDistances = []
	for x in trainData:
		sumOfSquares = 0
		for i in range(0,1024):
			sumOfSquares = sumOfSquares + (float(x[i]) - float(testVector[i]))**2
			
		myDistances.append(sumOfSquares**0.5)
		
	myIndices = findPosKlowest(myDistances,k) 
	
	myTargets = [trainData[j][1024] for j in myIndices]
	
	myans = mode(myTargets)
	
	return myans
	
def prepareImageToVector(filename):

	im = Image.open(filename,'r')
	im = im.convert('1')
	mypixels = list(im.getdata())
	for x in range(0,len(mypixels)):
		if (mypixels[x] == 255):
			mypixels[x] = '1'
			
		else:
			mypixels[x] = '0'
			
	return mypixels
	
def printString(s):
	for x in range(0,len(s)-31,32):
		print s[x:x+32]
		
def createTestData(filename):

	fr = open(filename)

	listOfLines = fr.readlines()

	mydata = []

	for x in xrange(0,len(listOfLines)-32,33):
		myInstance = []
		for i in range(x,x+33):
			myLine = listOfLines[i]
			myLine.strip()
			myCharacters = myLine[0:32]
			for j in myCharacters:
				myInstance.append(j)
			
		myInstance.append(listOfLines[x+32].strip()[0])
	
		mydata.append(myInstance)
		
	for x in mydata:
		del x[1026]
		del x[1025]
		del x[1024]
		
	return mydata
	
def checkAccuracy(trainData,testData,k):
	accuracy = 0.0
	for x in testData:
		myans = classifyUsingKNN(trainData,x[0:len(x)-1],k)
		
		if (myans == x[-1]):
			
			accuracy = accuracy + 1.0/len(testData)
			
	return accuracy
	
			
			
	
	
	 
			
	
		
	
	

	
	
	

	
	

		
		
	
