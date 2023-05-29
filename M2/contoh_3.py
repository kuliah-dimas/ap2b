from urllib import request
import json


url = "https://jsonplaceholder.typicode.com/posts"
response = request.urlopen(url)
data = json.loads(response.read())

for x in range(len(data)):
    print(data[x]['title'])


for i in range(len(data)):
    print(data[i]["title"])
    print()
