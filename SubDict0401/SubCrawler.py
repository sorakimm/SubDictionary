#-*- coding: cp949-*-
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib import robotparser
import urllib
from urllib import *
import urllib.robotparser
import time, traceback, re, os, os.path
import sqlite3
import cgi
import sys
from SubDB import SubDB
import SubEditor
import socket

sType = dict(B_C_NOTIFY_SUBTITLE = '201', B_C_NOTIFY_SUBURL = '202', B_C_REQ_SUBURL = '203' , B_S_ANS_SUBURL = '204', B_C_REQ_WORD = '509', B_S_ANS_SUBTITLE = '504', B_S_ANS_COUNT = '503') # ��Ŷ Ÿ��

crawler_name = 'smigle_crawler'
gom_mainPage = 'http://gomtv.com/'
gom_gomMainPage = 'http://gom.gomtv.com'
gom_mainBoardPage = 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=l&menu=subtitles&lang=3&page=1&md5key='
gom_searchMainBoard = '/main/index.html?ch=subtitles&pt=l&menu=subtitles&lang=3&sWord=&page='
gom_boardURL = 'http://gom.gomtv.com/main/index.html/'
gom_DownCHPT_URL = 'ch=subtitles&pt=down&'

smiDir = './smi/'
temp_startPage = 1
rp = robotparser.RobotFileParser(gom_mainPage + 'robots.txt')
rp.read()

##############################################################
# SOCKET NETWORKING
HOST = '127.0.0.1'                # The remote host
PORT = 10001        # The same port as used by the server
s = socket.socket()
##############################################################


def canFetch(self, url):
    return rp.can_fetch(crawler_name, url)

def getGomLastBoard(url):
    GomBoard = urllib.request.urlopen(url).read()
    #unicode(GomBoard, 'utf-8').decode('utf-8').encode('utf-8')
    soup = BeautifulSoup(GomBoard, "html.parser")
    lastBoard = soup('a', {'class':'next_last'})

    temp = str(lastBoard[0])
    lastBoardNumTemp = temp.split(' ')[2]
    lastBoardNum = int(lastBoardNumTemp.rsplit('=', 1)[-1].rstrip('"'))
    return lastBoardNum


def getGomAllBoardPageURL(lastpage):
    pageURLList = []
    for page in range(temp_startPage, lastpage+1):
        pageURL = gom_gomMainPage + gom_searchMainBoard + str(page)
        pageURLList.append(pageURL)

    return pageURLList

    
def getGomTitleLink(url):
    print ("getGomTitleLink Start!")
    url = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=l&menu=subtitles&lang=3&page=1&md5key=']
    for u in range(0, len(url)):
        time.sleep(1)
        gomPageTemp = urllib.request.urlopen(url[u]).read()
        #gomPageTemp = urllib2.urlopen(url[u]).read()
        gomPage= str(gomPageTemp).replace("$", '')
        soup = BeautifulSoup(gomPage, "html.parser")
        rTitles = re.compile('.+prepage.+')
        titlesTemp = soup('a', {'href':rTitles})
        titlesList = []
        sTitleURLListTemp = []
        sTitleURLList = []
        
        for i in range(0, len(titlesTemp)):
            titles = re.sub('&amp;', '&', str(titlesTemp[i]))
            titlesList.append(titles)
            titlesList[i] = titlesList[i].split(' ')[1]
            title = titlesList[i].strip('href="')
            titleURL = 'http://gom.gomtv.com'+title
            
            sTitleURLList.insert(0, sType['B_C_NOTIFY_SUBURL'])
            sTitleURLList.insert(1, str(len(titleURL)))
            sTitleURLList.insert(2, titleURL)
            db.connect(HOST, PORT)
            db.sendURL(sTitleURLList)
            db.closesocket()
               

def getGomDownLink(url):
    #url = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910618&prepage=1&md5key=&md5skey=']
    print ("getGomDownLink Start!")
    rDownLinkList = []
    rIntCapSeq = re.compile('\d+')
    rTitle = re.compile("\'(.+?).smi\'")
    down_cnt = 0
    contentsList = []

    gomDown = urllib.request.urlopen(url)
    textTemp = gomDown.read()
    textTemp = textTemp.decode('utf-8')
    text = str(textTemp).replace("$", '')
    soup = BeautifulSoup(text, 'html.parser')
    rDownLink = soup('a', {'class':'btn_type3 download'})
    if(len(rDownLink) == 0):
        return 0
    rDownLink[0] = str(rDownLink[0])
    rDownLinkList.insert(0, rDownLink[0])
    intSeq = rIntCapSeq.findall(str(rDownLinkList[0]))[1]
    capSeq = rIntCapSeq.findall(str(rDownLinkList[0]))[2]
    temp = rTitle.findall(str(rDownLinkList[0]))[0]
    titleTemp = str(rTitle.findall(str(rDownLinkList[0]))[0])
    fileName = str(titleTemp.split("'")[-1])
    #print ("fileName : ", smart_unicode(fileName))

    fullDownURL= gom_boardURL+quote(fileName)+'?'+gom_DownCHPT_URL+'intSeq='+str(intSeq)+'&'+'capSeq='+str(capSeq)
    req = urllib.request.Request(fullDownURL)
    res = urllib.request.urlopen(req)
    #fileName = smart_unicode(fileName)

    #http://gom.gomtv.com/main/index.html/Femme.Fatales.S01E01.720p.HDTV.x264.smi?ch=subtitles&pt=down&intSeq=910618&capSeq=908517
    contents = res.read()
       
    contentsList.insert(0, fileName)
    contentsList.insert(1, contents)
    return contentsList

        
