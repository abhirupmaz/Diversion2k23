import pandas as pd
import numpy as np
from scipy import stats 
data = pd.read_csv('results1.csv')
data.info()
data.head(3)
data.describe()
data['date']=data['date'].apply(lambda x : int(str.split(x,'-')[0]))
data['date'].value_counts()
#print(data['date'].min())

rec_data=data.loc[(data['date']>=2000)]
# rec_data.iloc[[rec_data.total_goals.argmax()]]
# print(rec_data.total_goals.mean())
from scipy.special import factorial
import numpy as np
#k is no. of event we want to find the probability of

def poisson(k,exp_events):
    minutes=90
    lam =(exp_events)
    p_k= np.exp(-lam)*np.power(lam,k)/factorial(k)
    #print(f'The probability of {k} goals in {minutes} minutes is {100*p_k:.2f}%.')
    return p_k
k=[]
p_k=[]
for i in range(10):
    p_k.append(poisson(i,2.74)*100)
    k.append(i)

def p_lessorequal(n_query,exp_events,quiet=True):
    p_n=poisson(np.arange(100),exp_events)
    p=p_n[:n_query+1].sum()
    if quiet:
        return p
    else:
        print(f'{exp_events} goals per game.Probability of {n_query} or fewer goals in 1 game: {100*p:.2f}%.')
    
def p_greaterorequal(n_query,exp_events,quiet=True):
    p = 1 - p_lessorequal(n_query,exp_events)
    if quiet:
        return p
    else:
        print(f'Probability of more than {n_query} goals in 1 game: {100*p:.2f}%.')
for i in range(1,10):
    p_greaterorequal(i,2.74,False)

events_per_min=(2.74/90)
np.random.seed(42)
events = np.random.choice([0,1],size=100000,
                          replace=True,
                          p=[1-events_per_min,events_per_min])
success_times = np.where(events==1)[0]
waiting_times = np.diff(success_times)
waiting_times[:10]

avg = []
events_per_minute=(2.74/90)
for i in range(10000):
    avg.append(np.mean(np.diff(np.where(np.random.choice([0, 1], size = 100000, replace=True, 
                          p=[1-events_per_minute, events_per_minute]) == 1)[0])))

print(len(data[(data.home_team =='England') & (data.away_team =='France')]))

data['home_team'] = data['home_team'].apply(lambda x: (''.join(x.split())).lower())
data['away_team'] = data['away_team'].apply(lambda x: (''.join(x.split())).lower())


counts = np.random.poisson(2.87,10)
print(int(stats.mode(counts)[0]))

def PredictScore():
    
    home_team = 'Manchester United'
    ht = (''.join(home_team.split())).lower()
    away_team = 'Liverpool'
    at = (''.join(away_team.split())).lower()
    
    if len(data[(data.home_team ==ht) & (data.away_team ==at)]) > 20:
        
        avg_home_score = data[(data.home_team ==ht) & (data.away_team ==at)].home_score.mean()
        avg_away_score = data[(data.home_team ==ht) & (data.away_team ==at)].away_score.mean()
        
        home_goal = int(stats.mode(np.random.poisson(avg_home_score,100000))[0])                    
        away_goal = int(stats.mode(np.random.poisson(avg_away_score,100000))[0])
        
    else:
        avg_home_goal_conceded = data[(data.home_team ==ht)].away_score.mean()
        avg_away_goal_scored   = data[(data.away_team ==at)].away_score.mean()
        away_goal = int(stats.mode(np.random.poisson(1/2*(avg_home_goal_conceded+avg_away_goal_scored),100000))[0])
        
        avg_away_goal_conceded = data[(data.home_team ==at)].home_score.mean()
        avg_home_goal_scored   = data[(data.away_team ==ht)].home_score.mean()
        home_goal = int(stats.mode(np.random.poisson(1/2*(avg_away_goal_conceded+avg_home_goal_scored),100000))[0])
    
    avg_total_score = int(stats.mode(
        np.random.poisson((data[(data.home_team ==ht) & (data.away_team ==at)].total_goals.mean()),100000))[0])
    
    #print(f'Expected total goals are {avg_total_score}')
    #print(f'They have played {len(data[(data.home_team ==ht) & (data.away_team ==at)])} matches')
    print(f' {home_team} {home_goal}:{away_goal} {away_team}')
    resp={"pred":f" {home_team} {home_goal}:{away_goal} {away_team}"}
    return resp

PredictScore()