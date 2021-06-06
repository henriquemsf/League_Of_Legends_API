from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import requests
import json
import psycopg2

args={
    'owner' : 'Henrique',
    'start_date' : days_ago(1) 
}

dag = DAG(dag_id='LeagueOfLegends_ETL', default_args = args, schedule_interval=None)

#Token generated on the RiotGames API's website, expires in 24h
token = "*"

header = {
    "X-Riot-Token" : token
    }

def getAccountPuuid(**context):

    #First, we need to get the account puuid, which is used on the next API requests

    #Example: "BR1"
    tagLine = "BR1"
    #Nickname in-game
    gameName = "Henripster"

    url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"

    puuid = requests.get(url.format(gameName = gameName, tagLine = tagLine), headers = header).json()['puuid']

    context['ti'].xcom_push(key = 'puuid', value = puuid)

def getRecentMatches(**context):

    puuid = context['ti'].xcom_pull(task_ids = 'getAccountPuuid', key = 'puuid')

    #Using the account puuid, we can retrieve the account's recent matches id's
    #The number of matches retrieved defaults at 20, with a maximum of 100
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100"

    recentMatches = requests.get(url.format(puuid = puuid), headers = header).json()

    context['ti'].xcom_push(key = 'recentMatches', value = recentMatches)

def getMatchesData(**context):

    recentMatches = context['ti'].xcom_pull(task_ids = 'getRecentMatches', key = 'recentMatches')

    puuid = context['ti'].xcom_pull(task_ids = 'getAccountPuuid', key = 'puuid')

    url = "https://americas.api.riotgames.com/lol/match/v5/matches/{gameId}"

    #Creating an empty dataframe on which we will be adding our data
    matchDatas = pd.DataFrame(columns = ['GameMode', 'Duration', 'Timestamp', 'Win', 'Champion', 'Kills', 'Deaths', 'Assists', 'Vision_Score', 'Pink_Wards'])

    #For each match in the list retrieved, an API call will be used
    for match in recentMatches:

        data = requests.get(url.format(gameId = match), headers = header).json()
        
        try:
            #Since every match has 10 players, we will iterate through each one of them until the player puuid matches the puuid retrieved earlier
            for player in range(10):
                if data['info']['participants'][player]['puuid'] == puuid:

                    champion = data['info']['participants'][player]['championName']

                    assists = data['info']['participants'][player]['assists']

                    deaths = data['info']['participants'][player]['deaths']

                    pinkWardsBought = data['info']['participants'][player]['visionWardsBoughtInGame']

                    visionScore = data['info']['participants'][player]['visionScore']

                    kills = data['info']['participants'][player]['kills']

                    win = data['info']['participants'][player]['win']

                    gameMode = data['info']['gameMode']

                    duration = data['info']['gameDuration']

                    timestamp = data['info']['gameStartTimestamp']

                    #Organizing the data in a dict
                    matchData = {
                        'GameMode' : gameMode,
                        'Duration' : duration,
                        'Timestamp' : timestamp,
                        'Win' : win,
                        'Champion' : champion,
                        'Kills' : kills,
                        'Deaths' : deaths,
                        'Assists' : assists,
                        'Vision_Score' : visionScore,
                        'Pink_Wards' : pinkWardsBought,
                    }

                    #Appending the dict to the dataframe already created
                    matchDatas = matchDatas.append(matchData, ignore_index=True)

                    #Exiting the loop after matching the puuid
                    break       
            
        except Exception as e: 
            print(e)

    #converts the dataframe to json, so that it can be passed forward with xcom_push
    matchesData = matchDatas.to_json()

    context['ti'].xcom_push(key = 'matchesData', value = matchesData)

def databaseUpload(**context):

    matchesDatas = context['ti'].xcom_pull(task_ids = 'getMatchesData', key = 'matchesData')

    #Recreates the dataframe based on the json retrieved
    matchesDatas = pd.DataFrame.from_dict(json.loads(matchesDatas))

    #Connects to the database
    conn = psycopg2.connect(
        database='*', user='*', password='*',
        host='*', port='*'
    )

    conn.autocommit = True

    cursor = conn.cursor()

    #Before adding new Data to the database, this will retrieve the "Timestamp" column of the last 50 matches added to it
    cursor.execute(
    '''
    SELECT "Timestamp"
    FROM "MatchData"
    LIMIT 100
    '''
    )

    LastGames = []

    #Appends data to the list created
    for game in cursor.fetchall():
        LastGames.append(key[0])

    #Deletes any matches that are both in the Database and the dataframe to be appended
    #This is done to avoid any duplicate matches, since the Timestamp field has to be unique
    #Then, transform the dataframe's value to a list
    matchesDatas = matchesDatas[-matchesDatas['Timestamp'].isin(LastGames)].values.tolist()

    Query= ''' INSERT INTO "MatchData" ("GameMode", "Duration", "Timestamp", "Win", "Champion", "Kills", "Deaths", "Assists", "Vision_Score", "Pink_Wards") VALUES %s'''

    #Appends the matches data to the database, executing the query above for every match in the matchesDatas list
    psycopg2.extras.execute_values(cursor, Query, matchesDatas)
    
    cursor.close()
    conn.close() 

with dag:

    AccountPuuid = PythonOperator(
        task_id='getAccountPuuid',
        python_callable=getAccountPuuid,
        provide_context=True
    )
    RecentMatches = PythonOperator(
        task_id='getRecentMatches',
        python_callable=getRecentMatches,
        provide_context=True
    )
    MatchData = PythonOperator(
        task_id='getMatchesData',
        python_callable=getMatchesData,
        provide_context=True
    )

    dbUpload = PythonOperator(
        task_id='dbUpload',
        python_callable=databaseUpload,
        provide_context=True
    )

    AccountPuuid >> RecentMatches >> MatchData >> dbUpload

