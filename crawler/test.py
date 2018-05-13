# -*- coding: utf-8 -*-

f_name = "강원삼척시장.txt"
f = open(f_name, "r", -1, "utf-8")
data = f.read().splitlines()
print(data)
f.close()