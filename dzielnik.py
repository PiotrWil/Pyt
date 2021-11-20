from functools import reduce


def GCD(b, a):
    if a == 0:
        return b
    return GCD(a, b % a)


print(GCD(15, 80))


def palidrome(a):
    for i in range(int(len(a) / 2)):
        if a[i] != a[len(a) - 1 - i]:
            return "Nie jest polidrome"
        else:
            return "Jest"


print(palidrome("abccbt"))


def add(a):
    s = []
    for x in a.keys():
        s.append(x)
    d = reduce(lambda x, y: x + y, s)

    print(d)


b = {1: 1, 2: 2, 4: 3}
add(b)


def undef(**blabla):
    suma = 0
    for y in blabla.values():
        suma+=y
    print(suma)


undef(a=1,b=2,c=6)

dd = False
if dd !=True:
    print("aaa")

lista = [1,4,6,7,8]
for i in range(len(lista)-1,-1,-1):
    print(lista[i])

def sum(w):
    s = 0
    for i in w:
        s+=i
    return s

ww =[]

for i in range(3):
    num = int(input("Hej, dej numer"))
    ww.append(num)
print(sum(ww))


uu = [input("ddd") for i in range(3)]
print(uu)
7

def met(a):
    for x in range(a):
        yield x

print(list(met(5)))
for r in met(5):
    print(r)


stre = 'Hi'
print([stre for stre in range(2)])


def sum13(nums):
  sum = 0
  if nums[0] == 13:
    sum = 0
  else:
    sum = nums[0]

  for i in range(1, len(nums)):
    if(nums[i] == 13 or nums[i-1] == 13):
      continue
    sum = sum + nums[i]
  return sum

print(sum13([13,4,6,14,13,7]))


def so(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)

so([7,6,5,1,2,0])