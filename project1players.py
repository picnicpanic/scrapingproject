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
driver.get("https://overwatchleague.com/en-us/players")
time.sleep(1)

csv_file = open('players.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['player','name','hometown','role'])

index = 1

while True:
    try:
    
        print('Scraping page {}'.format(index))
        index = index + 1 

        time.sleep(1)
        wait_review = WebDriverWait(driver, 10)

        players = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="table-rowstyles__Content-sc-1t1l9w4-3 iNtjXU"]')))

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
                name = player.find_element_by_xpath('.//a[@class="players-liststyles__Link-sc-1jhwo3g-14 CQTPb"]').text
                #print(name)
            except:
                print('name not found')
                name = None

            try:
                hometown = player.find_element_by_xpath('.//div[@class="players-liststyles__HometownCell-sc-1jhwo3g-8 ghvQQY table-cellstyles__Container-sc-1k1ivbt-0 gtVrBZ"]').text
                #print(hometown)
            except:
                print('hometown not found')
                hometown = None

    #       #could not get team name abbreviation for some reason            
    #       try:
    #           team = player.find_element_by_xpath('.//span[@class="table-cardstyles__Name-sc-2s08up-1 cWeemN resizable-namestyles__Abbreviation-sc-1qh8dp6-1 gYcSYZ"]').text
    #           print(team)
    #       except:
    #           print('team not found')
    #           team = None
            try:
                role = player.find_element_by_xpath('.//span[@class="players-liststyles__RoleName-sc-1jhwo3g-20 hIpmas"]').text
                #print(role)
            except:
                print('role not found')
                role = None

            player_dict['player'] = nickname
            player_dict['name'] = name
            player_dict['hometown'] = hometown
            player_dict['role'] = role

            writer.writerow(player_dict.values())

         
        wait_button = WebDriverWait(driver, 10)
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//i[@class="icon-ChevronRight iconstyles__StyledIcon-maju6z-0 dKHRSY"]')))
        next_button.click()
    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break