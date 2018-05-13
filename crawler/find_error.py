import datetime

f = open("politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()

for keyword in keywords:
    lst = []
    f_name = keyword.split('"')[1]+".txt"
    import codecs
    with codecs.open(f_name, encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        
    print(f_name)
    if len(data) != 0:
        for line in data:
            dt = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M")
    