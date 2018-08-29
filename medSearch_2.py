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




def Main():

    browser=webdriver.Chrome()
    browser.get("https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348")
    page=BeautifulSoup(browser.page_source)
    structure=findH(page,browser)
    header=structure['header']
    content=structure['content']

    df=dataFrame(header,content)

    writer=pd.ExcelWriter('mS_2.xlsx',
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


        if i!='*************':

            Cword=Cword+i

        elif i=='*************':
            Clist.append(Cword)
            Cword=''
        else:
            Clist.append(Cword)


    print (Clist)
    dic={'header':hList, 'content':Clist}
    df=pd.DataFrame.from_dict(dic, orient='index')
    return df




def findH(page, browser):


    text1=[]
    content=[]
    i=page.h1
    header=page.h1
    j=header
    text1.append(j.text)

    j=j.next_sibling
    links = []




    while j != None:
        #if j==None:
         #   break


        for i in str(j).split():
            if i=='<h2':

                    text1.append(j.text)
                    j=j.next_sibling
                    content.append('*************')

            elif i=='<h3':

                    text1.append(j.text)
                    j=j.next_sibling
                    content.append('*************')

            elif i=='<h4':

                    text1.append(j.text)
                    j=j.next_sibling
                    content.append('*************')

            else:
                break

        if  j!=None:
            content.append(j.text)

        else:

            break
        j=j.next_sibling


    content.append('*************')
    print (text1)

    print (content)


    return {'header':text1, 'content':content}










if __name__ == '__main__':
	Main()
