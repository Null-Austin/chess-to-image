import statsreturn
import imgkit
def gethtml(username):
    stats=statsreturn.getall(username)
    html = open('template.html').read()
    html = html.replace('{{{username}}}',username)
    html = html.replace('{{{date}}}',stats[3])
    html = html.replace('{{{score}}}',str(stats[0]))
    html = html.replace('{{{winrate}}}',str(int(float(stats[1][:-1])*100)) + '%')
    html = html.replace('{{{rank}}}',stats[6][0])
    html = html.replace('{{{country}}}',stats[4])
    html = html.replace('{{{ISMOD}}}',str(stats[5]).lower())
    html = html.replace('{{{img}}}',stats[2])
    return(html)
def takescreenshot(username):
    imgkit.from_string(gethtml(username), 'users/USER' + username + '.png', options={'width': '1000', 'height': '225'})
takescreenshot('BaronAustin')