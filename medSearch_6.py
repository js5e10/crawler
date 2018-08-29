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

    url="https://hackernoon.com/learn-blockchains-by-building-one-117428612f46"
    response=requests.get(url)
    html=response.text
    page=BeautifulSoup(html,'html.parser')
    print('parse_done')
    time.sleep(10)


    structure=findH(page)
    header=structure['header']
    content=structure['content']

    df=dataFrame(header,content)

    writer=pd.ExcelWriter('mS_6.xlsx',
                          engine='xlsxwriter')

    df.to_excel(writer, sheet_name='sheet1')
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
