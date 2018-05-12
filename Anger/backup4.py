# -*- coding: utf-8 -*-

import tweepy 

consumer_key = 'jYCKoZ7VJ7MRjUIxAr7ZT6IZ2'

consumer_secret = '8BFrc01U3bodfN3oMC75jZO0a9prF6KQUny1H44Kg2eY1r6nzn'

access_token = '972705355154079744-5M7h50L3jqEZgdtwh4CTQwFcPYrbg3r'

access_token_secret = 'dY675bItOVShdHpyG9WAYyevlpcD8LB8qHZJ45qzTPES3'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)  


location = "%s,%s,%s" % ("35.95", "128.25", "1000km")

keyword = "분노하다 OR 분노한다 OR 화나다 OR 화난다 OR 화가난다 -filter:retweets"

file = open("Anger_Predicate_in_Tweet.txt", 'w', -1, "utf-8")


cursor = tweepy.Cursor(api.search, 
                       q=keyword,
                       since='2018-01-01',
                       count=100,
                       geocode=location)

for i, tweet in enumerate(cursor.items(100)):
#    print("{}: {}".format(i, tweet.text))
#    dt = tweet.created_at
#    print(dt.strftime("%Y-%m-%d %H:%M"))
#    print(tweet.coordinates, tweet.place, tweet.geo, tweet.user.location)
#    print(tweet.truncated, tweet.retweeted)

    if not tweet.truncated:
        dataStr = str(i) + ',' + tweet.text + '\n\n'
        file.write(dataStr)

file.close()