def checkUpdatedDownURL():
    time.sleep(10)
    page = 1
    check_cnt = 0
    temp = 0
    updatedTitlesList = []

    while (temp != page):
        #print "check while start!"
        #print "check page : ", page
        updatedPageURL = gom_gomMainPage + gom_searchMainBoard + str(page)
        getGomTitleLink(updatedPageURL)
        while True:
            db.connect(HOST, PORT)
            db.reqURL() # titleURL ��û
            db.closesocket()
            
            db.connect(HOST, PORT) 
            updatedTitleURL = db.recvURL()
            db.closesocket()

            if(len(updatedTitleURL) == 0): # ������ titleURL�� ���̰� 0�� �� (���� ��Ŷ�� URL ���̰� 0�̸� ����)
                break;
            updatedTitleList.append(updatedTitleURL)

        if(len(updatedTitleList) >15):
            page = page+1
            
        temp = temp+1
    

    return updatedTitleList
    
          

def contentsEditSend(contentsList):
    print ("contentsEditSend Start!")
    sendSubList = []
    #contentsList[0] : FileName
    #contentsList[1] : Contents
    if(contentsList == 0) :
            print ("FileName - ",contentsList[0], " contents Error!")
    else:
        if(SubEditor.checkKREN(contentsList[1]) == True):        # �ڸ� ����
            oneSortedSubList = SubEditor.sortTXT(contentsList)
            for j in range(0, len(oneSortedSubList)):
                sendTitle = contentsList[0]
                pStyle = re.compile(".smi")
                sendTitle = pStyle.sub('', sendTitle)
                sendEN = oneSortedSubList[j][1]
           
                sendKO = oneSortedSubList[j][2]
                #print ("sendEN : ", sendEN)
                sendENKeywords = SubEditor.getEngNoun(sendEN)
                sendENKeywordsLen = len(sendENKeywords)

                sendKOKeywords = SubEditor.collectWord(sendKO)
                sendKOKeywordsLen = len(sendKOKeywords)

                pStyle = re.compile("'")
                sendEN = pStyle.sub("''", sendEN)
                sendKO = pStyle.sub("''", sendKO)

                sendSubList.insert(0, sendTitle) # 0 : Ÿ��Ʋ
                sendSubList.insert(1, sendEN) # 1 : ������
                sendSubList.insert(2, sendKO) # 2 : �ѱ����
                sendSubList.insert(3, str(sendENKeywordsLen+sendKOKeywordsLen)) # 3 : ���ܾ�+�Ѵܾ� ����                
                for k in range(4, 4+sendENKeywordsLen):
                    sendSubList.insert(k, sendENKeywords[k-4])
                
                for k in range(0, sendKOKeywordsLen):
                    sendSubList.insert(k+4+sendENKeywordsLen, sendKOKeywords[k])
                
                db.connect(HOST, PORT)
                db.sendSubtitle(sendSubList)
                db.closesocket()

        else:
            print ("Wrong KREN SMI")
   
        


db = SubDB()

class AllStatesFetched(Exception):
    def __init__(self):
       pass

if __name__ == '__main__':
    print ('starting Gom Crawl.py...')
    lastBoardNum = getGomLastBoard(gom_mainBoardPage)
    lastBoardNum = 10
    print ("lastBoardNum : ", lastBoardNum)
    pageURLList = []
    pageURLList = getGomAllBoardPageURL(lastBoardNum)
     
    getGomTitleLink(pageURLList)
    
    titleList = []
    #while True:
    #    db.connect(HOST, PORT)
    #    db.reqURL() # titleURL ��û
    #    db.closesocket()
        
    #    db.connect(HOST, PORT) 
    #    titleURL = db.recvURL()
    #    db.closesocket()

    #    if(len(titleURL) == 0): # ������ titleURL�� ���̰� 0�� �� (���� ��Ŷ�� URL ���̰� 0�̸� ����)
    #        break;
    #    titleList.append(titleURL)
    
    titleList = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=908441&prepage=5&md5key=&md5skey=', 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=907827&prepage=7&md5key=&md5skey=']
    #print (titleList[0])
    
    #for i in range(0, len(titleList)):
    #    contentsList = getGomDownLink(titleList[i])
    #    contentsEditSend(contentsList)
                       
    while 1:
        print ("checkUpdatedDownURL START! ")
        #updatedTitleList = []    
        time.sleep(100)
        #updatedTitleList = checkUpdatedDownURL()  
        updatedTitleList = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=908441&prepage=5&md5key=&md5skey=', 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=907827&prepage=7&md5key=&md5skey=']
    
        for i in range(0, len(updatedTitleList)):
            updatedContentsList = getGomDownLink(updatedTitleList[i])
            contentsEditSend(updatedContentsList)    
      
    #s.close()          
            