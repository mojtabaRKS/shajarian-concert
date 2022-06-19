from bs4 import BeautifulSoup
import time
import vlc
import random
import requests

URL = "https://www.tiwall.com/s/homayoun.shajarian"


def watch():
    try:
        while True:
            response = requests.get(URL)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find('div', attrs={'id': 'showTimesMenu'}).select('a.pjax-noscroll')

            if len(links) != 11:
                while True:
                    p = vlc.MediaPlayer("./song.mp3")
                    p.play()
            else:
                n = random.randint(15, 90)
                time.sleep(n)
    except:
        watch()


watch()
