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

keywords = ['"감개무량하다" OR "감개무량하네" OR "감개무량하군" OR "감개무량해" OR "감개무량함" OR "감개무량합니다" -"안감개무량" -filter:retweets',
            '"감개무량했다" OR "감개무량했네" OR "감개무량했어" OR "감개무량했음" OR "감개무량했습니다" -"안감개무량" -filter:retweets',
            '"감격한다" OR "감격함" OR "감격합니다" -"안감격" -filter:retweets',
            '"감격했다" OR "감격했네" OR "감격했어" OR "감격했음" OR "감격했습니다" -"안감격" -"괜히감격했" -filter:retweets',
            '"감동한다" OR "감동함" OR "감동합니다" -"안감동" -filter:retweets',
            '"감동했다" OR "감동했네" OR "감동했어" OR "감동했음" OR "감동했습니다" -"안감동" -"괜히감동했" -filter:retweets',
            '"감미롭다" OR "감미롭네" OR "감미롭군" OR "감미로워" OR "감미로움" OR "감미롭습니다" -"안감미" -filter:retweets',
            '"감미로웠다" OR "감미로웠네" OR "감미로웠어" OR "감미로웠음" OR "감미로웠습니다" -"안감미로웠" -filter:retweets',
            '"감복한다" OR "감복함" OR "감복합니다" -"안감복" -filter:retweets',
            '"감복했다" OR "감복했네" OR "감복했어" OR "감복했음" OR "감복했습니다" -"안감복" -"괜히감복했" -filter:retweets',
            '"감사하다" OR "감사한다" OR "감사하네" OR "감사하군" OR "감사해" OR "감사함" OR "감사합니다" -"안감사" -filter:retweets',
            '"감사했다" OR "감사했네" OR "감사했어" OR "감사했음" OR "감사했습니다" -"안감사" -"괜히감사했" -filter:retweets',
            '"경쾌하다" OR "경쾌하네" OR "경쾌하군" OR "경쾌해" OR "경쾌함" OR "경쾌합니다" -"안경쾌" -filter:retweets',
            '"경쾌했다" OR "경쾌했네" OR "경쾌했어" OR "경쾌했음" OR "경쾌했습니다" -"안경쾌" -filter:retweets',
            '"고맙다" OR "고맙네" OR "고맙군" OR "고마워" OR "고마움" OR "고맙습니다" -"안고마" -"안고맙" -filter:retweets',
            '"고마웠다" OR "고마웠네" OR "고마웠어" OR "고마웠음" OR "고마웠습니다" -"안고마웠" -filter:retweets',
            '"근사하다" OR "근사하네" OR "근사하군" OR "근사해" OR "근사함" OR "근사합니다" -"안근사" -filter:retweets',
            '"근사했다" OR "근사했네" OR "근사했어" OR "근사했음" OR "근사했습니다" -"안근사" -filter:retweets',
            '"기분좋다" OR "기분좋네" OR "기분좋군" OR "기분좋아" OR "기분좋음" OR "기분좋습니다" -"안기분좋" -filter:retweets',
            '"기분좋았다" OR "기분좋았네" OR "기분좋았어" OR "기분좋았음" OR "기분좋았습니다" -"안기분좋았" -"괜히기분좋았" -filter:retweets',
            '"기쁘다" OR "기쁘네" OR "기쁘군" OR "기뻐" OR "기쁩니다" -"안기쁘" -"안기쁩" -filter:retweets',
            '"기뻤다" OR "기뻤네" OR "기뻤어" OR "기뻤음" OR "기뻤습니다" -"안기뻤" -filter:retweets',
            '"낭만적이다" OR "낭만적이네" OR "낭만적이군" OR "낭만적이야" OR "낭만적이에요" OR "낭만적임" OR "낭만적입니다" -"안낭만적" -filter:retweets',
            '"낭만적이었다" OR "낭만적이었네" OR "낭만적이었어" OR "낭만적이었음" OR "낭만적이었습니다" -"안낭만적이었" -filter:retweets',
            '"달갑다" OR "달갑네" OR "달갑군" OR "달가워" OR "달가움" OR "달갑습니다" -"안달가" -"안달갑" -filter:retweets',
            '"달가웠다" OR "달가웠네" OR "달가웠어" OR "달가웠음" OR "달가웠습니다" -"안달가웠" -filter:retweets',
            '"대견하다" OR "대견하네" OR "대견하군" OR "대견해" OR "대견함" OR "대견합니다" -"안대견" -filter:retweets',
            '"대견했다" OR "대견했네" OR "대견했어" OR "대견했음" OR "대견했습니다" -"안대견" -filter:retweets',
            '"따뜻하다" OR "따뜻하네" OR "따뜻하군" OR "따뜻해" OR "따뜻함" OR "따뜻합니다" -"안따뜻" -filter:retweets',
            '"따스하다" OR "따스하네" OR "따스하군" OR "따스해" OR "따스함" OR "따스합니다" -"안따스" -filter:retweets',
            '"만족한다" OR "만족하네" OR "만족해" OR "만족함" OR "만족합니다" -"안만족" -filter:retweets',
            '"만족했다" OR "만족했네" OR "만족했어" OR "만족했음" OR "만족했습니다" -"안만족" -filter:retweets',
            '"반갑다" OR "반갑네" OR "반갑군" OR "반가워" OR "반가움" OR "반갑습니다" -"안반가" -"안반갑" -filter:retweets',
            '"반가웠다" OR "반가웠네" OR "반가웠어" OR "반가웠음" OR "반가웠습니다" -"안반가웠" -filter:retweets',
            '"방그레" OR "방글방글" OR "방긋" -filter:retweets',
            '"보기좋다" OR "보기좋네" OR "보기좋군" OR "보기좋아" OR "보기좋음" OR "보기좋습니다" -"안보기좋" -filter:retweets',
            '"보기좋았다" OR "보기좋았네" OR "보기좋았어" OR "보기좋았음" OR "보기좋았습니다" -"안보기좋았" -filter:retweets',
            '"뿌듯하다" OR "뿌듯하네" OR "뿌듯하군" OR "뿌듯해" OR "뿌듯함" OR "뿌듯합니다" -"안뿌듯" -filter:retweets',
            '"뿌듯했다" OR "뿌듯했네" OR "뿌듯했어" OR "뿌듯했음" OR "뿌듯했습니다" -"안뿌듯" -filter:retweets',
            ]

file = open("Happy.txt", 'a', -1, "utf-8")

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