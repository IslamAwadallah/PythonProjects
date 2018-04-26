#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import MySQLdb
import json
import facebook
import schedule
import time
import unicodedata
import Levenshtein

short_token='EAAEzLTR2AqkBADlPcWnGtWbJWVqCze8bozZBg4jxKOzkgIbdF1jpqOCT5HvvZB5Abvi9vWTmCjZCac6NCMZBOZBgxVw46MicNv6VC5ZBAMlQXiHOdVbSliEXOD3Ea9bcfU9ZAefZBNLkJG2pN2xq6CNvANZAn4fAjjpsbMmfNeHzQ3wZDZD'

graph= facebook.GraphAPI(short_token)
id='337744223404713'
secrit='50d613d48ac57206f9588775c27053a9'
long_token=graph.extend_access_token(id, secrit)
graph= facebook.GraphAPI(long_token['access_token'])
pages=graph.get_object('me?fields=id,name,likes{name,posts.limit(3)}')
# pages=graph.get_object('me?fields=likes.limit(20){posts.limit(50){id,created_time,link,message,full_picture}}')
# pages=graph.get_object('me?fields=likes.limit(30)%7Bposts.limit(50)%7Bmessage%2Clink%2Cfull_picture%2Cid%2Ccreated_time%7D%7D')
# pages='https://graph.facebook.com/v2.12/me?fields=likes%7Bposts.limit(3)%7Bmessage%2Clink%2Cfull_picture%2Cid%2Ccreated_time%7D%7D&access_token='+short_token
class GetData:
    flag=0
    g=0
    def __init__(self):
        print(" Graduation Project ")

    # def GetProductsForSalary(self,x):
    #     s = False
    #     ps = PorterStemmer()
    #     words = word_tokenize(x)
    #     st = ISRIStemmer()
    #     length = len(words)
    #     # print(x)
    #
    #     if length<30:
    #         s=False
    #     else:
    #         i = 0
    #         while i < length:
    #             z = st.stem(words[i])
    #             if re.search('\d\d+', z):
    #             #     k = 0
    #             #     while (k < len(z)):
    #             #         if z[k] == "ش":
    #             #             s = True
    #             #             print("vvvvvvvvvvvvvvvvvvvvvvvvv", z)
    #             #
    #             # elif z == "شيكل" or z == "شيقل" or z == "ش" or z == "NIS" or z == "Nis":
    #                 s = True
    #                 # print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT====>", s)
    #
    #             i += 1
    #
    #
    #
    #     return s


    def GetProducts(self,product):
        q1 = re.search(" للبيع لاب توب", product)
        q2 = re.search("Samsung Galaxy", product)
        q3 = re.search("samsung", product)
        q4 = re.search("iphone", product)
        q5 = re.search("اي فون", product)
        q6 = re.search("لاب توب", product)
        q7 = re.search("laptop للبيع", product)
        q9 = re.search("ايفون", product)
        q10 = re.search("اي باد", product)
        q11 = re.search("iphone", product)
        q13 = re.search("لاب توب للبيع", product)
        q12=re.search("صيانة",product)


        if not q12 :

            if q1: self.type=0;return q1.group(0)
            if q13:self.type=0;return q13.group(0)
            if q6: self.type=0;return q6.group(0)
            if q7: self.type=0;return q7.group(0)


            if q2: self.type=1;return q2.group(0)
            if q3: self.type=1;return q3.group(0)
            if q4: self.type=1;return q4.group(0)
            if q5: self.type=1;return q5.group(0)
            if q9: self.type=1;return q9.group(0)
            if q10:self.type=1;return q10.group(0)
            if q11:self.type=1;return q11.group(0)






    def GetPosts(self,post):
        count=0
        db = MySQLdb.connect("127.0.0.1", "root", "", "DATA1" ,charset='utf8')
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

                    if len(_msg)>50:
                        if self.GetProducts(_msg):
                            # if  self.GetProductsForSalary(_msg)==True:
                            #     print(_msg)
                            #     print("this is pic ", _pic)
                            #     print("this is link", _link)
                            #     print("this is id",type(str(_id)))
                            #     print("this is time", _time)
                                # print("sloom ",self.GetProducts(_msg))
                                t1 , t2=_time.split('T')
                                print(t1)
                                cur.execute("""SELECT * FROM Posts""")
                                post_id = cur.fetchall()
                                # print(_id)
                                # print(type(_msg))
                                # print(type(post_id[1][1]))

                                sab = unicodedata.normalize('NFKD', _msg).encode('ascii', 'ignore')

                                print(type(sab))
                                try:
                                    if len(post_id)>0:
                                        for p in post_id:
                                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                            print(type(p[1]))
                                            print(p[1])
                                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                            print(type(_msg))
                                            print(_msg)
                                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                            DataBase_msg=unicodedata.normalize('NFKD', p[1]).encode('ascii', 'ignore')
                                            Facebook_msg=unicodedata.normalize('NFKD', _msg).encode('ascii', 'ignore')
                                            print(type(DataBase_msg))
                                            print(type(Facebook_msg))

                                            xab=Levenshtein.hamming(DataBase_msg,Facebook_msg)
                                            print(DataBase_msg)
                                            print("########################################################################")
                                            print(Facebook_msg)
                                            print(xab)
                                            if xab==0:
                                                cur.execute("""INSERT INTO Simelarity VALUES(%s,%s,%s,%s)""",(_id, _msg, _link, _pic))
                                            else:

                                                for postt in post_id:
                                                    # print("yes")
                                                    # print(postt[0])
                                                    # print(_id)
                                                    if postt[0] != _id:
                                                        self.flag = 0
                                                    else:
                                                        self.flag = 1
                                                        break

                                                if self.flag==0:
                                                    if self.type == 0:
                                                        cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                                    (_id, _msg, _link, _pic, '0'))
                                                    elif self.type==1:
                                                        cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                                    (_id, _msg, _link, _pic, '1'))
                                    else:
                                        for postt in post_id:
                                            # print("yes")
                                            # print(postt[0])
                                            # print(_id)
                                            if postt[0] != _id:
                                                self.flag = 0
                                            else:
                                                self.flag = 1
                                                break

                                        if self.flag == 0:
                                            if self.type == 0:
                                                cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                            (_id, _msg, _link, _pic, '0'))
                                            elif self.type == 1:
                                                cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                            (_id, _msg, _link, _pic, '1'))

                                except:
                                    print("not the Same")
                                    for postt in post_id:
                                        # print("yes")
                                        # print(postt[0])
                                        # print(_id)
                                        if postt[0] != _id:
                                            self.flag = 0
                                        else:
                                            self.flag = 1
                                            break

                                    if self.flag == 0:
                                        if self.type == 0:
                                            cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                        (_id, _msg, _link, _pic, '0'))
                                        elif self.type == 1:
                                            cur.execute("""INSERT INTO Posts VALUES(%s,%s,%s,%s,%s)""",
                                                        (_id, _msg, _link, _pic, '1'))


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

def job():
    G = GetData()

    for i in pages:
        print(i)

    G.GetPosts(pages)

if __name__ == '__main__':
    json_api=json.dumps(pages, indent=4, sort_keys=True)
    print(json_api)


    # schedule.every(0.1).minutes.do(job)
    #
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)




