# -*- coding: utf-8 -*-

import codecs
import re

def remove_emoji(string):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣a-zA-Z0-9\x00-\x7f]+')
    result = hangul.sub('', string)
    return result

train_data = []
train = open("train_data_non_EMOJI.txt", 'w', -1, "utf-8")
Anger = codecs.open("Anger.txt", encoding='utf-8')
Disgust = codecs.open("Disgust.txt", encoding='utf-8')
Fear = codecs.open("Fear.txt", encoding='utf-8')
Happy = codecs.open("Happy.txt", encoding='utf-8')
Sad = codecs.open("Sad.txt", encoding='utf-8')
Surprise = codecs.open("Surprise.txt", encoding='utf-8')
AngerData = codecs.open("AngerData.txt", encoding='utf-8')
FearData = codecs.open("FearData.txt", encoding='utf-8')
HappyData = codecs.open("HappyData.txt", encoding='utf-8')
SadData = codecs.open("SadData.txt", encoding='utf-8')

n_anger = 0
n_disgust = 0
n_fear = 0
n_happy = 0
n_sad = 0
n_surprise = 0

for line in list(set(Anger.read().splitlines()) - set(AngerData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '0')
    n_anger = n_anger + 1
        
for line in list(set(Disgust.read().splitlines()) - set(AngerData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '0')
    n_disgust = n_disgust + 1
        
for line in list(set(Fear.read().splitlines()) - set(FearData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '1')
    n_fear = n_fear + 1
        
for line in list(set(Happy.read().splitlines()) - set(HappyData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '2')
    n_happy = n_happy + 1
        
for line in list(set(Sad.read().splitlines()) - set(SadData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '3')
    n_sad = n_sad + 1
        
for line in list(set(Surprise.read().splitlines()) - set(FearData.read().splitlines())):
    new_text = remove_emoji(line)
    train_data.append(new_text + '\t' + '1')
    n_surprise = n_surprise + 1
        
train_text = '\n'.join(train_data)

train.write(train_text)

print(n_anger, n_disgust, n_fear, n_happy, n_sad, n_surprise)

train.close()