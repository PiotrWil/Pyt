import json

import requests
from pyassert import *

s = requests.Session()
r = s.get("https://reqres.in/api/{}".format('users'), params = {'page': '2'})
print(r.status_code)
print(r.json())
print(r.json()['page']== 2)
print(r.json()['data'][0]['id']== 7)
assert_that(r.json()['support']['url']).is_equal_to('https://reqres.in/#support-heading')
assert_that(r.ok).is_true()
print(r.headers)


with open("jso") as plik:
    js = json.load(plik)
#params={'q': 'requests+language:python'},
str_json = json.dumps(js)
sr = '{"name": "pio", "job": "tester"}'
srr = json.loads(sr)
headers = {'Accept': 'application/json'}
response = requests.post('https://reqres.in/api/users', headers=headers, json=srr)
#json and data work both for dictionary
assert_that(response.status_code).is_equal_to(201)
a = response.json()
assert_that(a['name']).is_equal_to('pio')
print(response.headers['content-type'])
print(response.headers)




#with requests.Session() as session:
#    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
#    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
#print(response.headers)
#print(response.json())