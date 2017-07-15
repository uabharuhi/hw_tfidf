import tool
import tfidf
filename = 'tweet.txt'
content_list = tool.read_tweet_content(filename)
print(content_list[0])
print('- - '*50)
print(content_list[1])
stem_list = tfidf.preprocess(content_list)
print('- - '*50)
print(stem_list[0])
print('- - '*50)
print(stem_list[1])
token_2d_list = tfidf.tokenization(stem_list)
print(token_2d_list[0])
print(token_2d_list[1])

print('res')
res = tfidf.tf_idf(token_2d_list)
print('dump')
tfidf.dump_tfidf_json(res,'tfidf.json')

