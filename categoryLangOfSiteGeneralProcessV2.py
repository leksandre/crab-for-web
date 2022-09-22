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


# from google.cloud import language_v1
# from google.cloud import speech_v1 as speech
# from google.cloud import language
# from google.cloud.speech_v1 import types
# # from kmip import enums



# from google.cloud.language import types
# from google.cloud import speech_v1 as speech
# from google.cloud.speech_v1.gapic import enums
# from google.cloud.speech_v1 import enums
# from enum import enums
# from google.cloud.speech_v1p1beta1 import enums
# from google.cloud.language import enums
# from google.cloud.speech_v1 import enums
# from google.cloud.language_v1 import enums
# from google.cloud.bigtable_admin_v2 import enums
# from google.cloud.speech_v1p1beta1 import enums
# from grafeas.grafeas_v1.gapic import enums



from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from matplotlib.font_manager import json_dump
import favicon
from numpy.core.defchararray import str_len
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

from googletrans import Translator
translator = Translator()

try:
    import requests
except ImportError:
    if sys.platform.startswith('linux'):
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cs.json'

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
    print('restartTor')
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

                sql = " Update objects set inprogress=true where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                # conpg.commit()

                sql = " Update objects set startdate=now() where id=%(id)s"
                params={"id":site[0]}
                curpg.execute(sql,params)
                conpg.commit()

    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


def updateResult(siteid,alreadyAdded1, hasSw, hasMan, keywords = '', descriptions = '' ):
    
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


              s=','
            #   conpg.commit()
              if keywords:
                if len(keywords)>0:
                 if str_len((keywords)) > 1:  
                    s=','
                    sql = " Update objects set \"NameThisColumn4\"=%(keywords)s where id=%(id)s"
                    # print(sql)
                    keywords = keywords.replace(chr(0x00), "")
                    print(siteid,(keywords),' language ')
                    params={"keywords":(keywords),"id":siteid}
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
            #   conpg.commit()
              if descriptions:
                if len(descriptions)>0:
                  if str_len((descriptions)) > 1:
                    s=','
                    sql = " Update objects set  \"NameThisColumn5\"=%(descriptions)s  where id=%(id)s"
                    # print(sql)
                    descriptions = descriptions.replace(chr(0x00), "")
                    print(siteid,(descriptions)," content ")
                    params={"descriptions":(descriptions),"id":siteid}
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





