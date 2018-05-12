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

keywords = ['"감개무량하다" OR "감개무량하네" OR "감개무량하군" OR "감개무량해요" OR "감개무량함" OR "감개무량합니다" -"안감개무량" -filter:retweets',
            '"감개무량했다" OR "감개무량했네" OR "감개무량했어" OR "감개무량했음" OR "감개무량했습니다" -"안감개무량" -filter:retweets',
            '"감격한다" OR "감격해요" OR "감격함" OR "감격합니다" -"안감격" -filter:retweets',
            '"감격했다" OR "감격했네" OR "감격했어" OR "감격했음" OR "감격했습니다" -"안감격" -"괜히감격했" -filter:retweets',
            '"감동한다" OR "감동해요" OR "감동함" OR "감동합니다" -"안감동" -filter:retweets',
            '"감동했다" OR "감동했네" OR "감동했어" OR "감동했음" OR "감동했습니다" -"안감동" -"괜히감동했" -filter:retweets',
            '"감미롭다" OR "감미롭네" OR "감미롭군" OR "감미로워요" OR "감미로움" OR "감미롭습니다" -"안감미" -filter:retweets',
            '"감미로웠다" OR "감미로웠네" OR "감미로웠어" OR "감미로웠음" OR "감미로웠습니다" -"안감미로웠" -filter:retweets',
            '"감복한다" OR "감복해요" OR "감복함" OR "감복합니다" -"안감복" -filter:retweets',
            '"감복했다" OR "감복했네" OR "감복했어" OR "감복했음" OR "감복했습니다" -"안감복" -"괜히감복했" -filter:retweets',
            '"감사하다" OR "감사한다" OR "감사하네" OR "감사하군" OR "감사해요" OR "감사함" OR "감사합니다" -"안감사" -filter:retweets',
            '"감사했다" OR "감사했네" OR "감사했어" OR "감사했음" OR "감사했습니다" -"안감사" -"괜히감사했" -filter:retweets',
            '"경쾌하다" OR "경쾌하네" OR "경쾌하군" OR "경쾌해요" OR "경쾌함" OR "경쾌합니다" -"안경쾌" -filter:retweets',
            '"경쾌했다" OR "경쾌했네" OR "경쾌했어" OR "경쾌했음" OR "경쾌했습니다" -"안경쾌" -filter:retweets',
            '"고맙다" OR "고맙네" OR "고맙군" OR "고마워요" OR "고마움" OR "고맙습니다" -"안고마" -"안고맙" -filter:retweets',
            '"고마웠다" OR "고마웠네" OR "고마웠어" OR "고마웠음" OR "고마웠습니다" -"안고마웠" -filter:retweets',
            '"근사하다" OR "근사하네" OR "근사하군" OR "근사해요" OR "근사함" OR "근사합니다" -"안근사" -filter:retweets',
            '"근사했다" OR "근사했네" OR "근사했어" OR "근사했음" OR "근사했습니다" -"안근사" -filter:retweets',
            '"기분좋다" OR "기분좋네" OR "기분좋군" OR "기분좋아요" OR "기분좋음" OR "기분좋습니다" -"안기분좋" -filter:retweets',
            '"기분좋았다" OR "기분좋았네" OR "기분좋았어" OR "기분좋았음" OR "기분좋았습니다" -"안기분좋았" -"괜히기분좋았" -filter:retweets',
            '"기쁘다" OR "기쁘네" OR "기쁘군" OR "기뻐요" OR "기쁩니다" -"안기쁘" -"안기쁩" -filter:retweets',
            '"기뻤다" OR "기뻤네" OR "기뻤어" OR "기뻤음" OR "기뻤습니다" -"안기뻤" -filter:retweets',
            '"낭만적이다" OR "낭만적이네" OR "낭만적이군" OR "낭만적이에요" OR "낭만적임" OR "낭만적입니다" -"안낭만적" -filter:retweets',
            '"낭만적이었다" OR "낭만적이었네" OR "낭만적이었어" OR "낭만적이었음" OR "낭만적이었습니다" -"안낭만적이었" -filter:retweets',
            '"달갑다" OR "달갑네" OR "달갑군" OR "달가워요" OR "달가움" OR "달갑습니다" -"안달가" -"안달갑" -filter:retweets',
            '"달가웠다" OR "달가웠네" OR "달가웠어" OR "달가웠음" OR "달가웠습니다" -"안달가웠" -filter:retweets',
            '"대견하다" OR "대견하네" OR "대견하군" OR "대견해요" OR "대견함" OR "대견합니다" -"안대견" -filter:retweets',
            '"대견했다" OR "대견했네" OR "대견했어" OR "대견했음" OR "대견했습니다" -"안대견" -filter:retweets',
            '"따뜻하다" OR "따뜻하네" OR "따뜻하군" OR "따뜻해요" OR "따뜻함" OR "따뜻합니다" -"안따뜻" -filter:retweets',
            '"따스하다" OR "따스하네" OR "따스하군" OR "따스해요" OR "따스함" OR "따스합니다" -"안따스" -filter:retweets',
            '"만족한다" OR "만족하네" OR "만족해요" OR "만족함" OR "만족합니다" -"안만족" -filter:retweets',
            '"만족했다" OR "만족했네" OR "만족했어" OR "만족했음" OR "만족했습니다" -"안만족" -filter:retweets',
            '"반갑다" OR "반갑네" OR "반갑군" OR "반가워요" OR "반가움" OR "반갑습니다" -"안반가" -"안반갑" -filter:retweets',
            '"반가웠다" OR "반가웠네" OR "반가웠어" OR "반가웠음" OR "반가웠습니다" -"안반가웠" -filter:retweets',
            '"방그레" OR "방글방글" OR "방긋" -filter:retweets',
            '"보기좋다" OR "보기좋네" OR "보기좋군" OR "보기좋아요" OR "보기좋음" OR "보기좋습니다" -"안보기좋" -filter:retweets',
            '"보기좋았다" OR "보기좋았네" OR "보기좋았어" OR "보기좋았음" OR "보기좋았습니다" -"안보기좋았" -filter:retweets',
            '"뿌듯하다" OR "뿌듯하네" OR "뿌듯하군" OR "뿌듯해요" OR "뿌듯함" OR "뿌듯합니다" -"안뿌듯" -filter:retweets',
            '"뿌듯했다" OR "뿌듯했네" OR "뿌듯했어" OR "뿌듯했음" OR "뿌듯했습니다" -"안뿌듯" -filter:retweets',
            '"사랑스럽다" OR "사랑스럽네" OR "사랑스럽군" OR "사랑스러워요" OR "사랑스러움" OR "사랑스럽습니다" -"안사랑스" -filter:retweets',
            '"상쾌하다" OR "상쾌하네" OR "상쾌하군" OR "상쾌해요" OR "상쾌함" OR "상쾌합니다" -"안상쾌" -filter:retweets',
            '"상쾌했다" OR "상쾌했네" OR "상쾌했어" OR "상쾌했음" OR "상쾌했습니다" -"안상쾌" -filter:retweets',
            '"상큼하다" OR "상큼하네" OR "상큼하군" OR "상큼해요" OR "상큼함" OR "상큼합니다" -"안상큼" -filter:retweets',
            '"설렌다" OR "설레네" OR "설레군" OR "설레요" OR "설렙니다" -"안설레" -filter:retweets',
            '"설레였다" OR "설레였네" OR "설레였어" OR "설레였음" OR "설레였습니다" -"안설레였" -filter:retweets',
            '"신난다" OR "신나네" OR "신나군" OR "신나요" OR "신남" OR "신납니다" -"안신나" -"안신남" -"안신납" -filter:retweets',
            '"신명난다" OR "신명나네" OR "신명나군" OR "신명나요" OR "신명남" OR "신명납니다" -"안신명" -filter:retweets',
            '"신명났다" OR "신명났네" OR "신명났어" OR "신명났음" OR "신명났습니다" -"안신명났" -filter:retweets',
            '"신바람난다" OR "신바람나네" OR "신바람나군" OR "신바람나는군" OR "신바람나요" OR "신바람남" OR "신바람납니다" -"안신바람" -filter:retweets',
            '"신바람났다" OR "신바람났네" OR "신바람났어" OR "신바람났음" OR "신바람났습니다" -"안신바람났" -"괜히신바람났" -filter:retweets',
            '"싱글벙글하다" OR "싱글벙글하네" OR "싱글벙글하군" OR "싱글벙글해요" OR "싱글벙글함" OR "싱글벙글합니다" -"안싱글벙글" -filter:retweets',
            '"싱글벙글했다" OR "싱글벙글했네" OR "싱글벙글했어" OR "싱글벙글했음" OR "싱글벙글했습니다" -"안싱글벙글" -"괜히싱글벙글했" -filter:retweets',
            '"예쁘다" OR "예쁘네" OR "예쁘군" OR "예뻐요" OR "예쁨" OR "예쁩니다" -"안예쁘" -"안예뻐" -"안예쁨" -"안예쁩" -filter:retweets',
            '"우아하다" OR "우아하네" OR "우아하군" OR "우아해요" OR "우아함" OR "우아합니다" -"안우아" -filter:retweets',
            '"우아했다" OR "우아했어" OR "우아했음" OR "우아했습니다" -"안우아" -filter:retweets',
            '"유쾌하다" OR "유쾌하네" OR "유쾌하군" OR "유쾌해요" OR "유쾌함" OR "유쾌합니다" -"안유쾌" -filter:retweets',
            '"유쾌했다" OR "유쾌했네" OR "유쾌했어" OR "유쾌했음" OR "유쾌했습니다" -"안유쾌" -filter:retweets',
            '"재미있다" OR "재미있네" OR "재미있군" OR "재미있어요" OR "재미있음" OR "재미있습니다" -"안재미있" -filter:retweets',
            '"재미있었다" OR "재미있었네" OR "재미있었어" OR "재미있었음" OR "재미있었습니다" -"안재미있었" -filter:retweets',
            '"좋다" OR "좋네" OR "좋군" OR "좋아요" OR "좋음" OR "좋습니다" -"안좋" -filter:retweets',
            '"좋아한다" OR "좋아해요" OR "좋아함" OR "좋아합니다" -"안좋아" -filter:retweets',
            '"즐겁다" OR "즐겁네" OR "즐겁군" OR "즐거워요" OR "즐거움" OR "즐겁습니다" -"안즐거" -"안즐겁" -filter:retweets',
            '"즐거웠다" OR "즐거웠네" OR "즐거웠어" OR "즐거웠음" OR "즐거웠습니다" -"안즐거웠" -filter:retweets',
            '"친근하다" OR "친근하네" OR "친근하군" OR "친근해요" OR "친근함" OR "친근합니다" -"안친근" -filter:retweets',
            '"친근했다" OR "친근했네" OR "친근했어" OR "친근했음" OR "친근했습니다" -"안친근" -filter:retweets',
            '"친숙하다" OR "친숙하네" OR "친숙하군" OR "친숙해요" OR "친숙함" OR "친숙합니다" -"안친숙" -filter:retweets',
            '"친숙했다" OR "친숙했네" OR "친숙했어" OR "친숙했음" OR "친숙했습니다" -"안친숙" -filter:retweets',
            '"쾌적하다" OR "쾌적하네" OR "쾌적하군" OR "쾌적해요" OR "쾌적함" OR "쾌적합니다" -"안쾌적" -filter:retweets',
            '"쾌적했다" OR "쾌적했네" OR "쾌적했어" OR "쾌적했음" OR "쾌적했습니다" -"안쾌적" -filter:retweets',
            '"통쾌하다" OR "통쾌하네" OR "통쾌하군" OR "통쾌해요" OR "통쾌함" OR "통쾌합니다" -"안통쾌" -filter:retweets',
            '"통쾌했다" OR "통쾌했네" OR "통쾌했어" OR "통쾌했음" OR "통쾌했습니다" -"안통쾌" -filter:retweets',
            '"편안하다" OR "편안하네" OR "편안하군" OR "편안해요" OR "편안함" OR "편안합니다" -"안편안" -filter:retweets',
            '"편안했다" OR "편안했네" OR "편안했어" OR "편안했음" OR "편안했습니다" -"안편안" -filter:retweets',
            '"함박웃음" -filter:retweets',
            '"행복하다" OR "행복하네" OR "행복하군" OR "행복해요" OR "행복함" OR "행복합니다" -"안행복" -filter:retweets',
            '"후련하다" OR "후련하네" OR "후련하군" OR "후련해요" OR "후련함" OR "후련합니다" -"안후련" -filter:retweets',
            '"후련했다" OR "후련했네" OR "후련했어" OR "후련했음" OR "후련했습니다" -"안후련" -filter:retweets',
            '"훌륭하다" OR "훌륭하네" OR "훌륭하군" OR "훌륭해요" OR "훌륭함" OR "훌륭합니다" -"안훌륭" -filter:retweets',
            '"훌륭했다" OR "훌륭했네" OR "훌륭했어" OR "훌륭했음" OR "훌륭했습니다" -"안훌륭" -filter:retweets',
            '"흐뭇하다" OR "흐뭇하네" OR "흐뭇하군" OR "흐뭇해요" OR "흐뭇함" OR "흐뭇합니다" -"안흐뭇" -filter:retweets',
            '"흐뭇했다" OR "흐뭇했네" OR "흐뭇했어" OR "흐뭇했음" OR "흐뭇했습니다" -"안흐뭇" -filter:retweets',
            '"흡족한다" OR "흡족하네" OR "흡족하군" OR "흡족해요" OR "흡족함" OR "흡족합니다" -"안흡족" -filter:retweets',
            '"흡족했다" OR "흡족했네" OR "흡족했어" OR "흡족했음" OR "흡족했습니다" -"안흡족" -filter:retweets',
            '"흥겹다" OR "흥겹네" OR "흥겹군" OR "흥겨워요" OR "흥겨움" OR "흥겹습니다" -"안흥겨" -"안흥겹" -filter:retweets',
            '"흥겨웠다" OR "흥겨웠네" OR "흥겨웠어" OR "흥겨웠음" OR "흥겨웠습니다" -"안흥겨웠" -filter:retweets',
            ]

file = open("Happy.txt", 'w', -1, "utf-8")

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