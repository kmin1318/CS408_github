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

keywords = ['"겁난다" OR "겁나네" OR "겁나군" OR "겁나요" OR "겁남" OR "겁납니다" -"안겁" -filter:retweets',
            '"겁났다" OR "겁났네" OR "겁났어" OR "겁났음" OR "겁났습니다" -"안겁났" -"괜히겁났" -filter:retweets',
            '"공포감" -filter:retweets',
            '"두렵다" OR "두렵네" OR "두렵군" OR "두려워" OR "두려움" OR "두렵습니다" -"안두려" -"안두렵" -filter:retweets',
            '"두려웠다" OR "두려웠네" OR "두려웠어" OR "두려웠음" OR "두려웠습니다" -"안두려웠" -"괜히두려웠" -filter:retweets',
            '"무섭다" OR "무섭네" OR "무섭군" OR "무서워" OR "무서움" OR "무섭습니다" -"안무섭" -"안무서" -filter:retweets',
            '"무서웠다" OR "무서웠네" OR "무서웠어" OR "무서웠음" OR "무서웠습니다" -"안무서웠" -"괜히무서웠" -filter:retweets',
            '"무시무시하다" OR "무시무시하네" OR "무시무시하군" OR "무시무시해" OR "무시무시함" OR "무시무시합니다" -"안무시무시" -filter:retweets',
            '"무시무시했다" OR "무시무시했네" OR "무시무시했어" OR "무시무시했음" OR "무시무시했습니다" -"안무시무시" -filter:retweets',
            '"불안하다" OR "불안하네" OR "불안하군" OR "불안해" OR "불안함" OR "불안합니다" -"안불안" -filter:retweets',
            '"불안했다" OR "불안했네" OR "불안했어" OR "불안했음" OR "불안했습니다" -"안불안" -"괜히불안했" -filter:retweets',
            '"살벌하다" OR "살벌하네" OR "살벌하군" OR "살벌해" OR "살벌함" OR "살벌합니다" -"안살벌" -filter:retweets',
            '"살벌했다" OR "살벌했네" OR "살벌했어" OR "살벌했음" OR "살벌했습니다" -"안살벌" -"괜히살벌했" -filter:retweets',
            '"새파래진다" OR "새파래지네" OR "새파래지는군" OR "새파래짐" OR "새파래집니다" -"안새파래" -filter:retweets',
            '"새파래졌다" OR "새파래졌네" OR "새파래졌어" OR "새파래졌음" OR "새파래졌습니다" -"안새파래졌" -"괜히새파래졌" -filter:retweets',
            '"섬뜩하다" OR "섬뜩하네" OR "섬뜩하군" OR "섬뜩해" OR "섬뜩함" OR "섬뜩합니다" -"안섬뜩" -filter:retweets',
            '"섬뜩했다" OR "섬뜩했네" OR "섬뜩했어" OR "섬뜩했음" OR "섬뜩했습니다" -"안섬뜩" -"괜히섬뜩했" -filter:retweets',
            '"소름끼친다" OR "소름끼치네" OR "소름끼치군" OR "소름끼치는군" OR "소름끼쳐" OR "소름끼침" OR "소름끼칩니다" -"안소름끼" -filter:retweets',
            '"소름끼쳤다" OR "소름끼쳤네" OR "소름끼쳤어" OR "소름끼쳤음" OR "소름끼쳤습니다" -"안소름끼쳤" -"괜히소름끼쳤" -filter:retweets',
            '"소름이끼친다" OR "소름이끼치네" OR "소름이끼치군" OR "소름이끼치는군" OR "소름이끼쳐" OR "소름이끼침" OR "소름이끼칩니다" -"안소름이끼" -filter:retweets',
            '"소름이끼쳤다" OR "소름이끼쳤네" OR "소름이끼쳤어" OR "소름이끼쳤음" OR "소름이끼쳤습니다" -"안소름이끼쳤" -"괜히소름이끼쳤" -filter:retweets',
            '"스산하다" OR "스산하네" OR "스산하군" OR "스산해" OR "스산함" OR "스산합니다" -"안스산" -filter:retweets',
            '"스산했다" OR "스산했네" OR "스산했어" OR "스산했음" OR "스산했습니다" -"안스산" -"괜히스산했" -filter:retweets',
            '"아찔하다" OR "아찔하네" OR "아찔하군" OR "아찔해" OR "아찔함" OR "아찔합니다" -"안아찔" -filter:retweets',
            '"아찔했다" OR "아찔했네" OR "아찔했어" OR "아찔했음" OR "아찔했습니다" -"안아찔" -"괜히아찔했" -filter:retweets',
            '"오싹하다" OR "오싹하네" OR "오싹하군" OR "오싹해" OR "오싹함" OR "오싹합니다" -"안오싹" -filter:retweets',
            '"오싹했다" OR "오싹했네" OR "오싹했어" OR "오싹했음" OR "오싹했습니다" -"안오싹" -"괜히오싹했" -filter:retweets',
            '"으스스하다" OR "으스스하네" OR "으스스하군" OR "으스스해" OR "으스스함" OR "으스스합니다" -"안으스스" -filter:retweets',
            '"으스스했다" OR "으스스했네" OR "으스스했어" OR "으스스했음" OR "으스스했습니다" -"안으스스" -"괜히으스스했" -filter:retweets',
            '"조마조마하다" OR "조마조마하네" OR "조마조마하군" OR "조마조마해" OR "조마조마함" OR "조마조마합니다" -"안조마조마" -filter:retweets',
            '"조마조마했다" OR "조마조마했네" OR "조마조마했어" OR "조마조마했음" OR "조마조마했습니다" -"안조마조마" -"괜히조마조마했" -filter:retweets',
            '"초조하다" OR "초조하네" OR "초조하군" OR "초조해" OR "초조함" OR "초조합니다" -"안초조" -filter:retweets',
            '"초조했다" OR "초조했네" OR "초조했어" OR "초조했음" OR "초조했습니다" -"안초조" -"괜히초조했" -filter:retweets',
            ]

file = open("Fear.txt", 'a', -1, "utf-8")

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