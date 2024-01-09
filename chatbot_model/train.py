from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle
import csv
import timeit
import random
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk





def preprocess(sentence):
	sentence = sentence.lower()
	#print(sentence)
		
	sentences = nltk.sent_tokenize(sentence.lower())
	#print (sentences)
	
	words = nltk.word_tokenize(sentence.lower())
    #print(sentence)
		
	new_words= [word for word in words if word.isalnum()]
	#new_words

	"""WordSet = []
	for word in new_words:
		if word not in set(stopwords.words("english")):
			WordSet.append(word)
	#print(WordSet)
		
	
	lm= WordNetLemmatizer()
	
	WordSetLem = []
	for word in new_words:
		WordSetLem.append(lm.lemmatize(word))
	print(WordSetLem)"""
	
	sentence=""
	for i in new_words:
		sentence+=i+" "
	print(sentence)
	return sentence





def train(user_sentence):
	csv_file_path = "dataset.csv"
		
	tfidf_vectorizer_pikle_path = "tfidf_vectorizer.pickle"
	tfidf_matrix_train_pikle_path = "tfidf_matrix_train.pickle"
		
	i = 0
	sentences = []
	test_set = (user_sentence,"")
		
	temp=[]
	for i in test_set:
		temp.append(preprocess(i))
				
	test_set=temp
		
	sentences.append(" No you")
	sentences.append(" No you")
		
		
		
	start = timeit.default_timer()
		   
		   
	with open(csv_file_path, "r") as sentence_file:
		reader = csv.reader(sentence_file, delimiter=",")
		for row in reader:
			sentences.append(row[0])
			i =+ 1
			
	print(sentences[0])
			
	temp=[]
			
	for i in sentences:
		temp.append(preprocess(i))
				
	sentences=temp
						
	tfidf_vectorizer = TfidfVectorizer()
			
	tfidf_matrix_train = tfidf_vectorizer.fit_transform(sentences)
			
	stop = timeit.default_timer()
	#print(f"training time took was: {stop - start}")
			
	f = open(tfidf_vectorizer_pikle_path, 'wb')
	pickle.dump(tfidf_vectorizer, f)
	f.close()
			
	f = open(tfidf_matrix_train_pikle_path, 'wb')
	pickle.dump(tfidf_matrix_train, f)
	f.close()

	tfidf_matrix_test = tfidf_vectorizer.transform(test_set)
		
	cosine = cosine_similarity(tfidf_matrix_test, tfidf_matrix_train)
	cosine = np.delete(cosine, 0)
		
	maxi = cosine.max()
	response_index = 0
		
	if (maxi > 0.7):
		new_max = maxi - 0.01
		listi = np.where(cosine > new_max)
		response_index = random.choice(listi[0])
	else:
		response_index = np.where(cosine == maxi)[0][0] + 2
	j = 0
		
	with open(csv_file_path,"r") as sentences_file:
		reader = csv.reader(sentences_file, delimiter=",")
		for row in reader:
			j += 1
			if j == response_index:
				return row[1], response_index,
				break
				
				
response=train("hi")

try:
	print("First response chat bot: ",response)
	print("your chatbot is ready")
except:
	print("your chatbot is not ready..plz train properly!!")