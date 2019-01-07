from urllib.request import urlopen
from bs4 import BeautifulSoup

scrap_site = 'http://www.espn.in/soccer/team/_/id/360/manchester-united'
scrap_page = urlopen(scrap_site)
soup = BeautifulSoup(scrap_page, 'html.parser')
soup_1 = soup.find('section', class_='club-schedule')
game_strips = soup_1.select('.game-strip')

for game_strip in game_strips[1:]:
    team_a = game_strip.select_one('.team-a')
    team_b = game_strip.select_one('.team-b')
    team_a_name = team_a.select_one('.abbrev').get_text()
    team_a_score = team_a.select_one('.score-container').get_text()
    team_b_name = team_b.select_one('.abbrev').get_text()
    team_b_score = team_b.select_one('.score-container').get_text()

    print(str(team_a_name) + " " + str(team_a_score) + " - " + str(team_b_name) + " " + str(team_b_score))
    print('\n--------------------------------------------------------------------------------------\n')
