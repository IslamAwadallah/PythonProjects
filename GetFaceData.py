#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import nltk
import arabicstemmer

import json
import os
import requests
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.isri import ISRIStemmer
import facebook
import mysql.connector



# db=mysql.connector()



short_token='EAAEzLTR2AqkBAONEBQRYLENEURYcYxamj5YDdqy0JIhfdMnaSSwJSv7DIDsqKC3ZB2nbbYNBZCyAVrfxOqBoF4rly5nqpDzBil4YWKkrMRDtdvFdDN0LTbEXHRXiLtmWPfPbTSaQ0XTbEWtaZCUFxPUALcc09NjoLldDxv6WURsygSgjUHSZCpV87pXjuo8ZD'

graph=facebook.GraphAPI(short_token)
id='337744223404713'
secrit='50d613d48ac57206f9588775c27053a9'
long_token=graph.extend_access_token(id, secrit)
graph=facebook.GraphAPI(long_token['access_token'])
pages=graph.get_object('me?fields=likes.limit(24){posts{message,link,full_picture,id}}')



def GetProductsForSalary(x):
    s=False
    ps = PorterStemmer()
    words = word_tokenize(x)
    st = ISRIStemmer()
    length = len(words)
    # print(x)
    i = 0
    while i < length:
        z = st.stem(words[i])
        if re.search('\d', z):
            k=0
            while(k<len(z)):
                if z[k]=="ش":
                    s=True
                    print("vvvvvvvvvvvvvvvvvvvvvvvvv",z)

        elif z == "شيكل" or z == "شيقل" or z == "ش" or z=="NIS" or z=="Nis" :
               s=True

        i += 1
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT====>",s)
    return  s

#
# def GetPages(page):
#     for n in dataX['data']:
#          x=n['name'].encode('UTF-8')
#          print(x)
         # AllPages.append(n['id'])

def GetProducts(product):
    q1 = re.search("لاب توب", product)
    q2 = re.search("Samsung Galaxy", product)
    q3 = re.search("طابعة", product)
    q4 = re.search("iphone", product)
    q5 = re.search("اي فون", product)
    q6 = re.search("لابتوب", product)
    q7 = re.search("Laptop", product)
    q8 = re.search("سماعة", product)
    q9 = re.search("Intel", product)
    q10 = re.search("شواحن", product)
    q11 = re.search("GB", product)
    q12 = re.search("ram", product)
    q13 = re.search("شاحن", product)
    q14 = re.search("Samsung Galaxy j7", product)
    q15 = re.search("Samsung Galaxy j5", product)

    # print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",q.match())
    if q1 or q2 or  q6 or q4 or q5  or q7 :
        # print(q.group(0))
            if q1:print(q1.group(0));return q1.group(0)
            if q2:print(q2.group(0));return q2.group(0)
            if q3:print(q3.group(0));return  q3.group(0)
            if q4:print(q4.group(0));return q4.group(0)
            if q5:print(q5.group(0));return q5.group(0)
            if q6:print(q6.group(0));return q6.group(0)
            if q7:print(q7.group(0));return q7.group(0)
            if q8:print(q8.group(0));return q8.group(0)
            if q9: print(q9.group(0));return q9.group(0)
            if q10: print(q10.group(0));return q10.group(0)
            if q11: print(q11.group(0));return q11.group(0)
            if q12: print(q12.group(0));return q12.group(0)
            if q13: print(q13.group(0));return q13.group(0)
            if q14: print(q14.group(0));return q14.group(0)
            if q15: print(q15.group(0));return q15.group(0)




def GetPosts(post):
    count=0
    for j in post['likes']['data']:
        for i in j['posts']['data']:
            if 'message' in i:
                y = i['message']
                if GetProducts(y):
                # if  GetProductsForNumber(y):
                #     x=GetProductsForSalary(y)
                    print(y)

                    if 'full_picture' in i:
                        pic=i['full_picture']
                        print("this is pic ",pic)
                    if 'link'in i:
                        link = i['link']
                        print("this is link", link)
                    if 'id'in i:
                        id = i['id']
                        print("this is id", id)


                    count +=1
                    print("===================================================")

    print("the count is ==> ",count)








