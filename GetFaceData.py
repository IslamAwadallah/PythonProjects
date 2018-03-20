#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import numpy
import MySQLdb
import nltk
import arabicstemmer
import json
import os
import requests
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.isri import ISRIStemmer
import facebook
import sys




short_token='EAAEzLTR2AqkBADOA54eUZBxLfZCauO7GJfYDSY83MFOCx81LZByCyIZBMsZA9bMSzFcyR2RA6C1d6M6B33PPX9wSsDz59VMM6RuheJNontZAit57cPKeF3i0CFYwrzdnW4atLJB7hETKjoeaZCf0d8cwdiMtPZBVtUlyZCWTUIxFxgFasGQoIMHtFfJNpjJZAeFKIj0K50saRSugZDZD'

graph=facebook.GraphAPI(short_token)
id='337744223404713'
secrit='50d613d48ac57206f9588775c27053a9'
long_token=graph.extend_access_token(id, secrit)
graph=facebook.GraphAPI(long_token['access_token'])
pages=graph.get_object('me?fields=likes.limit(15){posts{message,link,full_picture,id}}')



def GetProductsForSalary(x):
    s = False
    ps = PorterStemmer()
    words = word_tokenize(x)
    st = ISRIStemmer()
    length = len(words)
    # print(x)

    if length<30:
        s=False
    else:
        i = 0
        while i < length:
            z = st.stem(words[i])
            if re.search('\d\d+', z):
            #     k = 0
            #     while (k < len(z)):
            #         if z[k] == "ش":
            #             s = True
            #             print("vvvvvvvvvvvvvvvvvvvvvvvvv", z)
            #
            # elif z == "شيكل" or z == "شيقل" or z == "ش" or z == "NIS" or z == "Nis":
                s = True
                # print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT====>", s)

            i += 1



    return s

#
# def GetPages(page):
#     for n in dataX['data']:
#          x=n['name'].encode('UTF-8')
#          print(x)
         # AllPages.append(n['id'])

def GetProducts(product):
    q1 = re.search("لاب توب", product)
    q2 = re.search("Samsung Galaxy", product)
    q3 = re.search("samsung", product)
    q4 = re.search("iphone", product)
    q5 = re.search("اي فون", product)
    q6 = re.search("لابتوب", product)
    q7 = re.search("laptop", product)
    q8 = re.search("lenovo", product)
    q9 = re.search("ايفون", product)
    q10 = re.search("اي باد", product)
    q11 = re.search("iphone", product)
    # q12 = re.search("ram", product)
    # q13 = re.search("شاحن", product)
    # q14 = re.search("Samsung", product)
    # q15 = re.search("Samsung Galaxy j5", product)
    # q20=re.search("iphone",product)

    # print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",q.match())

    if  q1 or q2 or  q6 or q4 or q5  or q7 or q8 or q9 or q10 or q11:
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
            # if q12: print(q12.group(0));return q12.group(0)
            # if q13: print(q13.group(0));return q13.group(0)
            # if q14: print(q14.group(0));return q14.group(0)
            # if q15: print(q15.group(0));return q15.group(0)




def GetPosts(post):
    count=0
    db = MySQLdb.connect("127.0.0.1", "root", "", "DATA" ,charset='utf8')
    cur = db.cursor()
    for j in post['likes']['data']:
        for i in j['posts']['data']:
            if 'message' in i:
                if 'full_picture' in i and 'link' in i and 'full_picture' in i:
                    _msg=i['message']
                    _pic = i['full_picture']
                    _link = i['link']
                    _id = i['id']

                if GetProducts(_msg):
                    if  GetProductsForSalary(_msg)==True:
                        print(_msg)
                        print("this is pic ", _pic)
                        print("this is link", _link)
                        print("this is id", _id)

                        # print(type())
                        cur.execute("""INSERT INTO test VALUES(%s,%s,%s,%s)""" ,(_id,_msg,_link,_pic))


                        count +=1
                        print("===================================================")
    db.commit()
    db.close()

    print("SHIIIIIIIIT")

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

