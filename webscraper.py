from bs4 import BeautifulSoup
import itertools


import requests

page_link ='http://www.rotoworld.com/playernews/nfl/football-player-news'

# fetch the content from url

page_response = requests.get(page_link, timeout=200)

# parse html

page_content = BeautifulSoup(page_response.content, "html.parser")


# print(page_content.prettify())


# extract all html elements where price is stored


players_general = page_content.select('.pb .player')
player_stories = page_content.select('.pb .report')
players= [pg.select('a') for pg in players_general]

for x,y in zip(players, player_stories):
	print (x[0].get_text() + '  -  ' + x[1].get_text() + y.get_text())


#for x in players:
#	for y in x:
		# print y.get_text()
#		y = y.get_text()


	




# prices has a form:

#[<div class="main_price">Price: $66.68</div>,

# <div class="main_price">Price: $56.68</div>]



# you can also access the main_price class by specifying the tag of the class

