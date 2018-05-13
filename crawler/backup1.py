# -*- coding: utf-8 -*-

import tweepy
import re

f = open("politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()


consumer_key = 'wDPlj513reBvpDflXKDbSK9lQ'

consumer_secret = 'wfKhCv3L0djCNPhTqNW2CyysKaLUP2ARgUE8h03UL8RtKjOckW'

access_token = '972705355154079744-Xch0ybmZ678I6ZkTOuK87E5mfuiYoH0'

access_token_secret = 'xeniK0Q09fwQtyiWNwLuQtNCcLTgrmHdxJOSvlN5yjP73'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def tweet_processing(t):
    t1 = re.sub(r"@\S+", "", t)
    t2 = re.sub(r"http\S+", "", t1)
    t3 = t2.strip()
    l = t3.splitlines()
    pt = ' '.join(l)
    return pt

location = "%s,%s,%s" % ("35.95", "128.25", "1000km")

#keywords = ['"대통령" OR "문재인" -filter:retweets',
#            '"서울특별시장" OR "서울시장" OR "박원순" -filter:retweets',
#           '"부산광역시장" OR "부산시장" OR "서병수" -filter:retweets']

for keyword in keywords:
    lst = []
    f_name = keyword.split('"')[1]+".txt"
    f = open(f_name, "a", -1, "utf-8")
    cursor = tweepy.Cursor(api.search,
                       q=keyword,
                       since='2018-01-01',
                       count=100,
                       geocode=location)
    for i, tweet in enumerate(cursor.items()):
        if not tweet.truncated:
            text = tweet_processing(tweet.text)
            rt_count = str(tweet.retweet_count)
            dt = tweet.created_at
            date = dt.strftime("%Y-%m-%d %H:%M")
            data = text + '\t' + rt_count + '\t' + date
            lst.append(data)
    set_lst = list(set(lst))
    dataStr = '\n'.join(set_lst)
    f.write(dataStr)
    f.close()
