t = '@asdf @sdfds @asdfsdkjf good luck!\nI love you!\nYou are good~~ https://t.co/PRJL6gRAl8'
print(t)

l = t.splitlines()
print(l)
if l[0][0] == '@':
    l2 = l[0].split(' ')
    print(l2)
    i = 1
    while i < len(l2):
        if l2[i][0] == '@':
            i = i + 1
        else:
            print(i)
            nt = ' '.join(l2[i:])
            break
    l[0] = nt
print(l)

if 'http' in l[-1]:
    l3 = l[-1].split(' ')
    nt = ' '.join(l3[:-1])
    print(nt)
    l[-1] = nt
    
print(l)
pt = ' '.join(l)
print(pt)
    
        
