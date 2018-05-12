import codecs

Anger = codecs.open("AngerData.txt", encoding='utf-8')
Fear = codecs.open("FearData.txt", encoding='utf-8')
Happy = codecs.open("HappyData.txt", encoding='utf-8')
Sad = codecs.open("SadData.txt", encoding='utf-8')
test = open("test_data.txt", 'w', -1, "utf-8")

test_data = []
nanger = 0
nfear = 0
nhappy = 0
nsad = 0

for line in list(set(Anger.read().splitlines())):
    test_data.append(line + '\t' + '0')
    nanger = nanger + 1
        
for line in list(set(Fear.read().splitlines())):
    test_data.append(line + '\t' + '1')
    nfear = nfear + 1
        
for line in list(set(Happy.read().splitlines())):
    test_data.append(line + '\t' + '2')
    nhappy = nhappy + 1
        
for line in list(set(Sad.read().splitlines())):
    test_data.append(line + '\t' + '3')
    nsad = nsad + 1
    
test_text = '\n'.join(test_data)

test.write(test_text)

print(nanger, nfear, nhappy, nsad)

test.close()