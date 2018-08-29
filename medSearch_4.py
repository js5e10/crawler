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
    browser.get("https://medium.com/@josh_nussbaum/blockchain-project-ecosystem-8940ababaf27")
    page=BeautifulSoup(browser.page_source)



    structure=findH(page,browser)
    header=structure['header']
    content=structure['content']

    df=dataFrame(header,content)

    writer=pd.ExcelWriter('mS_4.xlsx',
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




def findH(page, browser):

    #h1=page.find('h1')

    #for h1_sibling in h1.next_siblings:
    #    print(repr(h1_sibling))
    #    time.sleep(5)

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







    #print(repr(a))
    #time.sleep(5)



    #text1=[]
    #content=[]
    #i=page.h1
    #header=page.h1
    #j=header
    #text1.append(j.text)

    #j=j.next_sibling





    #while j != None:
    #    if j==None:
    #        break


    #    for i in str(j).split():
    #        if i=='<h2':

    #               text1.append(j.text)
    #                j=j.next_sibling
    #                content.append('*************')

    #       elif i=='<h3':

    #                text1.append(j.text)
    #                j=j.next_sibling
    #                content.append('*************')

    #        elif i=='<h4':

    #                text1.append(j.text)
    #                j=j.next_sibling
    #                content.append('*************')

     #       else:
     #           break

     #   if  j!=None:
     #       content.append(j.text)

     #   else:

     #       break
     #   j=j.next_sibling


    content.append('*************')
    print (text)

    print (content)


    return {'header':text, 'content':content}










if __name__ == '__main__':
	Main()
