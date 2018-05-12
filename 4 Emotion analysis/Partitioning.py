import codecs
import random

train_data = []
test_data = []
train = open("train_data.txt", 'w', -1, "utf-8")
test = open("test_data.txt", 'w', -1, "utf-8")
Anger = codecs.open("Anger.txt", encoding='utf-8')
Disgust = codecs.open("Disgust.txt", encoding='utf-8')
Fear = codecs.open("Fear.txt", encoding='utf-8')
Happy = codecs.open("Happy.txt", encoding='utf-8')
Sad = codecs.open("Sad.txt", encoding='utf-8')
Surprise = codecs.open("Surprise.txt", encoding='utf-8')

for line in Anger.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '0')
    else:
        test_data.append(line + '\t' + '0')
        
for line in Disgust.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '0')
    else:
        test_data.append(line + '\t' + '0')
        
for line in Fear.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '1')
    else:
        test_data.append(line + '\t' + '1')
        
for line in Happy.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '2')
    else:
        test_data.append(line + '\t' + '2')
        
for line in Sad.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '3')
    else:
        test_data.append(line + '\t' + '3')
        
for line in Surprise.read().splitlines():
    if random.randint(1,10) < 8:
        train_data.append(line + '\t' + '1')
    else:
        test_data.append(line + '\t' + '1')
        
train_text = '\n'.join(train_data)
test_text = '\n'.join(test_data)

train.write(train_text)
test.write(test_text)

train.close()
test.close()