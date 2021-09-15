import json
from os import path
from functools import reduce

def pala(a):
    for i in range(int(len(a)/2)):
        if a[i] != a[(len(a)-1-i)]:
            return False
        else:
            return True

print(pala('kajak'))

bb = {}
bb['user'] = [{"a":"a1", "b":"b1"}, {"a":"a2", "b":"b3"}]
cc = [{"a":"a1", "b":"b1"}, {"a":"a2", "b":"b4"}]
#bb['user'].append({"a":"a1", "b":"b1"})
#bb['user'].append({"a":"a2", "b":"b2"})
aa = json.dumps(bb)
dic = {}
if path.exists('pp') != True:
    with open("pp","x") as plik:
        json.dump(bb,plik)
with open('pp') as ppp:
            dic = json.load(ppp)
print(dic)
print(aa)


s = 'abcfrbvbv'
dic = {}
for letter in s:
    if letter in dic.keys():
        dic[letter] = dic[letter] + 1
    else:
        dic[letter] = 1
print(dic)
tab =[]
for a,b in dic.items():
    tab.append([a,b])

tab.sort(key = lambda x:x[1], reverse=True)
print(tab)
print(tab[0][1])

ff = [1,2,3,4,5]
gg=[]
for i in range(1, len(ff), 1):
    gg.append(ff[i])
gg.append(ff[0])

print(gg)

hh = [1,2,3,4,5]
o = 0
p = 0
for i in range(len(hh)-1, -1, -1):
    o = hh[i]
    hh[i] = p
    p = o

    if i==0:
        hh[len(hh)-1] = p

print(hh)



ii=[]
with open("readd", "r") as d:
    for a in d:
        ii.append(a)
print(ii)
stri = reduce(lambda x,y: x+y ,ii, "start")
print(stri.replace("\n",""))

tt=[]
with open("listList", "r") as line:
    for l in line:
        tt.append(l.split(" "))
ttt=[]
for k in tt:
    kk = [int(a) for a in k]
    a = reduce(lambda x,y: x+y, kk, 0)
    ttt.append(a)

print(ttt)






