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

keywords = ['"갑작스럽다" OR "갑작스럽네" OR "갑작스럽군" OR "갑작스러워" OR "갑작스러움" OR "갑작스럽습니다" -"안갑작스" -filter:retweets',
            '"갑작스러웠다" OR "갑작스러웠네" OR "갑작스러웠어" OR "갑작스러웠음" OR "갑작스러웠습니다" -"안갑작스러웠" -filter:retweets',
            '"경악함" -"안경악" -filter:retweets',
            '"경악했다" OR "경악했네" OR "경악했어" OR "경악했음" OR "경악했습니다" -"안경악" -filter:retweets',
            '"급작스럽다" OR "급작스럽네" OR "급작스럽군" OR "급작스러워" OR "급작스러움" OR "급작스럽습니다" -"안급작스" -filter:retweets',
            '"급작스러웠다" OR "급작스러웠네" OR "급작스러웠어" OR "급작스러웠음" OR "급작스러웠습니다" -"안급작스러웠" -filter:retweets',
            '"기겁함" -"안기겁" -filter:retweets',
            '"기겁했다" OR "기겁했네" OR "기겁했어" OR "기겁했음" OR "기겁했습니다" -"안기겁" -"괜히기겁했" -filter:retweets',
            '"기상천외하다" OR "기상천외하네" OR "기상천외하군" OR "기상천외해" OR "기상천외함" OR "기상천외합니다" -"안기상천외" -filter:retweets',
            '"기상천외했다" OR "기상천외했네" OR "기상천외했어" OR "기상천외했음" OR "기상천외했습니다" -"안기상천외" -filter:retweets',
            '"기절초풍하다" OR "기절초풍하네" OR "기절초풍하군" OR "기절초풍해" OR "기절초풍함" OR "기절초풍합니다" -"안기절초풍" -filter:retweets',
            '"기절초풍했다" OR "기절초풍했네" OR "기절초풍했어" OR "기절초풍했음" OR "기절초풍했습니다" -"안기절초풍" -filter:retweets',
            '"까무러침" -"안까무러" -filter:retweets',
            '"까무러쳤다" OR "까무러쳤네" OR "까무러쳤어" OR "까무러쳤음" OR "까무러쳤습니다" -"안까무러쳤" -filter:retweets',
            '"깜짝" -filter:retweets',
            '"놀랍다" OR "놀랍네" OR "놀랍군" OR "놀람" OR "놀랍습니다" -"안놀랍" -"안놀람" -filter:retweets',
            '"놀라웠다" OR "놀라웠네" OR "놀라웠어" OR "놀라웠음" OR "놀라웠습니다" -"안놀라웠" -"괜히놀라웠" -filter:retweets',
            '"놀랐다" OR "놀랐네" OR "놀랐어" OR "놀랐음" OR "놀랐습니다" -"안놀랐" -"괜히놀랐" -filter:retweets',
            '"놀랬다" OR "놀랬네" OR "놀랬어" OR "놀랬음" OR "놀랬습니다" -"안놀랬" -"괜히놀랬" -filter:retweets',
            '"뜨악함" -"안뜨악" -filter:retweets',
            '"뜨악했다" OR "뜨악했네" OR "뜨악했어" OR "뜨악했음" OR "뜨악했습니다" -"안뜨악" -"괜히뜨악했" -filter:retweets',
            '"쇼킹함" -"안쇼킹" -filter:retweets',
            '"쇼킹했다" OR "쇼킹했네" OR "쇼킹했어" OR "쇼킹했음" OR "쇼킹했습니다" -"안쇼킹" -filter:retweets',
            '"충격적이다" OR "충격적이네" OR "충격적이군" OR "충격적이야" OR "충격적이에요" OR "충격적임" OR "충격적입니다" -"안충격적" -filter:retweets',
            '"충격적이었다" OR "충격적이었네" OR "충격적이었음" OR "충격적이었습니다" -"안충격적" -"괜히충격적이었" -filter:retweets',
            '"휘둥그레짐" -"안휘둥그레" -filter:retweets',
            '"휘둥그레졌다" OR "휘둥그레졌네" OR "휘둥그레졌어" OR "휘둥그레졌음" OR "휘둥그레졌습니다" -"안휘둥그레졌" -"괜히휘둥그레졌" -filter:retweets',
            '"흠칫함" -"안흠칫" -filter:retweets',
            '"흠칫했다" OR "흠칫했네" OR "흠칫했어" OR "흠칫했음" OR "흠칫했습니다" -"안흠칫" -"괜히흠칫했" -filter:retweets',
            ]

file = open("Surprise.txt", 'a', -1, "utf-8")

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