from astropy.io import fits #using the fits I/O class of Astropy
import matplotlib.pyplot as plt  #for plotting the graph
import sys #for exceptions handling

try:
	inputFITS = sys.argv[1]
	image = fits.open(inputFITS)
	imageData = image[0].data
except :
	sys.exit("Wrong input")



def brightestPixel(imageData, coordinatesList):
	zBound = imageData.shape[0]
	yBound = imageData.shape[1]
	xBound = imageData.shape[2]
	pixelValue = 0 #initializing variables to be used in the indented loops
	x = 0
	y = 0
	for j in range(yBound):
		for k in range(xBound):
			tempValue = imageData[0, j, k]
			if(tempValue >= pixelValue):
				pixelValue = tempValue
				x = k
				y = j
	coordinatesList.append(y) #we are inverting the x and y to conform with the library syntax
	coordinatesList.append(x)
	return coordinatesList

def generateValuesList(imageData, coordinatesList, valuesList):	
	zBound = imageData.shape[0]
	yBound = imageData.shape[1]
	xBound = imageData.shape[2]
	for i in range(zBound):
		valuesList.append(imageData[i, coordinatesList[0], coordinatesList[1]]) #we are assuming that is it a square image (i.e xBound = yBound)
	return valuesList

def generateTimeList(imageData, timeList):
	timeBound = imageData.shape[0]
	for m in range(timeBound):
		timeList.append(m)
	return timeList	

def plotCreation(valuesList, timeList):
	plt.plot(timeList, valuesList)
	plt.ylabel('Differential magnitude')
	plt.xlabel('Time')
	plt.show()

coordinatesList = []
brightestPixel(imageData, coordinatesList)
valuesList = []
generateValuesList(imageData, coordinatesList, valuesList)
timeList = []
generateTimeList(timeList)
print timeList
print "\n"
print valuesList
print "\n"
print coordinatesList
plotCreation(valuesList, timeList)
