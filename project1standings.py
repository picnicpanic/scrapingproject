from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\Sathya\Desktop\chromedriver\chromedriver.exe')
# Go to the page that we want to scrape
driver.get("https://overwatchleague.com/en-us/standings")
time.sleep(3)
league_button = driver.find_element_by_xpath('//li[@class="tabsstyles__Label-sc-1fl2yza-4 eBerzq"][3]')
league_button.click()


time.sleep(1)

csv_file = open('standings.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['team','wins','losses'])


time.sleep(1)
wait_review = WebDriverWait(driver, 10)

teams = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="standings-tablestyles__StandingRow-r7smk9-8 kjUKQm table-rowstyles__Container-sc-1t1l9w4-0 guERse"]')))

       
time.sleep(1)
        
        
for player in players[100:120]:
            player_dict={}
            time.sleep(1)
            try:
                team = player.find_element_by_xpath('.//span[@class="table-cardstyles__Name-sc-2s08up-1 cWeemN resizable-namestyles__Name-sc-1qh8dp6-2 gORxWa"]').text
                #print(team)
            except:
                print('team not found')
                continue

            try:
                wins = int(player.find_element_by_xpath('./div/div[4]/span[@class="standings-tablestyles__TableCellContent-r7smk9-6 gMHZaP"]').text)
                #print(wins)
            except:
                print('wins not found')
                wins = None
                
            try:
                losses = int(player.find_element_by_xpath('./div/div[5]/span[@class="standings-tablestyles__TableCellContent-r7smk9-6 gMHZaP"]').text)
                #print(losses)
            except:
                print('losses not found')
                losses = None

            player_dict['team'] = team
            player_dict['wins'] = wins
            player_dict['losses'] = losses
         

            writer.writerow(player_dict.values())


csv_file.close()