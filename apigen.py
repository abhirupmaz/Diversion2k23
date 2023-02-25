from flask import *
import json, time
import requests
import json
import pandas as pd
import random


app= Flask(__name__)

def fixture():
    url='https://fixturedownload.com/feed/json/epl-2022'
    response = requests.get(url)
    currentmatchday=28
    r=response.json()
    for x in r:
        if x['HomeTeam'] == 'Man Utd' or x['AwayTeam'] == 'Man Utd':
            if x['MatchNumber']-currentmatchday >= 0:
                upcoming=x
                break
            prev=x
    resp={'prev':prev,'upcoming':upcoming}
    return resp

def news():
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
    for x in r['articles']:
        if(('Manchester United' or'Man United' or 'Man Utd' or 'Man U') in x['description']):
            title.append(x['title'])
            url.append(x['url'])
            count-=1
            if(count==0):
                break
    randomlist = random.sample(range(0, 10), 3)
    temp={}
    resp={}
    c=0
    for x in randomlist:
        temp["title"]=title[x]
        temp["url"]=url[x]
        resp[c]=temp
        c+=1
        temp={}
    return resp

def standings():
    df = pd.read_csv("standings.csv")
    currentyear='2021-22'
    df=df.loc[df['Season'] == currentyear]
    df = df.iloc[:, 1:8]
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    parsed=json.dumps(parsed, indent=4)  
    return parsed
    # print(parsed)

@app.route('/fixtures',methods=['GET'])
def fixture_page():
    data_set=fixture()
    json_dump=json.dumps(data_set)
    return json_dump

@app.route('/news',methods=['GET'])
def news_page():
    data_set=news()
    json_dump=json.dumps(data_set)
    return json_dump

@app.route('/standings',methods=['GET'])
def standings_page():
    data_set=standings()
    return data_set

@app.route('/team/',methods=['GET'])
def team_page():
    team_query=str(request.args.get('team')) #/team/?team=TEAM_NAME
    data_set={'Team':f'{team_query}'}
    json_dump=json.dumps(data_set)
    return json_dump

@app.route('/',methods=['GET'])
def home_page():
    data_set={'Message':'Success'}
    json_dump=json.dumps(data_set)
    return json_dump

if __name__== '__main__':
    app.run()
