Github URL: https://github.com/picnicpanic/scrapingproject

I scraped the https://overwatchleague.com website.
Specifically 3 child URLs from this parent website:
	-https://overwatchleague.com/en-us/standings
	-https://overwatchleague.com/en-us/players
	-https://overwatchleague.com/en-us/stats

Had to use selenium since 'page next' button did not update the URL.

The .py files in the repository each perform a scrape of one of the three sites listed above.
	Into players.csv, standings.csv, stats.csv.

The .ipynb file is a notebook file I used for analysis/graphs and also merging on some values from the scraped csv files to make new ones. Merged into overwatch_player_stats.csv, overwatch_team_stats.csv

Analysis was done to see which if any of the statistics could best predict wins, along with some other descriptive statistics.