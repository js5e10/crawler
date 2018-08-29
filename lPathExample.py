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
    browser.get("https://medium.com/@jimmysong/why-blockchain-is-hard-60416ea4c5c")
    page=BeautifulSoup(browser.page_source)
    structure=findH(page,browser)
    header=structure['header']
    content=structure['content']

    df=dataFrame(header,content)

    writer=pd.ExcelWriter('medium.xlsx',
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
    #print ('+++++++++++++++++++++++++++++++++')

    #print(browser.find_element_by_class_name('left-content-section').text)

    #print ('+++++++++++++++++++++++++++++++++')



    #time.sleep(15)

    #print(page.h4.next_sibling)

    i=page.h1
    tag1='h1'
    tag2='h2'
    tag3='h3'
    tag4='h4'

    header=page.h1
    j=header
    text1.append(j.text)
    j=j.next_sibling



    while j != None:
        if j==None:
            break


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
