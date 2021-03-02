import tweepy

ACCESS_TOKEN =
ACCESS_SECRET =
CONSUMER_KEY =
CONSUMER_SECRET =


def connect_to_twitter():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter()

#project start
user = input("user:")
word_list=[]
tweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in tweets:
    word_list.append(tweet.text)

words=[]
for tweet in word_list:
    seperated = tweet.split()
    words = words + seperated

def Sorting(words2):
    words2.sort(key=len)
    return words2

print(Sorting(words))

SYMBOLS = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

results = []
for element in words:
    temp = ""
    for ch in element:
        if ch not in SYMBOLS:
            temp += ch

    results.append(temp)


for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])