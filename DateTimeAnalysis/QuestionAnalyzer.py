import nltk
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy as np
from sklearn.svm import SVC
import csv
import numpy as np
import matplotlib.pyplot as plt
import textstat 


questions = []
views = []

#data load
def loadData(filename):
	title = []
	tags = []
	data = []
	with open(filename, 'r') as f:
		allData = csv.reader(f)
		for row in allData:
			if (row[0] == "Title"):
				continue
			datarow= []
			#Title 0 ,Score 1 ,ViewCount 2,Tags 3 ,AnswerCount 4 ,CommentCount 5 ,FavoriteCount 6
			title.append(row[0])
			tags.append(row[3])
			datarow.append(int(row[1]))
			datarow.append(int(row[2]))
			datarow.append(int(row[4]))
			datarow.append(int(row[5]))
			if (row[6] != ""):
				datarow.append(int(row[6]))
			else:
				datarow.append(0)
			data.append(datarow)
	return title, tags, data
			

def processData(data):
	#score 40, viewcount 30, answercount 10, commentcount 5, favoritecount 15
	score_score = .4
	viewcount_score = .3
	answercount_score = .1
	commentcount_score = .05
	favoritecount_score = .15

	maxPoints = np.amax(data, axis=0)
	normalizedData = data/np.float_(maxPoints)
	Y_data = []

	for i in range(len(normalizedData)):
		Y_data.append(normalizedData[i][0]*score_score + normalizedData[i][1]*viewcount_score + normalizedData[i][2]*answercount_score + normalizedData[i][3]*commentcount_score + normalizedData[i][4]*favoritecount_score )
	
	return Y_data

def plotData(allData, Y_data):
	score = np.array(allData)[:,0]
	viewcount = np.array(allData)[:,1]
	answercount = np.array(allData)[:,2]
	commentcount = np.array(allData)[:,3]
	favoritecount = np.array(allData)[:,4]

	#plt.scatter(Y_data, score, color='blue')
	#plt.scatter(Y_data, viewcount, color='red')
	#plt.scatter(Y_data, answercount, color='green')
	#plt.scatter(Y_data, commentcount, color='purple')
	plt.scatter(Y_data, favoritecount, color='black')

	plt.show()

def getReadabilityScore(title):
	print textstat.flesch_reading_ease(title[0])

def simpleAnalysis():

	cv = CountVectorizer(questions)
	transformedX = cv.fit_transform(questions).toarray()


	interval = 600000
	maxval = 2800000
	minval = 5000
	category = []

	for i in range(len(views)):
		if views[i] > (maxval-interval):
			category.append(5)
		elif views[i] > (maxval-2*interval):
			category.append(4)
		elif views[i] > (maxval-3*interval):
			category.append(3)
		elif views[i] > (maxval-4*interval):
			category.append(2)
		else:
			category.append(1)

	#print category

	svc = SVC()
	svc.fit(transformedX,category)
	print(svc.predict(category))

def main():
	title, tags, data = loadData('QueryResults_All.csv')
	getReadabilityScore(title)
	#Y_data = processData(data)
	#plotData(data, Y_data)

if __name__ == "__main__":
    main()

