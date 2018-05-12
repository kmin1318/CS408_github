# -*- coding: utf-8 -*-

import tweepy
import re

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

keywords = ['"가관이다" OR "가관이네" OR "가관이군" OR "가관이에요" OR "가관임" OR "가관입니다" -"안가관" -filter:retweets',
            '"가관이었다" OR "가관이었네" OR "가관이었어" OR "가관이었음" OR "가관이었습니다" -"안가관" -filter:retweets',
            '"거북하다" OR "거북하네" OR "거북하군" OR "거북해요" OR "거북함" OR "거북합니다" -"안거북" -filter:retweets',
            '"거북했다" OR "거북했네" OR "거북했어" OR "거북했음" OR "거북했습니다" -"안거북" -"괜히거북했" -filter:retweets',
            '"경박하다" OR "경박하네" OR "경박하군" OR "경박해요" OR "경박함" OR "경박합니다" -"안경박" -filter:retweets',
            '"경박했다" OR "경박했네" OR "경박했어" OR "경박했음" OR "경박했습니다" -"안경박" -filter:retweets',
            '"괴팍하다" OR "괴팍하네" OR "괴팍하군" OR "괴팍해요" OR "괴팍함" OR "괴팍합니다" -"안괴팍" -filter:retweets',
            '"괴팍했다" OR "괴팍했네" OR "괴팍했어" OR "괴팍했음" OR "괴팍했습니다" -"안괴팍" -filter:retweets',
            '"구역질난다" OR "구역질나네" OR "구역질나군" OR "구역질나는군" OR "구역질나요" OR "구역질남" OR "구역질납니다" -"안구역질" -filter:retweets',
            '"구역질났다" OR "구역질났네" OR "구역질났어" OR "구역질났음" OR "구역질났습니다" -"안구역질" -"괜히구역질났" -filter:retweets',
            '"구질구질하다" OR "구질구질하네" OR "구질구질하군" OR "구질구질해요" OR "구질구질함" OR "구질구질합니다" -"안구질구질" -filter:retweets',
            '"구질구질했다" OR "구질구질했네" OR "구질구질했어" OR "구질구질했음" OR "구질구질했습니다" -"안구질구질" -"괜히구질구질했" -filter:retweets',
            '"꼴불견" OR "넌더리" -filter:retweets',
            '"달갑잖다" OR "달갑잖네" OR "달갑잖군" OR "달갑잖아요" OR "달갑잖음" OR "달갑잖습니다" -filter:retweets',
            '"달갑잖았다" OR "달갑잖았네" OR "달갑잖았어" OR "달갑잖았음" OR "달갑잖았습니다" -"괜히달갑잖았" -filter:retweets',
            '"달갑지않다" OR "달갑지않네" OR "달갑지않군" OR "달갑지않아요" OR "달갑지않음" OR "달갑지않습니다" -filter:retweets',
            '"달갑지않았다" OR "달갑지않았네" OR "달갑지않았어" OR "달갑지않았음" OR "달갑지않았습니다" -"괜히달갑지않았" -filter:retweets',
            '"더럽다" OR "더럽네" OR "더럽군" OR "더러워요" OR "더러움" OR "더럽습니다" -"안더러" -"안더럽" -filter:retweets',
            '"더러웠다" OR "더러웠네" OR "더러웠어" OR "더러웠음" OR "더러웠습니다" -"안더러" -"괜히더러웠" -filter:retweets',
            '"망측하다" OR "망측하네" OR "망측하군" OR "망측해요" OR "망측함" OR "망측합니다" -"안망측" -filter:retweets',
            '"망측했다" OR "망측했네" OR "망측했어" OR "망측했음" OR "망측했습니다" -"안망측" -"괜히망측했" -filter:retweets',
            '"못미덥다" OR "못미덥네" OR "못미덥군" OR "못미더워요" OR "못미더움" OR "못미덥습니다" -filter:retweets',
            '"못미더웠다" OR "못미더웠네" OR "못미더웠어" OR "못미더웠음" OR "못미더웠습니다" -"괜히못미더웠" -filter:retweets',
            '"역겹다" OR "역겹네" OR "역겹군" OR "역겨워요" OR "역겨움" OR "역겹습니다" -"안역겨" -"안역겹" -filter:retweets',
            '"역겨웠다" OR "역겨웠네" OR "역겨웠어" OR "역겨웠음" OR "역겨웠습니다" -"안역겨" -"안역겹" -"괜히역겨웠" -filter:retweets',
            '"지독하다" OR "지독하네" OR "지독하군" OR "지독해요" OR "지독함" OR "지독합니다" -"안지독" -filter:retweets',
            '"지독했다" OR "지독했네" OR "지독했어" OR "지독했음" OR "지독했습니다" -"안지독" -"괜히지독했" -filter:retweets',
            '"징그럽다" OR "징그럽네" OR "징그럽군" OR "징그러워요" OR "징그러움" OR "징그럽습니다" -"안징그" -filter:retweets',
            '"징그러웠다" OR "징그러웠네" OR "징그러웠어" OR "징그러웠음" OR "징그러웠습니다" -"안징그" -"괜히징그러웠" -filter:retweets',
            '"흉측하다" OR "흉측하네" OR "흉측하군" OR "흉측해요" OR "흉측함" OR "흉측합니다" -"안흉측" -filter:retweets',
            '"흉측했다" OR "흉측했네" OR "흉측했어" OR "흉측했음" OR "흉측했습니다" -"안흉측" -"괜히흉측했" -filter:retweets',
            ]

file = open("Disgust.txt", 'w', -1, "utf-8")

lst = []

for keyword in keywords:
    cursor = tweepy.Cursor(api.search, 
                           q=keyword,
                           since='2018-01-01',
                           count=100,
                           geocode=location)
    for i, tweet in enumerate(cursor.items()):
        if not tweet.truncated:
            lst.append(tweet_processing(tweet.text))
            
set_lst = list(set(lst))
dataStr = '\n'.join(set_lst)

file.write(dataStr)

file.close()