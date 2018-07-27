from bs4 import BeautifulSoup
import itertools
import requests


# Checks for players listed on user's team in rotoworld headlines. If players match, their news is sent to team.txt. All news then sent to console
def check_team(team, players, player_stories):
	for y,z in zip(players,player_stories):
		for x in team: 
			if x == y[0].get_text(strip=True):
				with open("team.txt","r+") as f:
					lines = f.readlines()
					lines = [i.strip() for i in lines]
					lines = filter(None, lines)

					if z.get_text(strip=True) in lines:
						continue
					f.write(y[0].get_text(strip=True) + ' \r\n' + z.get_text(strip=True) + '\r\n\r\n')
				f.close()

	run_page(players, player_stories)


def run_page(players, player_stories):
	for x,y in zip(players, player_stories):
		print (x[0].get_text() + '  -  ' + x[1].get_text() + ' ' + y.get_text())


page_link ='http://www.rotoworld.com/playernews/nfl/football-player-news'

# fetch the content from url

page_response = requests.get(page_link, timeout=200)

# parse html

page_content = BeautifulSoup(page_response.content, "html.parser")

# link player names with teams and their story headline
players_general = page_content.select('.pb .player')
player_stories = page_content.select('.pb .report')
players= [pg.select('a') for pg in players_general]



team = []

check_team(team, players, player_stories)
