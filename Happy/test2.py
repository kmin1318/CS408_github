import re

t = '@asdf @sdfds @asdfsdkjf good luck!\nI love you!\nYou are good~~ https://t.co/PRJL6gRAl8'
t1 = re.sub(r"@\S+", "", t)
t2 = re.sub(r"http\S+", "", t1)
t3 = t2.strip()
l = t3.splitlines()
pt = ' '.join(l)
print(pt)

    
        
