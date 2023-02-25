import requests
url='https://fixturedownload.com/feed/json/epl-2022'
response = requests.get(url)
currentmatchday=15
r=response.json()
# print(r)
for x in r:
    if x['HomeTeam'] == 'Man Utd' or x['AwayTeam'] == 'Man Utd':
        if x['MatchNumber']-currentmatchday >= 0:
            upcoming=x
            break
        prev=x
# print(prev)
# print(upcoming)
with open('./fixtures.txt', 'w', encoding='utf-8') as f:
    print(prev['MatchNumber'],prev['HomeTeam'],prev['HomeTeamScore'],prev['AwayTeamScore'],prev['AwayTeam'],)
    f.write(str(prev['MatchNumber']))
    f.write(' ')
    f.write(prev['HomeTeam'])
    f.write(' ')
    f.write(str(prev['HomeTeamScore']))
    f.write(' ')
    f.write(str(prev['AwayTeamScore']))
    f.write(' ')
    f.write(prev['AwayTeam'])
    f.write('\n')
    f.write(str(upcoming['MatchNumber']))
    f.write(' ')
    f.write(upcoming['HomeTeam'])
    f.write(' ')
    f.write('-')
    f.write(' ')
    f.write('-')
    f.write(' ')
    f.write(upcoming['AwayTeam'])
    print(upcoming['MatchNumber'],upcoming['HomeTeam'],'-','-',upcoming['AwayTeam'])




