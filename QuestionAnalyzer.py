import nltk
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy as np
from sklearn.svm import SVC
questions = []
views = []

#data load
with open('QuestionAndViewCount.csv', 'r') as f:
	read_data = f.readlines()
	for i in range(1,len(read_data)):
		ind = read_data[i].rindex(",")
		questions.append(read_data[i][1:ind-1])
		num = re.findall('\d+', read_data[i][ind+2:len(read_data[i])])
		views.append(int(num[0]))
		
#analysis


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

