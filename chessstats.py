import requests
def getstats(name):
    url = 'https://www.chess.com/callback/member/stats/' + name
    response = requests.get(url)
    return(response.json())
def getstats1(name):
    url = 'https://www.chess.com/callback/user/popup/' + name
    response = requests.get(url)
    return(response.json())
def getstats2(name):
    url = 'https://www.chess.com/callback/leagues/user-league/search/' + name
    response = requests.get(url)
    return(response.json())