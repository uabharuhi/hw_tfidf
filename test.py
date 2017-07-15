import re
import tfidf
#import re
#pattern = '[0-9]+[\t]+(.+)[\t]+[0-9]+'
#p = re.compile(pattern)
#m = p.search("\"1	theo walcott is still shit, watch rafa and johnny deal with him on saturday.	1\"")
#content = m.group(1)
#print(content)


# test tf idf
#i hava hava a dog
#i like 
# i :1/2 ,have:2/2, a :1/2  dog:1/2  
# i:1 like:1 

#tf-idf i:0 have:1 a:1/2 dog:1/2 
#i:0 like:1

res = tfidf.tf_idf([ ['i','have','have','a','dog'],
	          ['i','like'] ])
print(res)



