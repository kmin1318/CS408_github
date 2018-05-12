t = 'asdf\nasdf\nasdf\nzxcv\nqwer\ntyui\ntyui\nghjk'
print (t)
l = t.splitlines()
print (l)
lst = list(set(l))
print(lst)
pt = '\n'.join(lst)
print(pt)