from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
from urllib.request import urlopen


# Declaration : webdriver
# In fact, we don't need the variable 'opts' just below
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver = webdriver.Chrome("chromedriver", options=opts)

# Data for the target toon
no_MAX = 81

# 1st episode url
driver.get("https://marumaru.dance/bbs/cmoic/20334/36331")

# Main for-loop
for no in range(1, no_MAX):
    html = driver.page_source

    # Page parsing
    soup = BeautifulSoup(html, 'html.parser')
    if (no == 1):
        url_next = soup.select("#thema_wrapper > div.at-body > div > div > div.col-md-9.at-col.at-main > div > div:nth-child(1) > h1:nth-child(2) > div.popular.pull-right.goods > a:nth-child(2)")
    else:
        url_next = soup.select("#thema_wrapper > div.at-body > div > div > div.col-md-9.at-col.at-main > div > div:nth-child(1) > h1:nth-child(2) > div.popular.pull-right.goods > a:nth-child(3)")
    url_page = soup.select("#thema_wrapper > div.at-body > div > div > div.col-md-9.at-col.at-main > div > div.view-img > img")

    # Saving image files
    os.makedirs(os.path.join('./IMAG/{:0>4}'.format(no)))
    i_num = 1
    for i in url_page:
        url_img = i['src']
        if(url_img == "https://image-comic.pstatic.net/static/agerate/age_all_white.jpg"):
            pass
        else:
            req = urllib.request.Request(url_img, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as f:
                with open('./IMAG/' + '{:0>4}/'.format(no) + '{:0>2}'.format(i_num) + '.jpg', 'wb') as h:
                    i_num += 1
                    img = f.read()
                    h.write(img)
    i_num = 1

    print("Episode " + '{:0>3}'.format(no) + " download completed")

    for j in url_next:
        url_next_episode = j['href']
    driver.get(url_next_episode)
