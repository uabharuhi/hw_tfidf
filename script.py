import tool
filename = 'tweet.txt'
content_list = tool.read_tweet_content(filename)
print(content_list[0])
print('- - '*50)
print(content_list[1])