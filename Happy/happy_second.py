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

keywords = ['"사랑스럽다" OR "사랑스럽네" OR "사랑스럽군" OR "사랑스러워" OR "사랑스러움" OR "사랑스럽습니다" -"안사랑스" -filter:retweets',
            '"상쾌하다" OR "상쾌하네" OR "상쾌하군" OR "상쾌해" OR "상쾌함" OR "상쾌합니다" -"안상쾌" -filter:retweets',
            '"상쾌했다" OR "상쾌했네" OR "상쾌했어" OR "상쾌했음" OR "상쾌했습니다" -"안상쾌" -filter:retweets',
            '"상큼하다" OR "상큼하네" OR "상큼하군" OR "상큼해" OR "상큼함" OR "상큼합니다" -"안상큼" -filter:retweets',
            '"설렌다" OR "설레네" OR "설레군" OR "설레" OR "설렙니다" -"안설레" -filter:retweets',
            '"설레였다" OR "설레였네" OR "설레였어" OR "설레였음" OR "설레였습니다" -"안설레였" -filter:retweets',
            '"신난다" OR "신나네" OR "신나군" OR "신나" OR "신남" OR "신납니다" -"안신나" -"안신남" -"안신납" -filter:retweets',
            '"신명난다" OR "신명나네" OR "신명나군" OR "신명나" OR "신명남" OR "신명납니다" -"안신명" -filter:retweets',
            '"신명났다" OR "신명났네" OR "신명났어" OR "신명났음" OR "신명났습니다" -"안신명났" -filter:retweets',
            '"신바람난다" OR "신바람나네" OR "신바람나군" OR "신바람나는군" OR "신바람나" OR "신바람남" OR "신바람납니다" -"안신바람" -filter:retweets',
            '"신바람났다" OR "신바람났네" OR "신바람났어" OR "신바람났음" OR "신바람났습니다" -"안신바람났" -"괜히신바람났" -filter:retweets',
            '"싱글벙글하다" OR "싱글벙글하네" OR "싱글벙글하군" OR "싱글벙글해" OR "싱글벙글함" OR "싱글벙글합니다" -"안싱글벙글" -filter:retweets',
            '"싱글벙글했다" OR "싱글벙글했네" OR "싱글벙글했어" OR "싱글벙글했음" OR "싱글벙글했습니다" -"안싱글벙글" -"괜히싱글벙글했" -filter:retweets',
            '"예쁘다" OR "예쁘네" OR "예쁘군" OR "예뻐" OR "예쁨" OR "예쁩니다" -"안예쁘" -"안예뻐" -"안예쁨" -"안예쁩" -filter:retweets',
            '"우아하다" OR "우아하네" OR "우아하군" OR "우아해" OR "우아함" OR "우아합니다" -"안우아" -filter:retweets',
            '"우아했다" OR "우아했어" OR "우아했음" OR "우아했습니다" -"안우아" -filter:retweets',
            '"유쾌하다" OR "유쾌하네" OR "유쾌하군" OR "유쾌해" OR "유쾌함" OR "유쾌합니다" -"안유쾌" -filter:retweets',
            '"유쾌했다" OR "유쾌했네" OR "유쾌했어" OR "유쾌했음" OR "유쾌했습니다" -"안유쾌" -filter:retweets',
            '"재미있다" OR "재미있네" OR "재미있군" OR "재미있어" OR "재미있음" OR "재미있습니다" -"안재미있" -filter:retweets',
            '"재미있었다" OR "재미있었네" OR "재미있었어" OR "재미있었음" OR "재미있었습니다" -"안재미있었" -filter:retweets',
            '"좋다" OR "좋네" OR "좋군" OR "좋아" OR "좋음" OR "좋습니다" -"안좋" -filter:retweets',
            '"좋아한다" OR "좋아해요" OR "좋아함" OR "좋아합니다" -"안좋아" -filter:retweets',
            '"즐겁다" OR "즐겁네" OR "즐겁군" OR "즐거워" OR "즐거움" OR "즐겁습니다" -"안즐거" -"안즐겁" -filter:retweets',
            '"즐거웠다" OR "즐거웠네" OR "즐거웠어" OR "즐거웠음" OR "즐거웠습니다" -"안즐거웠" -filter:retweets',
            '"친근하다" OR "친근하네" OR "친근하군" OR "친근해" OR "친근함" OR "친근합니다" -"안친근" -filter:retweets',
            '"친근했다" OR "친근했네" OR "친근했어" OR "친근했음" OR "친근했습니다" -"안친근" -filter:retweets',
            '"친숙하다" OR "친숙하네" OR "친숙하군" OR "친숙해" OR "친숙함" OR "친숙합니다" -"안친숙" -filter:retweets',
            '"친숙했다" OR "친숙했네" OR "친숙했어" OR "친숙했음" OR "친숙했습니다" -"안친숙" -filter:retweets',
            '"쾌적하다" OR "쾌적하네" OR "쾌적하군" OR "쾌적해" OR "쾌적함" OR "쾌적합니다" -"안쾌적" -filter:retweets',
            '"쾌적했다" OR "쾌적했네" OR "쾌적했어" OR "쾌적했음" OR "쾌적했습니다" -"안쾌적" -filter:retweets',
            '"통쾌하다" OR "통쾌하네" OR "통쾌하군" OR "통쾌해" OR "통쾌함" OR "통쾌합니다" -"안통쾌" -filter:retweets',
            '"통쾌했다" OR "통쾌했네" OR "통쾌했어" OR "통쾌했음" OR "통쾌했습니다" -"안통쾌" -filter:retweets',
            '"편안하다" OR "편안하네" OR "편안하군" OR "편안해" OR "편안함" OR "편안합니다" -"안편안" -filter:retweets',
            '"편안했다" OR "편안했네" OR "편안했어" OR "편안했음" OR "편안했습니다" -"안편안" -filter:retweets',
            '"함박웃음" -filter:retweets',
            '"행복하다" OR "행복하네" OR "행복하군" OR "행복해" OR "행복함" OR "행복합니다" -"안행복" -filter:retweets',
            '"후련하다" OR "후련하네" OR "후련하군" OR "후련해" OR "후련함" OR "후련합니다" -"안후련" -filter:retweets',
            '"후련했다" OR "후련했네" OR "후련했어" OR "후련했음" OR "후련했습니다" -"안후련" -filter:retweets',
            '"훌륭하다" OR "훌륭하네" OR "훌륭하군" OR "훌륭해" OR "훌륭함" OR "훌륭합니다" -"안훌륭" -filter:retweets',
            '"훌륭했다" OR "훌륭했네" OR "훌륭했어" OR "훌륭했음" OR "훌륭했습니다" -"안훌륭" -filter:retweets',
            '"흐뭇하다" OR "흐뭇하네" OR "흐뭇하군" OR "흐뭇해" OR "흐뭇함" OR "흐뭇합니다" -"안흐뭇" -filter:retweets',
            '"흐뭇했다" OR "흐뭇했네" OR "흐뭇했어" OR "흐뭇했음" OR "흐뭇했습니다" -"안흐뭇" -filter:retweets',
            '"흡족한다" OR "흡족하네" OR "흡족하군" OR "흡족해" OR "흡족함" OR "흡족합니다" -"안흡족" -filter:retweets',
            '"흡족했다" OR "흡족했네" OR "흡족했어" OR "흡족했음" OR "흡족했습니다" -"안흡족" -filter:retweets',
            '"흥겹다" OR "흥겹네" OR "흥겹군" OR "흥겨워" OR "흥겨움" OR "흥겹습니다" -"안흥겨" -"안흥겹" -filter:retweets',
            '"흥겨웠다" OR "흥겨웠네" OR "흥겨웠어" OR "흥겨웠음" OR "흥겨웠습니다" -"안흥겨웠" -filter:retweets',
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