# -*- coding: utf-8 -*-

import tweepy
import re

consumer_key = 'jYCKoZ7VJ7MRjUIxAr7ZT6IZ2'

consumer_secret = '8BFrc01U3bodfN3oMC75jZO0a9prF6KQUny1H44Kg2eY1r6nzn'

access_token = '972705355154079744-5M7h50L3jqEZgdtwh4CTQwFcPYrbg3r'

access_token_secret = 'dY675bItOVShdHpyG9WAYyevlpcD8LB8qHZJ45qzTPES3'


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

keywords = ['"개새끼" OR "개쌍년" OR "개자식" -filter:retweets',
            '"격노한다" OR "격노했다" OR "격노했네" OR "격노했어" OR "격노했음" OR "격노했습니다" OR "격노함" OR "격노합니다" -"안격노" -"괜히격노했" -filter:retweets',
            '"격분한다" OR "격분했다" OR "격분했네" OR "격분했어" OR "격분했음" OR "격분했습니다" OR "격분함" OR "격분합니다" -"안격분" -"괜히격분했" -filter:retweets',
            '"격해진다" OR "격해지네" OR "격해지는군" OR "격해져요" OR "격해졌다" OR "격해졌네" OR "격해졌어" OR "격해졌음" OR "격해졌습니다" OR "격해짐" OR "격해집니다" -"안격해" -"괜히격해졌" -filter:retweets',
            '"괘씸하다" OR "괘씸하네" OR "괘씸하군" OR "괘씸해요" OR "괘씸했다" OR "괘씸했네" OR "괘씸했어" OR "괘씸했음" OR "괘씸했습니다" OR "괘씸함" OR "괘씸합니다" -"안괘씸" -"괜히괘씸했" -filter:retweets',
            '"그자식" -filter:retweets',
            '"기분나쁘다" OR "기분나쁘네" OR "기분나쁘군" OR "기분나빠요" OR "기분나빴다" OR "기분나빴네" OR "기분나빴어" OR "기분나빴음" OR "기분나빴습니다" OR "기분나쁨" OR "기분나빴습니다" -"안기분나" -"괜히기분나빴" -filter:retweets',
            '"노여워한다" OR "노여워했다" OR "노여워했음" OR "노여워했습니다" OR "노여워함" -"안노여워" -"괜히노여워했" -filter:retweets',
            '"니미" OR "미친개" OR "버럭" -filter:retweets',
            '"분개한다" OR "분개했다" OR "분개했네" OR "분개했어" OR "분개했음" OR "분개했습니다" OR "분개함" OR "분개합니다" -"안분개" -"괜히분개했" -filter:retweets',
            '"분노한다" OR "분노했다" OR "분노했네" OR "분노했어" OR "분노했음" OR "분노했습니다" OR "분노함" OR "분노합니다" -"안분노" -"괜히분노했" -filter:retweets',
            '"빌어먹을" OR "싸가지" OR "쌍년" OR "쌍놈" OR "씨부랄" OR "씨부렁" OR "씩씩거리" OR "씹새끼" OR "아이씨" -filter:retweets',
            '"약오른다" OR "약오르네" OR "약오르군" OR "약올라요" OR "약올랐다" OR "약올랐네" OR "약올랐어" OR "약오름" OR "약오릅니다" -"안약오" -"안약올" -"괜히약올랐" -filter:retweets',
            '"얄밉다" OR "얄밉네" OR "얄밉군" OR "얄미워요" OR "얄미웠다" OR "얄미웠네" OR "얄미웠어" OR "얄미웠음" OR "얄미웠습니다" OR "얄미움" OR "얄밉습니다" -"안얄미" -"안얄밉" -"괜히얄미웠" -filter:retweets',
            '"어이없다" OR "어이없네" OR "어이없군" OR "어이없어요" OR "어이없었다" OR "어이없었네" OR "어이없었어" OR "어이없음" OR "어이없었습니다" OR "어이없음" OR "괘씸합니다" -"안괘씸" -"괜히괘씸했" -filter:retweets',
            '"옘병할" OR "우라질" OR "울화통" OR "웬수" OR "제기랄" -filter:retweets',
            '"증오한다" OR "증오하네" OR "증오해요" OR "증오했다" OR "증오했네" OR "증오했어" OR "증오했음" OR "증오했습니다" OR "증오함" OR "증오합니다" -"안증오" -"괜히증오했" -filter:retweets',
            '"진노한다" OR "진노했다" OR "진노했네" OR "진노했어" OR "진노했음" OR "진노했습니다" OR "진노함" OR "진노합니다" -"안진노" -"괜히진노했" -filter:retweets',
            '"짜증난다" OR "짜증나네" OR "짜증나군" OR "짜증나는군" OR "짜증나요" OR "짜증났다" OR "짜증났네" OR "짜증났어" OR "짜증났음" OR "짜증났습니다" OR "짜증남" OR "짜증납니다" -"안짜증" -"괜히짜증났" -filter:retweets',
            '"치떨린다" OR "치떨리네" OR "치떨리는군" OR "치떨려요" OR "치떨렸다" OR "치떨렸네" OR "치떨렸어" OR "치떨렸음" OR "치떨렸습니다" OR "치떨림" OR "치떨립니다" -"안치떨" -"괜히치떨렸" -filter:retweets',
            '"치가떨린다" OR "치가떨리네" OR "치가떨리는군" OR "치가떨려요" OR "치가떨렸다" OR "치가떨렸네" OR "치가떨렸어" OR "치가떨렸음" OR "치가떨렸습니다" OR "치가떨림" OR "치가떨립니다" -"안치가떨" -"괜히치가떨렸" -filter:retweets',
            '"치밀어오른다" OR "치밀어오르네" OR "치밀어오르는군" OR "치밀어올라요" OR "치밀어올랐다" OR "치밀어올랐네" OR "치밀어올랐어" OR "치밀어올랐음" OR "치밀어올랐습니다" OR "치밀어오름" OR "치밀어올랐습니다" -"안치밀어" -"괜히치밀어올랐" -filter:retweets',
            ]

file = open("Anger.txt", 'w', -1, "utf-8")

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