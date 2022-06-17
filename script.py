from selenium import webdriver
from bs4 import BeautifulSoup
import time
import  vlc
import random

def watch() :
    try:
        driver = webdriver.Chrome("/home/mojtaba/Projects/shajarian_script/chromedriver_linux64/chromedriver")

        url = "https://www.tiwall.com/s/homayoun.shajarian"

        while True:
            driver.get(url)
            content = driver.page_source
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find("body"
                    ).find("div", attrs={'id': 'top-bg-container'}
                    ).find("div", attrs={'id': '_container'}
                    ).find('div', attrs={'class': 'rc'}
                    ).find('div', attrs={'id': 'body'}
                    ).find('div', attrs={'id': 'steps-c'}
                    ).find('div', attrs={'id': 'reserve-config'}
                    ).find('form', attrs={'id': 'myForm'}
                    ).find('div', attrs={'id' : 'showtimeMenu'}
                    ).find('div', attrs={'id': 'showTimesMenu'}
                    ).select('a.pjax-noscroll')


            if len(links) != 11 :
                p = vlc.MediaPlayer("/home/mojtaba/Projects/shajarian_script/song.mp3")
                p.play()
            else:
                n = random.randint(15, 90)
                time.sleep(n)
    except:
        watch()



watch()