# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
from os import path
from functools import reduce
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print_hi("Piotr")

a = [1, 7, 4, 5]
v = lambda x: x

print([x * x for x in a])

w = sorted(a, key=v)
print(a)
print(w)


def sortuj(variable):
    return sorted(variable, key=v)


print(sortuj(a))

def silnia(r):
    if r < 0:
        return 'I am not able'
    elif r <= 1:
        return 1
    else:
        return r * silnia(r - 1)


print(silnia(-7))

a = [{"a":1, "b":2},{"a":-3, "b":-5} ]
a.sort(key = lambda x:x["b"])
print(a)

c = 'abcdabc'

def createDic(a):
    b = {}
    print(len(a))
    for i in a:
        if i in b:
            b[i] = b[i]+1
        else:
            b[i] = 1
    return b


print(createDic(c))

#if path.exists('aa'):
#   print("File exists")
#else:
#    open("aa", "x")
#with open("aa", "a") as d:
#    d.write("a\n")


b = [3,6,1,9,3,8,4,2]
for i in range(len(b)-1):
    for j in range(len(b)-1-i):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]


print(b)
h = ['ww', 'gg', 'nn']
print(random.choice(h))

str = 'abcedf'
for a in str:
    print(a)

str1 = [1,5,7,3,8]
for digit in str1:
    print(digit)
print(str1[1])

for i in range(len(str)-1, -1, -1):
    print(str[i])

f = lambda x,y: x+y

print(reduce(f, str1))
print(list(map(lambda x: x+1, str1)))


option = webdriver.ChromeOptions()

option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
driver = webdriver.Chrome(options= option, executable_path='C:\\dabag-dev\\chromedriver.exe')
driver.get("https://www.sport.pl/sport-hp/0,0.html")
driver.maximize_window()
sleep(1)
title = driver.title
print(title)
assert title == 'Sport na Sport.pl - Wyniki i wiadomości sportowe'

el1 = driver.find_element_by_xpath("//li/a[@title='Piłka nożna ']")
action = ActionChains(driver)
el2 = driver.find_element_by_xpath("//li/a[@title='Kadra ' and ./parent::li[@id='e3_4']]")
action.move_to_element(el1).perform()

wait = WebDriverWait(driver, 2).until(EC.visibility_of(el2))
#sleep(2)
#el2 = driver.find_element_by_xpath("//li/a[@title='Kadra ' and ./parent::li[@id='e3_4']]")
el2.click()

sleep(2)

driver.quit()
