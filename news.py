import requests
import random

url = ('https://newsapi.org/v2/everything?'
       'q=Manchester United&'
       'from=2023-02-01&'
       'sortBy=popularity&'
       'apiKey=88e48120bf2d439db0e9dea9a8975aca')
count=20
response = requests.get(url)
r=response.json()
title=[]
url=[]
# with open('./news.txt', 'w') as f:
for x in r['articles']:
    if(('Manchester United' or'Man United' or 'Man Utd' or 'Man U') in x['description']):
        # print(x['title'])
        # print(x['url'])
        title.append(x['title'])
        url.append(x['url'])
            # f.write(x['title'])
            # f.write('\n')
            # f.write(x['url'])
            # f.write('\n')
        count-=1
        if(count==0):
            break
        # print(r)

randomlist = random.sample(range(0, 10), 3)
with open('./news.txt', 'w', encoding='utf-8') as f:
    for x in randomlist:
        print(title[x])
        print(url[x])
        f.write(title[x])
        f.write('\n')
        f.write(url[x])
        f.write('\n')
    