def GetProductsForNumber(product):
    q = re.search("02[.-]\d+", product)
    num = re.search("05[6|9]\d+", product)
    if q:
        return q.group(0)
    if num:
        return num.group(0)

if __name__ == '__main__':
    # me1=requests.get(me)
    # print(me1.text)
    #
    # lk=requests.get(likes)
    # All_likes=lk.text
    # dataX=json.loads(All_likes)
    # GetPages(dataX)

    # pos=requests.get(pages)
    # posts=pos.text
    # aa=json.loads(posts)
    isla=json.dumps(pages, indent=4, sort_keys=True)
    # isla.encode('utf-8')
    # print (isla)
    GetPosts(pages)

























# token= os.environ.get('FACEBOOK_TEMP_TOKEN')
# graph=facebook.GraphAPI(token)
# profile=graph.get_object('me',fields='id')
# print(json.dumps(profile,indent=4))
#
# access_token = 'EAACEdEose0cBANAqtNX6o0ltLCIkyV9xNtSIWZBYDeA2PCyUOMjBdIqTBXbmeeH5utUDme6bBMthMGeA7dTczSCHI5CNmCnqR51Kuuamzk4Ed1a3n9ucFnuTxVkTL5VA8hd2wcmOjcVAS5ZBvVD7Qg99FbaUP9NLaZBueTuuTRdYh49YHwIjLXblhMSMrnZAY8D9J7vBwAZDZD'     # Obtained from https://developers.facebook.com/tools/accesstoken/
# app_id = "337744223404713"          # Obtained from https://developers.facebook.com/
# client_secret = "50d613d48ac57206f9588775c27053a9"    # Obtained from https://developers.facebook.com/
# link='https://graph.facebook.com/oauth/access_token?client_id=337744223404713&client_secret=50d613d48ac57206f9588775c27053a9&grant_type=fb_exchange_token&fb_exchange_token=EAACEdEose0cBANAqtNX6o0ltLCIkyV9xNtSIWZBYDeA2PCyUOMjBdIqTBXbmeeH5utUDme6bBMthMGeA7dTczSCHI5CNmCnqR51Kuuamzk4Ed1a3n9ucFnuTxVkTL5VA8hd2wcmOjcVAS5ZBvVD7Qg99FbaUP9NLaZBueTuuTRdYh49YHwIjLXblhMSMrnZAY8D9J7vBwAZDZD'
# s = requests.Session()
# token = s.get(link).content
# token=json.loads(token)
# token=token.get('access_token')
# print token
# https://graph.facebook.com/oauth/access_token?client_id=337744223404713&client_secret=50d613d48ac57206f9588775c27053a9&grant_type=fb_exchange_token&fb_exchange_token=ACCESS_TOKEN_HERE

# token='EAACEdEose0cBANAqtNX6o0ltLCIkyV9xNtSIWZBYDeA2PCyUOMjBdIqTBXbmeeH5utUDme6bBMthMGeA7dTczSCHI5CNmCnqR51Kuuamzk4Ed1a3n9ucFnuTxVkTL5VA8hd2wcmOjcVAS5ZBvVD7Qg99FbaUP9NLaZBueTuuTRdYh49YHwIjLXblhMSMrnZAY8D9J7vBwAZDZD'
# me='https://graph.facebook.com/v2.10/me?access_token='+ token
# likes = 'https://graph.facebook.com/v2.12/me/likes?access_token='+token
# po='https://graph.facebook.com/v2.12/me?fields=likes.limit(20)%7Bposts%7Bmessage%2Cfull_picture%2Clink%7D%7D&access_token='+token

# print token
