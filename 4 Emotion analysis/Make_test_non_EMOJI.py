# -*- coding: utf-8 -*-

import codecs
import re

def remove_emoji(string):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣a-zA-Z0-9\x00-\x7f]+')
    result = hangul.sub('', string)
    return result

Anger = codecs.open("AngerData.txt", encoding='utf-8')
Fear = codecs.open("FearData.txt", encoding='utf-8')
Happy = codecs.open("HappyData.txt", encoding='utf-8')
Sad = codecs.open("SadData.txt", encoding='utf-8')
test = open("test_data_non_EMOJI.txt", 'w', -1, "utf-8")

test_data = []
nanger = 0
nfear = 0
nhappy = 0
nsad = 0

for line in list(set(Anger.read().splitlines())):
    new_text = remove_emoji(line)
    test_data.append(new_text + '\t' + '0')
    nanger = nanger + 1
        
for line in list(set(Fear.read().splitlines())):
    new_text = remove_emoji(line)
    test_data.append(new_text + '\t' + '1')
    nfear = nfear + 1
        
for line in list(set(Happy.read().splitlines())):
    new_text = remove_emoji(line)
    test_data.append(new_text + '\t' + '2')
    nhappy = nhappy + 1
        
for line in list(set(Sad.read().splitlines())):
    new_text = remove_emoji(line)
    test_data.append(new_text + '\t' + '3')
    nsad = nsad + 1
    
test_text = '\n'.join(test_data)

test.write(test_text)

print(nanger, nfear, nhappy, nsad)

test.close()