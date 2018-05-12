# -*- coding: utf-8 -*-

import tweepy 

consumer_key = 'jYCKoZ7VJ7MRjUIxAr7ZT6IZ2'

consumer_secret = '8BFrc01U3bodfN3oMC75jZO0a9prF6KQUny1H44Kg2eY1r6nzn'

access_token = '972705355154079744-5M7h50L3jqEZgdtwh4CTQwFcPYrbg3r'

access_token_secret = 'dY675bItOVShdHpyG9WAYyevlpcD8LB8qHZJ45qzTPES3'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True)


location = "%s,%s,%s" % ("35.95", "128.25", "1000km")

keyword = '"반가워" OR "반갑네" OR "반갑다" OR "반가웠" OR "반갑스럽" OR "반가움" -"안반가" -"안반갑" -filter:retweets'

file = open("Happy.txt", 'w', -1, "utf-8")


cursor = tweepy.Cursor(api.search, 
                       q=keyword,
                       since='2018-01-01',
                       count=100,
                       geocode=location)

def tweet_processing(t):
    l = t.splitlines()
    
    if l[0][0] == '@':
        l2 = l[0].split(' ')
        i = 1
        print(l2)
        while i < len(l2):
            if (l2[i] != '') and (l2[i][0] == '@'):
                i = i + 1
            else:
                break
        nt = ' '.join(l2[i:])
        l[0] = nt

    if 'http' in l[-1]:
        l3 = l[-1].split(' ')
        nt = ' '.join(l3[:-1])
        l[-1] = nt
        
    pt = ' '.join(l)
    return pt

for i, tweet in enumerate(cursor.items()):
    if not tweet.truncated:
        dataStr = tweet_processing(tweet.text) + '\n'
        file.write(dataStr)

file.close()