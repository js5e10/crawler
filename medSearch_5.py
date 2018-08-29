import argparse
import os
import time
import urlparse2
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import requests




def Main():



    url="https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348"
    response=requests.get(url)
    html=response.text
    file=open('comp.text','w')
    print('=================check==================')
    file.write(str(html.encode('utf8')))
    page1=BeautifulSoup(html,'html.parser')

    browser=webdriver.Chrome()
    browser.get("https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348")
    page=BeautifulSoup(browser.page_source)
    file=open('comp_1.text','w')
    file.write(str(page.html.encode('utf8')))



    structure=findH(page)
    structure1=findH(page1)

    header=structure['header']
    content=structure['content']

    header1=structure1['header']
    content1=structure1['content']

    df=dataFrame(header,content)
    df1=dataFrame(header1,content1)

    writer=pd.ExcelWriter('mS_5.xlsx',
                          engine='xlsxwriter')
    writer1=pd.ExcelWriter('mS_5_compare.xlsx',
                          engine='xlsxwriter')


    df.to_excel(writer, sheet_name='sheet1')
    df1.to_excel(writer1, sheet_name='sheet1')
    writer.save()
    writer.close()



def dataFrame(header, content):

    hList=[]
    Clist=[]
    Cword=''



    for i in header:
        hList.append(i)

    for i in content:


        if i=='*************':
            Clist.append(Cword)
            Cword=''


        elif i!='*************':
            Cword=Cword+i
        else:
            Clist.append(Cword)


    print (Clist)
    dic={'header':hList, 'content':Clist}
    df=pd.DataFrame.from_dict(dic, orient='index')
    return df




def findH(page):


    a=page.find_all("div", class_="section-inner")
    text=[]
    content=[]
    header=page.h1
    text.append(header.text)
    for j in a:
        for element in j:
            for i in str(element).split():
                if '<h2' == i:
                    text.append(element.text)
                    content.append('*************')
                    print(element.text)
                    #time.sleep(2)
                    break
                elif '<h3' == i:
                    print(element.text)
                    text.append(element.text)
                    content.append('*************')
                    #time.sleep(2)
                    break
                elif '<h4' == i:
                    print(element.text)
                    text.append(element.text)
                    content.append('*************')
                    #time.sleep(2)
                    break
                elif '<h1' == i:
                    break

                content.append(element.text)
                print(element.text)
                #time.sleep(2)
                break


    content.append('*************')
    print (text)

    print (content)


    return {'header':text, 'content':content}










if __name__ == '__main__':
	Main()
