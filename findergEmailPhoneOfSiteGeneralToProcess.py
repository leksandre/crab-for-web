import pprint
# from googleapiclient.discovery import build
import optparse
import time
import sys
import os
import sqlite3
from sqlite3 import Error
import re
import threading
import datetime
import random
import json
import psutil
import psycopg2
import string
import tldextract
import subprocess
import urllib.parse
from bs4 import BeautifulSoup
from datetime import timezone
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
try:
    import requests
except ImportError:
    if sys.platform.startswith('linux'):
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)


name = sys.argv[0].split('/')[-1]
com = 'pgrep -f ' + name

totalQueries = 0

p = subprocess.Popen([com], stdout=subprocess.PIPE, shell=True)
res = p.communicate()[0]
res122 = res
if isinstance(res, bytes):
    res = res.decode("utf-8")
res = [str(x) for x in res.split('\n') if len(x) > 0]


# if len(res) > 0:
#     print(res, res122, com)
#     print('Already running!')
#     print('Exit!')
#     exit()
#     exit()
#     exit()


proxies = {
    'http': 'socks5h://10.72.1.135:9050',
    'https': 'socks5h://10.72.1.135:9050',
}



proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}


proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}


class Response1:
    def __init__(self, code1, text1):
        self.status_code = code1
        self.text = text1


num11 = 10
relsite = 1
safe11 = 'off'
counttreads = 0
lastcomment = 0
prev_numpost = 0
lastip = 0
restTorStart = 0
nowH = 0
relsite = 0
safe11 = 'active'
datelist = ['d', 'w', 'm', 'y']
targetlist = []
visitedUrl = []
alreadyAdded = []

blockThread = False
emptylist = []


targetlist3 = ['xamarin', 'ксамарин', 'ксомарин', 'AppGyver', 'App Gyver', 'Аппгайвер', ' Ionic ', 'PhoneGap', 'Phone Gap', 'Sencha Touch', 'SenchaTouch', 'CodeName One', 'CodeNameOne', 'React Native', 'ReactNative', 'Appcelerator', ' PWA ', ' PWA,', ' PWA.', ' pwa ', ' pwa,', ' pwa.', 'GoodBarber', 'Good Barber', 'Shoutem', 'Swiftic', 'AppInstitute', 'App Institute', 'Appy Pie', 'AppyPie', 'Bizness Apps', 'BiznessApps', 'AppYourself', 'App Yourself', 'Mobile Roadie', 'MobileRoadie', 'AppMachine', 'App Machine', 'Mobincube', 'AppsBuilder', 'Apps Builder', 'MobAppCreator', 'Mob App Creator', 'MobApp Creator',
               'AppMakr', 'App Makr', 'IBuild App', 'IBuildApp', 'BuildFire', 'Build Fire', 'Appery.io', 'Gamesalad', 'Zoho Creator', 'ZohoCreator', 'Zengine', 'Зенджин', 'Taplytics', 'Тэплитикс', 'Salesforce', 'Salesforce1', 'Mobile Roadie', 'MobileRoadie', 'Мобайл Роуди', 'Мобикарт', 'MobiCart', 'Гудбарбер', 'GoodBarber', 'Good Barber', 'GameSalad', 'Game Salad', 'Геймсэлэд', 'EachScape', 'Each Scape', ' Ичскейп ', 'BuildFire', 'Bizness Apps', 'BiznessApps', 'AppNotch', 'App Notch', 'AppMakr', 'App Makr', 'App Machine', 'AppMachine', 'Appery.io', 'AppBuilder', 'App Builder', 'App Factory', 'AppFactory', 'app.cat']








