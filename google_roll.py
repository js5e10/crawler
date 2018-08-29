import argparse
import os
import time
import urlparse2
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getLinks(page):
    links = []
    getBlockChain(page)

    for link in page.find_all('a'):
        url=link.get('href')
        #print ("---------" + str(url))
        if url:
            if '/search?q=blockchain&ei' in url:
                urlFilter=url
                print ("+++++++++" + str(urlFilter))
                browser=webdriver.Chrome()
                browser.get('https://www.google.com/'+str(urlFilter))
                updateLink='https://www.google.com/'+str(urlFilter)
                print(str(updateLink))


    return links

def getBlockChain(page):

    links = []
    for link in page.find_all('a'):
        url=link.get('href')
        if url:
                if 'blockchain' in url:
                    if 'accounts.google' not in url:
                        if '/search?' not in url:
                            if'maps.google' not in url:
                                if '/flights?'not in url:
                                    if '/advanced_search?' not in url:
                                        urlF=url
                                        print('+++++++++++++++++++++++++'+str(urlF))
                                        time.sleep(5)
                                        browser=webdriver.Chrome()
                                        browser.get(str(urlF))

    return links

def ViewBot(browser):

    visited = {}
    bList = []

    while True:

        page= BeautifulSoup(browser.page_source)
        getLinks(page)
        break





def getID(url):

    pUrl=urlparse2.urlparse(url)
    return urlparse2.parse_qs(pUrl.query)['id'][0]

def Main():

     parser=argparse.ArgumentParser()
     parser.add_argument("blockchain", help="blockchain")
     args = parser.parse_args()

     browser=webdriver.Chrome()
     browser.get("https://www.google.com/")

     searchElement = browser.find_element_by_id("lst-ib")
     searchElement.send_keys(args.blockchain)
     searchElement.submit()

     os.system('clear')
     ViewBot(browser)

if __name__ == '__main__':
	Main()
