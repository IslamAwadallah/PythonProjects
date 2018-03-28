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

# Islam=[]
# Islam="https://www.facebook.com/dialog/oauth?client_id=<337744223404713>&redirect_uri=<https://developers.facebook.com/tools/explorer/145634995501895/>"
#
# access_token ="https://graph.facebook.com/oauth/access_token?client_id=337744223404713&client_secret=50d613d48ac57206f9588775c27053a9&code="+Islam[1]

short_token='EAAEzLTR2AqkBAJtB66WKk3YwNCPUHlB4K5Hy8Nw6S9nfocU6ZCWiZB9X5R1sSAPdPhkhlH2XgBNAoSsVcXt9vpe7MPxqaMHhrlQlDw1OaZBsqfFjtjGgF77nS9KDeAbAgZBW1qu2KUB0TKEozfpZCAZBQILfeFeCZBcfkEAMSQIBwZDZD'

graph=facebook.GraphAPI(short_token)
id='337744223404713'
secrit='50d613d48ac57206f9588775c27053a9'
long_token=graph.extend_access_token(id, secrit)
graph=facebook.GraphAPI(long_token['access_token'])
pages=graph.get_object('me?fields=likes.limit(24){posts{id,created_time,link,message,full_picture}}')


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





def GetPosts(post):
    count=0
    db = MySQLdb.connect("127.0.0.1", "root", "", "DATA" ,charset='utf8')
    cur = db.cursor()
    for j in post['likes']['data']:
        for i in j['posts']['data']:
            if 'message' in i:
                if 'full_picture' in i and 'link' in i and 'created_time'in i:
                    _msg=i['message']
                    _pic = i['full_picture']
                    _link = i['link']
                    _id = i['id']
                    _time=i['created_time']

                category = GetProducts(_msg)
                if category:
                    if  GetProductsForSalary(_msg)==True:
                        print(_msg)
                        print("this is pic ", _pic)
                        print("this is link", _link)
                        print("this is id", _id)
                        print("this is time", _time)

                        t1 , t2=_time.split('T')
                        print(t1)
                        print("ssssssssss %s",t2)
                        # print(type())
                        cur.execute("""INSERT INTO test2 VALUES(%s,%s,%s,%s)""" ,(_id,_msg,_link,_pic))


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

