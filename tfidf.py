#preprocess:from every document(each line) remove every chararacter that is not a alphabet 
#and numer,than change it to case insensitive
import re
def preprocess(content_list):
	stem_list =[]
	for content in content_list:
		stem =  re.sub(r'^[a-zA-z0-9]',' ',content)
		stem_lower = stem.sten_lower
		stem_list.append(stem_lower)
	return stem_list

