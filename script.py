import tool
import tfidf
filename = 'tweet.txt'
content_list = tool.read_tweet_content(filename)
print(content_list[0])
print('- - '*50)
print(content_list[1])
stem_list = tfidf.preprocess(content_list)
print(stem_list[0])
print('- - '*50)
print(stem_list[1])