import chessstats
import math

def setup(username):
    data=chessstats.getstats(username)
    data1=chessstats.getstats1(username)
    data2=chessstats.getstats2(username)
    return([data,data1,data2])

def rapidrating(data): #data
    stats = data['stats']
    rapid_stats = stats[0]
    rapid_rating = rapid_stats['stats']['rating']
    return(rapid_rating)

def winrate(data): #data
    stats = data['stats']
    rapid_stats = stats[0]
    rapid_wins = rapid_stats['stats']['total_win_count']
    rapid_games = rapid_stats['stats']['total_game_count']
    
    chance = (int(rapid_wins)/int(rapid_games))
    return(str(math.ceil(chance*100)/100) + '%')

def getavatarurl(data): #data1
    return(data['avatarUrl'])

def joindate(data): #data1
    return(data['joinDate'])

def country(data): #data1
    return(data['countryName'])

def ismod(data): #data1
    if data['membership']['level'] >= 80:
        return(1)
    else:
        return(0)

def getleague(data):#data2
    divison = data['division']
    league = divison['league']
    name = league['name']
    badge = league['badge']
    return([name,badge])

def getall(username):
    alldata = setup(username)
    rapidrating_count = rapidrating(alldata[0]) #0
    winrate_count = winrate(alldata[0]) #1
    avatar = getavatarurl(alldata[1]) #2
    joindate_count = joindate(alldata[1]) #3
    country_code = country(alldata[1]) #4
    ismod_ = ismod(alldata[1]) #5
    league = getleague(alldata[2]) #6
    print(ismod_)
    return([rapidrating_count,winrate_count,avatar,joindate_count,country_code,ismod_,league])