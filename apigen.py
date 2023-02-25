from flask import *
import json, time
import requests
import json
import pandas as pd


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
