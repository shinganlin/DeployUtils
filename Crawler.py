import requests
from requests_html import HTML
from bs4 import BeautifulSoup
import sqlite3
import time
import json


class AccessToUrl:

    def __init__(self):
        self.userheader = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.product =str(input("Enter the product: "))
        if (len(self.product) < 1):
            self.product = "AppleMac"
        pchome_url='https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+self.product
        yahoo_url = 'https://tw.buy.yahoo.com/search/product?p='+self.product
        tkec_url = 'http://www.tkec.com.tw/search.aspx?q='+self.product
        self.url = {'PCHOME':pchome_url,'YAHOO':yahoo_url,'TKEC':tkec_url}
        self.title_data= list()
        self.price_data= list()
        self.picture_data = list()
        self.CreateDB('Shopdata.sqlite',self.product)

    def fetch(self):
        for shop, url in self.url.items():
            self.resp = requests.get(url, headers = self.userheader)
            if shop=="PCHOME":
                self.fetchcontent = json.loads(self.resp.text)
                self.fetchcontent = self.fetchcontent['prods']
                for line in self.fetchcontent:
                    self.title_data.append(line['name'])
                    self.price_data.append(line['price'])

            elif shop == "YAHOO":
                self.soup = BeautifulSoup(self.resp.text,'html.parser')
                allinfo = self.soup.find_all(class_="BaseGridItem__itemInfo___3E5Bx")
                for infos in allinfo:
                    if infos.find(class_="BaseGridItem__title___2HWui") != None and infos.find(class_="BaseGridItem__price___31jkj").em != None:
                        self.title_data.append(infos.find(class_="BaseGridItem__title___2HWui").text)
                    if infos.find(class_="BaseGridItem__price___31jkj").em != None:
                        self.price_data.append(infos.find(class_="BaseGridItem__price___31jkj").em.text)
                    # soup.find_all(class_="Pagination__numberBtn___3HrVf Pagination__button___fFc6Y")[0]['href'] GET NEXT PAGE

            elif shop == "TKEC": #燦坤
                self.soup = BeautifulSoup(self.resp.text,'lxml')

                allinfo = self.soup.find_all(class_="prod_item1512 colBox")
                for infos in allinfo:
                    if infos.find("h3",class_="title") != None:
                        self.title_data.append(infos.find("h3",class_="title").text)
                    if infos.find(class_="price") != None:
                        self.price_data.append(infos.find(class_="price").text.split("$")[1])

            self.InsertInDB(self.title_data,self.price_data)
                    #if infos.img !=None:
                        #self.picture_data.append(infos.img['src'])

    def CreateDB(self,DBName,tablename):

        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.dbname = DBName
        self.tablename = self.product

        droptable = "DROP TABLE IF EXISTS %s" % self.tablename
        self.cur.execute(droptable)
        createtable = """CREATE TABLE %s(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE,
            price TEXT UNIQUE
        );""" % self.tablename
        self.cur.execute(createtable)

    def InsertInDB(self,name,price):

        for i in name:
            insert_1 = "INSERT OR IGNORE INTO "+self.product+" (name) VALUES (?)"
            print(i)
            fillindata = (i)
            #insert_2 = "INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( ?, ? )"
            try:
                self.cur.execute(insert_1,(fillindata,))
            except:
                pass
            self.conn.commit()


        for j in price:
            insert_2 = "INSERT OR IGNORE INTO "+self.product+" (price) VALUES (?)"
            print(j)
            fillindata2 = (j)
            #insert_2 = "INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( ?, ? )"
            try:
                self.cur.execute(insert_2,(fillindata2,))
            except:
                pass
            self.conn.commit()


class grabfromDB:

    def __init__(self):
        self.itemname =list()
        self.itemprice =list()

    def connectDB(self,DBname):
        self.tablename = str(input("Enter the Tablename: "))
        db_connection = sqlite3.connect(DBname)
        cur = db_connection.cursor()
        rows = c.execute("SELECT id, name, price FROM %s;" % self.tablename)




#------------------Main Code==============================

Cra = AccessToUrl()
Cra.fetch()