def main33(siteData, time1start):
    # time1start = datetime.datetime.now()
    # print(siteData[0])
    # print(siteData[1])
    
    # siteData = eval(siteData)
    #1
    
    # print(siteData[0])
    # print(siteData[1])
    # exit()

    # time.sleep(random.uniform(0, 1))
    p = psutil.Process(os.getpid())
    p.nice(10)

    # markerStart(siteData)
    # print('siteData')
    # print(siteData)
    # time.sleep(10)
    torWath = 6
    diffTimeProcess = 1
    depthSite = 2


    alreadyAdded1 = []
    hasSw = []
    hasMan = []
    alreadyAdded1.append(str(siteData[1]))
    links = []
 
 
 
    rtext = makeGetRequest(str(siteData[1]), str(siteData[1]),random.choice([True,False]),torWath)
    # print(rtext)
    # time.sleep(9)
    page2 = rtext
    mailtos2 = []

    # if (page2):
    #     if len(hasMan)==0:
    #      foundManifest(page2, hasMan)
    #     if len(hasSw)==0:
    #      foundSw(page2, hasSw)
    if random.randint(0,9999)==9:
          global visitedUrl
          visitedUrl = []

    # print(siteData)
    if not rtext is None:
        soup = BeautifulSoup(rtext, 'html.parser')
        links = soup.find_all('a')

    keywords6 = ''
    descriptions7 = ''
    
    # 
    # 
    #     try:

    #      print('')
    #     except:
    #      print('fail icon for '+str(siteData[1]))
    #      keywords6 = ''
        

    if not rtext is None:
     try:
        soup = BeautifulSoup(rtext, 'html.parser')
        try: 
         title = soup.find('title').text
        except Exception as e:
         title = ''
         print('basetitle',e)
   

        
        description = soup.find('meta', attrs={'name': 'description'})
 
        if "content" in str(description):
            description = description.get("content")
        else:
            description = ""
        
     
     
        
        h1 = soup.find_all('h1')
        h1_all = ""
        for x in range (len(h1)):
            if x ==  len(h1) -1:
                h1_all = h1_all + h1[x].text
            else:
                h1_all = h1_all + h1[x].text + ". "
    
    
        paragraphs_all = ""
        paragraphs = soup.find_all('p')
        for x in range (len(paragraphs)):
            if x ==  len(paragraphs) -1:
                paragraphs_all = paragraphs_all + paragraphs[x].text
            else:
                paragraphs_all = paragraphs_all + paragraphs[x].text + ". "
    
    
    
        h2 = soup.find_all('h2')
        h2_all = ""
        for x in range (len(h2)):
            if x ==  len(h2) -1:
                h2_all = h2_all + h2[x].text
            else:
                h2_all = h2_all + h2[x].text + ". "
    
    
    
        h3 = soup.find_all('h3')
        h3_all = ""
        for x in range (len(h3)):
            if x ==  len(h3) -1:
                h3_all = h3_all + h3[x].text
            else:
                h3_all = h3_all + h3[x].text + ". "
    
        allthecontent = ""
        allthecontent1 = str(title) + " " + str(description) + " " + str(h1_all) + " " + str(h2_all) + " " + str(h3_all) + " " + str(paragraphs_all)
        
        
        if True:    
            text_content = allthecontent1.replace('@', "")
            text_content = text_content.replace('©', "")
            text_content = text_content.replace(u'\N{COPYRIGHT SIGN}', "")
            text_content = text_content.replace(u'\N{TRADE MARK SIGN}', "")
            text_content = text_content.replace(u'\N{REGISTERED SIGN}', "")

            text_content = text_content.replace("\\r\\n", " ")
            text_content = text_content.replace("\\n", " ")
            text_content = text_content.replace("\\r", " ")
            text_content = ' '.join(text_content.split())
            text_content = ' '.join([text_content.strip() for line in text_content])
            allthecontent = text_content
            
        allthecontent = str(allthecontent)[0:999].lstrip()
        
        
        
        try:
            langCont = detect(allthecontent)
        except LangDetectException as e:
            print('baseLangDetectException',e)
            langCont='en_2'
        except Exception as e:
            print('baseLang_Exception',e)
            langCont='en_2'
        
        if siteData[2] is None or siteData[2]=='' or siteData[2]==' ' or (siteData[2]!=langCont) :
            # print(str(siteData[1]),langCont)
            keywords6 = langCont
            
            
        # print('try translate1',siteData[3])
        if siteData[3] is None or siteData[3]=='' or siteData[3]==' ':
            descriptions7 = allthecontent
            if langCont!='en' and str_len(allthecontent)>1:
                descriptions7 = ''
                print('try translate2 ',str_len(allthecontent))
                try:
                    translation = translator.translate(allthecontent).text
                    translation = str(translation)[0:999]
                    # print('try translate3',translation)
                    print('try translate3 "', allthecontent[0:29], '" : "', translation[0:29], '"')
                    time.sleep(10)
                    descriptions7 = translation
                except Exception as e:
                    print('Translator',e)
            if str_len((descriptions7)) < 2:
                descriptions7 = 'empty'
                
    
            # try:
            #         text_content = str(translation)
            #         text_content = text_content[0:1000]
            #         client = language_v1.LanguageServiceClient()
            #         type_ = enums.Document.Type.PLAIN_TEXT
            #         language = "en"
            #         document = {"content": text_content, "type": type_, "language": language}
            #         encoding_type = enums.EncodingType.UTF8
            #         response = client.classify_text(document)
            #         print(response.categories[0].name)
            #         print(str(int(round(response.categories[0].confidence,3)*100))+"%")
            # except Exception as e:
            #     print('analyze content',e)
    
    
    
     except Exception as e:
        print('base',e)
        
    if str_len((keywords6)) > 1 or str_len((descriptions7)) > 1:
     updateResult(siteData[0],alreadyAdded1, hasSw, hasMan, keywords6, descriptions7)


 
    # if not links:
    #     Object1 = '#####'
    #     recursiveUrl( str(siteData[1]), Object1, 0,
    #                  str(siteData[1]), str(siteData[1]), alreadyAdded1, hasSw, hasMan, time1start,diffTimeProcess,depthSite,torWath)
    # if links:
    #     some_list = links
    #     links = list(dict.fromkeys(some_list))
    #     for link in links:
    #         recursiveUrl( str(siteData[1]), link, 0,
    #                   str(siteData[1]), str(siteData[1]), alreadyAdded1, hasSw, hasMan,  time1start,diffTimeProcess,depthSite,torWath)








    # if len(hasMan)>0:
    #   if len(hasSw)>0:
    #     print('wrote 2 ',(alreadyAdded1), '; torwhat', siteData[1])
    #     if len(alreadyAdded1)>1:
    #         print('wrote 3 ',(alreadyAdded1), '; torwhat', siteData[1])

    # if len(hasMan)>0 and len(hasSw)==0:
    #     print('wrote 1  hasMan',(alreadyAdded1), '; torwhat', siteData[1])
    # if len(hasMan)==0 and len(hasSw)>0:
    #     print('wrote 1  hasSw',(alreadyAdded1), '; torwhat', siteData[1])

    # if len(hasMan)==0:
    #   if len(hasSw)==0:
    #       print('wrote empty ',(alreadyAdded1), '; torwhat', siteData[1])





    # updateResult(siteData[0],alreadyAdded1, hasSw, hasMan)

    # exit()



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
        limit4 = 90000 #+ int(random.randint(1, 49999))
        
        with conpg.cursor(name='foo145site_'+str(thread_num1)) as curpg:
            curpg.itersize = limit4
            print('request') # "NameThisColumn4", "NameThisColumn5", "NameThisColumn6", "NameThisColumn7", "NameThisColumn8" // or \"NameThisColumn5\"  = \'empty\'
            sql = 'SELECT id, "Url", "NameThisColumn4", "NameThisColumn5" FROM objects where  "SwState"=\'2\' and "ManifestState"=\'2\' and ((\"NameThisColumn4\" is null or \"NameThisColumn4\" = \'\' or \"NameThisColumn4\" = \' \') or (\"NameThisColumn5\" is null or \"NameThisColumn5\"  = \'\' or \"NameThisColumn5\"  = \' \' ) ) and \"NameThisColumn4\"<>\'en\'  and \"NameThisColumn4\"<>\'unknown\' limit ' + str(limit4) #  order by id asc  and (id::NUMERIC % 20)="+str(thread_num1)+"    desc where not inprogress or inprogress is null  --  (inprogress is null or not inprogress) 
            curpg.execute(sql)

            # print('return')
            # return curpg

            print('fetchall')
            res1 = curpg.fetchall()
            
        print('end fetchall')
        print(len(res1))
        random.shuffle(res1)
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
    print(url,ext.domain,ext2.domain)
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

            rtext = (r.text)
            
            if not(rtext):
                if r.history:
                    print("Request was redirected")
                    # for resp in r.history:
                    #     print(resp.status_code, resp.url)
                    # print("Final destination:")
                    # print(r.status_code, r.url)
                    return makeGetRequest(r.url,main, nproxy, restartTorT)
                else:
                    print("Request was not redirected")
                
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


