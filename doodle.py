#!/usr/bin/python3
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


PAGE = 'https://www.google.com/doodles?hl=de#archive'
PATH = '/home/jens/docker/speeddial/data/'
NAME = 'speeddial.doodle.png'


def extract_doodle_link():
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(3)
    driver.get(PAGE)

    doodle_png_src = driver.find_element_by_xpath('//ul[@id="archive-list"]/li[1]//img').get_attribute('src')
    driver.quit()

    return doodle_png_src


def save_doodle(url):
    doodle_response = requests.get(url)

    if doodle_response.status_code == 200:
        with open(PATH + NAME, 'wb') as doodle:
            doodle.write(doodle_response.content)


if __name__ == '__main__':
    save_doodle(extract_doodle_link())
