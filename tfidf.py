#preprocess:from every document(each line) remove every chararacter that is not a alphabet 
#and numer,than change it to case insensitive
import re
import math
def preprocess(content_list):
	stem_list =[]
	for content in content_list:
		stem =  re.sub(r'[^a-zA-z0-9]',' ',content)
		stem_lower = stem.lower()
		stem_list.append(stem_lower)
	return stem_list

def tokenization(stem_list):
	token_2d_list =[]
	for stem_sentence in stem_list:
		tokens = stem_sentence.split()
		token_2d_list.append(tokens)
	return token_2d_list 



#tf function will return list of ft_count of set(key is word,count is term frequecy) in each line(document)
# [{word1,cnt1,word2,cnt2}(document1),{...}(document2),{}]
# and a set of all words
def tf_default(token_2d_list):
	word_set = set() #set of string
	tf_list = []
	for tokens in token_2d_list:
		tf = {}
		for token in tokens:
			if token not in word_set:
				word_set.add( token )
			if token not in tf:
				tf [ token ] = 0
			tf[ token ] += 1
		# find max freq
		max_freq = tf [ max( tf, key=lambda i: tf[i] ) ]

		for token in tf:
			tf[token] /= max_freq

		tf_list.append(tf)
	return  tf_list ,word_set


# word_set : set of all word
# tf_list : ...
def idf_default(tf_list,word_set):
	idf_dict = {}
	N = len(tf_list)
	for word in word_set:
		idf_dict[word] = 0
		occur_doc = 0
		for tf in tf_list:
			if word in tf:
				occur_doc+=1
		idf_dict[ word ] =  math.log2( N/occur_doc )

	return idf_dict



def tf_idf(token_2d_list ,tf_func=tf_default,idf_func=idf_default):
	tf_list ,word_set = tf_func(token_2d_list)
	idf_dict   = idf_func(tf_list,word_set)

	tfidf_list =[]

	for i,tf in enumerate(tf_list):
		tfidf_list.append(tf)
		for word in tf:
			tfidf_list[i][word]*=idf_dict[word]
			
	return tfidf_list