thread_num = 999
firstrun = True
pgdb = 'a7db574a'
pguser = 'postgres'
pgpswd = 'postgres'
pghost = '10.72.1.117'
pgport = '6432'
pgschema = 'a7db574a'
max_process_count = 199


while True:


    p = psutil.Process(os.getpid())
    p.nice(10)
    # siteGen = sys.argv
    # siteGen.pop(0)
    



    restartTor(0,3,True)
    if True:

        # for siteData in siteGen:
        #2
        

        siteGen = fromBase(thread_num)
        adeed = 0
        siteDataParam = []
        for siteData in siteGen:      
               
                if(random.randint(1, 499) == 1):
                    print(str(threading.active_count())+' - threading.active_count() in process')

                while threading.active_count() > max_process_count:
                    if(random.randint(1, 399) == 1):
                    #  print(getip())
                     print(' - timewait in process')
                    time.sleep(random.randint(1, 90))

                    
                # print(str(threading.active_count())+' - threading.active_count()')
                # thread = threading.Thread(
                #     target=main33, args=(siteData, datetime.datetime.now()) )
                # thread.daemon = True
                # thread.start()
                #3
                
                main33(siteData, datetime.datetime.now())
          
        print('end of for in process -----')
        # time.sleep(120)
                
while threading.active_count() > 1:
    print('--')
    time.sleep(10)
print('exit')

    
 