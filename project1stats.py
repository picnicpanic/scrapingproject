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
driver.get("https://overwatchleague.com/en-us/stats")
time.sleep(1)

csv_file = open('stats.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['player','team','eliminations','deaths','damage','healing'])

index = 1

while True:
    try:
    
        print('Scraping page {}'.format(index))
        index = index + 1 

        time.sleep(1)
        wait_review = WebDriverWait(driver, 10)

        players = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="table-rowstyles__Content-sc-1t1l9w4-3 iNtjXU"]')))
        #print(len(players))
        #players = driver.find_elements_by_xpath('//div[@class="table-rowstyles__Content-sc-1t1l9w4-3 iNtjXU"]') #will find 20 per page usually
        time.sleep(1)

        for player in players:
            player_dict={}
            time.sleep(1)
            
            try:
                nickname = player.find_element_by_xpath('.//span[@class="table-cardstyles__Name-sc-2s08up-1 cWeemN resizable-namestyles__Name-sc-1qh8dp6-2 gORxWa"]').text
                #print(nickname)
            except:
                print('nickname not found')
                continue

            try:
                team = player.find_element_by_xpath('.//span[@class="statistics-tablestyles__TableTeam-sc-68hghq-4 fkHNYi resizable-namestyles__Name-sc-1qh8dp6-2 gORxWa"]').text
                #print(team)
            except:
                print('team not found')
                team = None

            try:
                elim = float(player.find_element_by_xpath('.//span[@class="statistics-tablestyles__TableData-sc-68hghq-5 hLlELQ table-textstyles__DataText-sc-10uhrpp-0 eGVUqd"]').text)
                #print(elim)
            except:
                print('elim not found')
                elim = None

            try:
                deaths = float(player.find_element_by_xpath('./div[5]/span[@class="statistics-tablestyles__TableData-sc-68hghq-5 hLlELQ table-textstyles__DataText-sc-10uhrpp-0 eGVUqd"]').text)
                #print(deaths)
            except:
                print('deaths not found')
                deaths = None
                
            try:
                damage = int(player.find_element_by_xpath('./div[6]/span[@class="statistics-tablestyles__TableData-sc-68hghq-5 hLlELQ table-textstyles__DataText-sc-10uhrpp-0 eGVUqd"]').text)
                #print(damage)
            except:
                print('damage not found')
                damage = None
                
            try:
                healing = int(player.find_element_by_xpath('./div[7]/span[@class="statistics-tablestyles__TableData-sc-68hghq-5 hLlELQ table-textstyles__DataText-sc-10uhrpp-0 eGVUqd"]').text)
                #print(healing)
            except:
                print('healing not found')
                healing = None
                
            player_dict['player'] = nickname
            player_dict['team'] = team
            player_dict['eliminations'] = elim
            player_dict['deaths'] = deaths
            player_dict['damage'] = damage
            player_dict['healing'] = healing

            writer.writerow(player_dict.values())

         
        wait_button = WebDriverWait(driver, 10)
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//i[@class="icon-ChevronRight iconstyles__StyledIcon-maju6z-0 dKHRSY"]')))
        next_button.click()
        
    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break