def find_phrases2(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = '\n'.join(str1.split())
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True


def find_phrases(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = ' '.join(str1.split())
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True



def getip():

    try:
        r45 = requests.get('https://ident.me', proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return Response1("201", '')

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return Response1("201", '')
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return Response1("201", '')

    print(r45.text)

    return r45


global time1lastrestart1
time1lastrestart1 = datetime.datetime.now()



def restartTor(sec=0,torWath=3, forc1=False):

    
    if not forc1:
        global time1lastrestart1
        diff1 = (datetime.datetime.now()-time1lastrestart1).seconds
        if diff1 < 60:#torWath:
            return 0

    #subprocess.run(["brew", "services", "restart", "tor"])
    #subprocess.run(["brew", "services", "reload", "tor"])
    subprocess.run(["pkill", "-HUP", "tor"])
    time1lastrestart1 = datetime.datetime.now()

    if sec == 0:
        sec = 1 #0.001
    time.sleep(sec)


def getCountryCode(ip=''):

    try:
        r45 = requests.get('https://freegeoip.app/json/' +
                           str(ip), proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return 0

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return 0
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return 0

    print(r45.text)
    d = json.JSONDecoder()
    rval = d.decode(r45.text)
    countryCode = rval['country_code']

    return countryCode


def switchProxyIfNeedForCountry():
    while getCountryCode(getip().text) != 'RU':
        restartTor()


def switchProxyIfNeedForGoogle():
    while google() != '200':
        restartTor()


def switchProxyIfNeed(target, targetlist3):
    if target not in targetlist3:
        while getCountryCode(getip().text) != 'RU' and google() != '200' and random.randint(1, 10) > 1:
            restartTor()
    getCountryCode(getip().text)


def google():
    q = 'mobsted'
    randUa = user_agent_rotator.get_random_user_agent()
    headersget = {

        'User-Agent': randUa,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    try:
        r = requests.get(url, headers=headersget,
                         proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return '201'

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return '201'


    print('google target :'+str(r.status_code))
    return str(r.status_code)










def find_all(a_str, sub):
    a_str = a_str.lower()
    sub = sub.lower()
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def recursiveUrl(url, link, depth, urlMain, strUrl, alreadyAdded,  hasSw, hasMan,  time1start1,diffTimeProcess,depthSite,torWath):
    diff1 = (datetime.datetime.now()-time1start1).seconds
    
    # nonlocal diffTimeProcess
    if diff1 > diffTimeProcess:
        return url
    if link is None:
        return url
    # nonlocal depthSite
    if depth == 2: #depthSite:
        return url
    # if not alreadyAdded:
    #     return url
    if  (len(hasMan)>0 or len(hasSw)>0): #len(alreadyAdded) > 1 and
        return url


    if link == '#####':
        link = {'href': '#####'}
    else:
        if not link.has_attr('href'):
            # print('no has attr')
            return url






    if len(link['href']) < 2:
        return url
    global visitedUrl
    if str(url)+link['href'] in visitedUrl:
        return None

    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']

    page = makeGetRequest(newUrl, str(urlMain),False,torWath)
    visitedUrl.append(str(url)+link['href'])

    newlink = []
    newlink1 = []
    mailtos = []
    if not page is None:
        soup1 = BeautifulSoup(page, 'html.parser')
        mailtos = soup1.select('a[href^=mailto]')
        newlink1 = soup1.select('a')
        newlink = newlink1




    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']
    page2 = makeGetRequest(newUrl, str(urlMain),False,torWath)



    mailtos2 = []
    if (page2):

        # if(page2.find('manifest')):
            # print('manifest!!1',url,newUrl)
            # time.sleep(9)

        if len(page2)>0:
          if not page2 is None:
            soup = BeautifulSoup(page2, 'html.parser')
            mailtos2 = soup.select('a[href^=mailto]')
            newlink = soup.select('a')

        if len(hasMan)==0:
         foundManifest(page2, hasMan)
        if len(hasSw)==0:
         foundSw(page2, hasSw)









    some_list = mailtos+mailtos2
    mailtos = list(dict.fromkeys(some_list))






    for i in mailtos:
        if i['href']:
            href = i['href']
            try:
                str1, str2 = href.split(':')
            except ValueError:
                continue

            str2 = str2.lower()
            if str2.find('?subject') != -1:
                try:
                    str2, str1 = str2.split('?subject')
                except ValueError:
                    continue
            if str2.find('mailto:') != -1:
                try:
                    str1, str2 = str2.split('ailto:')
                except ValueError:
                    continue
            str2 = str2.strip(' \t\n\r')
            str2 = str2.strip()


            if not str2 in alreadyAdded:
                alreadyAdded.append(str2)
                # print('++new mail')
                # print(alreadyAdded)



    if newlink is None:
        newlink = newlink1

    if newlink is None:
        return link

    if len(newlink) == 0:
        newlink = newlink1

    if len(newlink) == 0:
        return link

    for link1 in newlink:
        recursiveUrl(url, link1, depth + 1, urlMain, strUrl, alreadyAdded,  hasSw, hasMan, time1start1,diffTimeProcess,depthSite,torWath)
        # while threading.active_count() > max_process_count:
        #     time.sleep(random.randint(10, 30))

        # thread = threading.Thread(
        #     target=recursiveUrl, args=(url, link1, depth + 1, urlMain, strUrl, alreadyAdded,  hasSw, hasMan, time1start1,diffTimeProcess,depthSite,torWath))
        # thread.daemon = True
        # thread.start()




def markerStart(site):
    try:
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                                host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'

        # if conpg:
        #  with conpg:
        #      with conpg.cursor() as curpg:
        #         sql = " Set search_path =%(pgdb)s "
        #         params={"pgdb":pgdb}
        #         curpg.execute(sql,params)
        #         conpg.commit()


        with conpg:
             with conpg.cursor() as curpg:
              if True:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

                sql = " Update projects set inprogress=true where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()

                sql = " Update projects set startdate=now() where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                conpg.commit()

    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


def updateResult(site,alreadyAdded1, hasSw, hasMan ):
    try:
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                                host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'

        # if conpg:
        #  with conpg:
        #      with conpg.cursor() as curpg:
                # sql = " Set search_path =%(pgdb)s "
                # params={"pgdb":pgdb}
                # curpg.execute(sql,params)
                # conpg.commit()


        with conpg:
             with conpg.cursor() as curpg:
              sql = " Set search_path =%(pgdb)s "
              params={"pgdb":pgdb}
              curpg.execute(sql,params)

              sql = " set statement_timeout to 0 "
              params={"pgdb":pgdb}
              curpg.execute(sql,params)

            #   conpg.commit()
              if alreadyAdded1:
                if len(alreadyAdded1)>1:
                    alreadyAdded1.pop(0)
                    s=','
                    sql = " Update projects set \"resText\"=%(resText)s, \"resJson\"=%(resJson)s  where id=%(id)s"
                    # print(sql)
                    params={"resText":s.join(alreadyAdded1),"resJson":json.dumps(alreadyAdded1),"id":site[0]}
                    curpg.execute(sql,params)
                    # conpg.commit()
                    # for x in range(0, 99):
                    #     try:
                    #         curpg.execute(sql,params)
                    #         conpg.commit()
                    #     except:
                    #         time.sleep(1)
                    #         pass
                    #     finally:
                    #         break

              if hasSw:
                if len(hasSw)>0:
                    sql = " Update projects set \"hasSW\"=True  where id=%(id)s"
                    # print(sql)
                    params={"id":site[0]}
                    curpg.execute(sql,params)
                    # conpg.commit()
                    # for x in range(0, 99):
                    #     try:
                    #         curpg.execute(sql,params)
                    #         conpg.commit()
                    #     except:
                    #         time.sleep(1)
                    #         pass
                    #     finally:
                    #         break

              if hasMan:
                if len(hasMan)>0:
                    sql = " Update projects set \"hasMan\"=True  where id=%(id)s"
                    # print(sql)
                    params={"id":site[0]}
                    curpg.execute(sql,params)
                    # conpg.commit()
                    # for x in range(0, 99):
                    #     try:
                    #         curpg.execute(sql,params)
                    #         conpg.commit()
                    #     except:
                    #         time.sleep(1)
                    #         pass
                    #     finally:
                    #         break

                    
              if True:
                sql = " Update projects set \"torwath\"=%(torWath)s where id=%(id)s"
                params={"torWath":str(int(site[3] or 0)+1),"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()
                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #         break
                sql = " Update projects set \"difftimeprocess\"=%(diffTimeProcess)s where id=%(id)s"
                params={"diffTimeProcess":str(int(site[4] or 8)+1),"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()
                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #         break
                sql = " Update projects set \"depthsite\"=%(depthSite)s where id=%(id)s"
                params={"depthSite":str(int(site[5] or 1)+1),"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()
                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #         break

                sql = " Update projects set inprogress=false where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()
                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #         break

                sql = " Update projects set enddate=now() where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                conpg.commit()
                # print('wrote fixed!----------------------------')
                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #         break

    except psycopg2.DatabaseError as e:
        print('Error %s' % e)

def foundSw(page2,hasSw):
    if(page2.find('serviceWorker.register')):#navigator.serviceWorker.register
        # print('sw!!')
        hasSw.append('1')
        return True

    soup = BeautifulSoup(page2, 'html.parser')
    manifLink = [i.get('src') for i in soup.find_all('script') if i.get('src')] 
    for d in manifLink:
        page3 = makeGetRequest(d,d)
        if (page3):
            if(page3.find('serviceWorker.register')):#navigator.serviceWorker.register
                print('sw!! in js')
                hasSw.append('1')
                return True
         

def foundManifest(page2,hasMan):
    soup = BeautifulSoup(page2, 'html.parser')
    manifLink = soup.select('link[rel="manifest"]')
    for d in manifLink:
        # print('manifest!!1')
        hasMan.append(d)
        return True
#                 
    manifLink2 = soup.select('link[rel=manifest]')
    for d in manifLink2:
        # print('manifest!!2')
        hasMan.append(d)
        return True
#                 

# if len(hasMan)==0:
#     soup = BeautifulSoup(page2, 'html.parser')
#     manifLink = soup.select('link[rel]')
#     for d in manifLink:
#         print('link[rel]')
#         pprint.pprint(d)

    if len(hasMan)==0:
        soup = BeautifulSoup(page2, 'html.parser')
        manifLink = soup.select('link[rel="wlwmanifest"]')
        for d in manifLink:
            print('manifest!!3')
            hasMan.append(d)
            return True
#                 
        manifLink2 = soup.select('link[rel=wlwmanifest]')
        for d in manifLink2:
            print('manifest!!4')
            hasMan.append(d)
            return True
#                 


def main331(siteData, time1stamp1):
  
    p = psutil.Process(os.getpid())
    p.nice(8)
    param1=["python3.6", "./findergEmailPhoneOfSiteGeneralProcessV2.py"]#, str(siteData[0]), str(siteData[1]), str(siteData[2]), str(siteData[3]), str(siteData[4]), str(siteData[5]), str(siteData[6]), str(siteData[7]), str(siteData[8]), str(siteData[9]), str(siteData[10]), str(siteData[11]), str(siteData[12]), str(siteData[13]), str(siteData[14]), str(siteData[15]), str(siteData[16]), str(siteData[17]) 
    for d in siteData:
        param1.append(str(d))
    subprocess.run(param1)



def fromBase(thread_num1):
    try:
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                                host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()
                 
                sql = " set statement_timeout to 0 "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)


        



        # with conpg.cursor(name='foo145site') as curpg:
        limit4 = 900000 #+ int(random.randint(1, 49999))
        
        with conpg.cursor(name='foo145site_'+str(thread_num1)) as curpg:
            curpg.itersize = limit4
            print('request') # 
            sql = 'SELECT id, "Url", "NameThisColumn4", "NameThisColumn5" FROM objects where  "SwState"=\'2\' and "ManifestState"=\'2\' and ((\"NameThisColumn4\" is null or \"NameThisColumn4\" = \'\' or \"NameThisColumn4\" = \' \') or (\"NameThisColumn5\" is null or \"NameThisColumn5\"  = \'\' or \"NameThisColumn5\"  = \' \') )  limit ' + str(limit4) #  order by id asc  and (id::NUMERIC % 20)="+str(thread_num1)+"    desc where not inprogress or inprogress is null  --  (inprogress is null or not inprogress) 
            curpg.execute(sql)

            # print('return')
            # return curpg

            print('fetchall')
            res1 = curpg.fetchall()
            
        print('end fetchall')
        print(len(res1))
        return res1
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


        
           

def makeGetRequest(url, main, nproxy=False, restartTorT=3):


    if url[-4].find('.jpg') > -1:
        return None
    if url[-4].find('.png') > -1:
        return None
    if url[-5].find('.tiff') > -1:
        return None
    if url[-4].find('.tif') > -1:
        return None
    if url[-4].find('.bmp') > -1:
        return None
    if url[-5].find('.jpeg') > -1:
        return None
    if url[-4].find('.gif') > -1:
        return None
    if url[-4].find('.eps') > -1:
        return None
    if url[-4].find('.raw') > -1:
        return None

    rtext = None

    # if main.find('//')>-1:
    #     str1, str2, *_ = main.split('//')
    #     main = str2
    # if main.find('/')>-1:
    #     str3, str4, *_ = main.split('/')
    #     main = str3
    # if main.find('?')>-1:
    #     str3, str4, *_ = main.split('?')
    #     main = str3
    # if main.find('&')>-1:
    #     str3, str4, *_ = main.split('&')
    #     main = str3
    useTor = True
    # else:
    #  str2=main

    ext = tldextract.extract(main)
    ext2 = tldextract.extract(url)
    # print(ext.domain,ext2.domain)
    if ext.domain!=ext2.domain:
        return None

    global visitedUrl
    if str(url) in visitedUrl:
        return None
    visitedUrl.append(url)
    # print(url)
    counttryes = 0
    while True:
        useTor = True
        r = Response1("0", '')
        counttryes = counttryes+1
        if counttryes > 2:
            return None
        if counttryes > 1:
            nproxy = not nproxy
        try:
            randUa = user_agent_rotator.get_random_user_agent()


            # if True:
            #  r = requests.get(url, headers={
            #     'origin': url,
            #     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #     'user-agent': randUa
            #  },  stream=True, timeout=1)
            #  receive_timeout = 3
            #  fileamxSize = 1024*1024*1
            #  r.raise_for_status()
            #  if int(r.headers.get('Content-Length')) > fileamxSize:
            #   raise ValueError('response too large')
            #   return None
            #  size = 0
            #  start = time.time()
            #  for chunk in r.iter_content(1024):
            #     if time.time() - start > receive_timeout:
            #         raise ValueError('timeout reached')
            #         return None
            #     size += len(chunk)
            #     if size > fileamxSize:
            #         raise ValueError('response too large')
            #         return None
            #  r.close()

            if not nproxy:
             useTor = False
            #  print('useTor',useTor)
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, timeout=1, allow_redirects=True)
            else:
            #  print('useTor',useTor)
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, proxies=proxies, timeout=1, allow_redirects=True)

            if r.history:
                # print("Request was redirected")
                # for resp in r.history:
                #     print(resp.status_code, resp.url)
                # print("Final destination:")
                # print(r.status_code, r.url)
                return makeGetRequest(r.url,main, nproxy, restartTorT)
            # else:
            #     print("Request was not redirected")

            rtext = (r.text)
            r.close()
        except requests.ConnectionError as e:
            # print("[-] host die  ConnectionError: "+str(e))
            # counttryes = counttryes-1
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.exceptions.ReadTimeout as e:
            # print("[-] host die  ReadTimeout: "+str(e))
            # counttryes = counttryes-1
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
            if useTor:
             restartTor(0, restartTorT)

            continue
        except requests.exceptions.RequestException as e:
            if (str(str(e))).find('Failed to parse:') != -1:
                continue
        except:
            if useTor:
             restartTor(0, restartTorT)
            continue


        if int(r.status_code) != 200:
            if useTor:
             restartTor(0, restartTorT)
            continue
     
        return rtext

def run_tasks (function, args, pool, chunk_size = None): 
    results = pool.map (function, args, chunk_size) 


thread_num = 999
# if int(sys.argv[1])>-1:
#     thread_num = sys.argv[1]
#     print('thread_num',thread_num)
firstrun = True
pgdb = 'a7db574a'
pguser = 'postgres'
pgpswd = 'postgres'
pghost = '10.72.1.117'
pgport = '6432'
pgschema = 'a7db574a'





# while p_p._processes > 1:
#     p_p.close ()
#     print('--')
#     time.sleep(300)
# print('exit')

max_process_count = 32

max_site_count = 499
# inprogressM11=[]
p = psutil.Process(os.getpid())
p.nice(8)

while True:



    restartTor(0,3,True)
    if True:
        siteGen = fromBase(thread_num)
        # if firstrun:
        #     time.sleep(500)
        #     firstrun = False
        # print('for start - ',thread_num)
        adeed = 0
        siteDataParam = []
        for siteData in siteGen:
            # print(siteData)
            # time.sleep(120)
            if(random.randint(1, 999) == 1):
              psLoad = psutil.cpu_percent()
              while int(psLoad)>85 and psLoad!='0.0':
                print(' - psutil.cpu_percent() ',int(psLoad))
                print(' - psutil.cpu_percent() ',str(psLoad))
                time.sleep(60)
                psLoad = psutil.cpu_percent()
            # id1=siteData[0]
            # # url=siteData[1]
            # if id1 in inprogressM11:
            #   if(random.randint(1, 999) == 9):
            #     print(' - id1 in inprogressM11 ',int(id1))
            #   if(random.randint(1, 9999) == 9):
            #     inprogressM11=[]
            #   continue
            # continue
            # (id,          site,            protocol,   torWath,  diffTimeProcess,  depthSite,  enddate,  hasSW,  hasMan,  resText,  resJson,  resOver,  inprogress,  fixed,  tryesproxy,  statussite,  tryesnotproxy,  startdate)
            # (209029934, 'thecurlyfugu.com', 'http://',    2,       8,                 1,         None,   None,   None,     None,     None,     None,       None,      None,    None,          None,         None,        None)
            # (0,                 1,              2,        3,       4,                 5,           6,      7,      8,       9,        10,       11,        12,        13,       14,            15,           16,         17)
            adeed=adeed+1
            siteDataParam.append(siteData)
            # inprogressM11.append(id1)
            if adeed>=max_site_count:
            # if (int(siteData[0]) % 20) == int(thread_num):
            # if True:
                # print(siteData)
                # print(str(threading.active_count())+' - threading.active_count()')
                # print(getip())
                if(random.randint(1, 499) == 1):
                    print(str(threading.active_count())+' - threading.active_count()')

                while threading.active_count() > max_process_count:
                    if(random.randint(1, 399) == 1):
                    #  print(getip())
                     print(' - timewait')
                    time.sleep(random.randint(1, 90))

                    
                # print(str(threading.active_count())+' - threading.active_count()')
                thread = threading.Thread(
                    target=main331, args=(siteDataParam, datetime.datetime.now()))
                thread.daemon = True
                thread.start()
                # time.sleep(25)
                siteDataParam = []
                adeed = 0
        print('end of for - ',thread_num)
        time.sleep(30)
                
                 
                

  


while threading.active_count() > 1:
    p_p.close ()
    print('--')
    time.sleep(300)
print('exit')
