#-*- coding:cp949-*-
from bs4 import BeautifulSoup
#from django.utils.encoding import smart_str, smart_unicode
from urllib import *
import urllib.robotparser
from ctypes import *  
import urllib
import time, traceback, re, os
import sqlite3
import codecs
import cgi
import sys
import konlpy
import pprint
import nltk
from konlpy.tag import Komoran
from konlpy.tag import Twitter
from nltk.tokenize import RegexpTokenizer
from SubDB import *

tokenizer = None
tagger = None

dir = './smi/'


def allFiles(dir):
    tempFileList = []
    filenames = os.listdir(dir)
    for filename in filenames:
        full_filename = os.path.join(dir, filename)
        tempFileList.append(full_filename)

    
    return tempFileList

def checkKREN(contents):
    "다운받은 smi 파일이 정상인지 체크"
    fileList = []
    
    #contents = contents.decode('cp949')
    pKRCC = re.compile(r'<P Class=KR.*>', re.IGNORECASE)
    pENCC = re.compile(r'<P Class=EN.*>', re.IGNORECASE)
    
    #print (contents)
    try:
       if(bool(re.search(pKRCC, contents))):
            if(bool(re.search(pENCC, contents))):
                return True
        
       else:
            print ("File contents error!!!")
            return False
    except:
        print ("File import error!!!")
        return False


def sortTXT(contentsList): 
    "smi파일내용 정렬"
    contents = contentsList[1][:]
    print(type(contents))
    
    #contents = contents.decode('utf-8').encode('cp949', 'ignore').decode('cp949')
    #contents = contents.decode('cp949', 'ignore')
    #contents = contentstemp
    print (type(contents))
    pStyle = re.compile('<br>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(' ', contents)
    pStyle = re.compile('<font color=.*?>', re.IGNORECASE)
    contents = pStyle.sub(' ', contents)
    pStyle = re.compile('</font>', re.IGNORECASE)
    contents = pStyle.sub(' ', contents)
    pStyle = re.compile('<HEAD(.*?)>(.*?)</HEAD>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('<!--(.*?)-->', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('<br>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(' ', contents)
    pStyle = re.compile('<SAMI>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('<BODY>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('</SAMI>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('</BODY>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('<i>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    pStyle = re.compile('</i>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub('', contents)
    #print (contents)
    pStyle = re.compile(r'<SYNC Start=\d+><P Class=KR.*>&nbsp;')
    contents = pStyle.sub('', contents)
    pStyle = re.compile(r'<SYNC Start=\d+><P Class=EN.*>&nbsp;')
    contents = pStyle.sub('', contents)

    pStyle = re.compile(r'( \r\n{1}$\r\n)', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(r'', contents)
    #print (contents)
    pStyle = re.compile(r'( \r\n{2,})', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(r'\r\n', contents)

    
    
    #print (contents)
    pStyle = re.compile(r'\n$', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(r'', contents)
    #print (contents)
    pStyle = re.compile(r' {2,}', re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(r' ', contents)
    pStyle = re.compile(r'\r\n', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contents = pStyle.sub(r' ', contents)

   

    #print (contents)
    #print ("------------")
    contentsKRTemp = []
    contentsENTemp = []
    contentsKR = []
    contentsEN = []
    pStyleKR = re.compile(r'<SYNC Start=(\d+)><P Class=KR.*?>(.+?)<', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    pStyleEN = re.compile(r'<SYNC Start=(\d+)><P Class=EN.*?>(.+?)<', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contentsKRTemp = pStyleKR.findall(contents)
    contentsENTemp = pStyleEN.findall(contents)
    
   
    #print (contentsKRTemp)
    #pTime = re.compile(r'\S{2}\Z')   
    pTime = re.compile('[0-9]{2}\Z')

    for i in range(0, len(contentsKRTemp)):
        #print ("contentskrtemp")
        #if(contentsKRTemp[i][1] == '  '):
        #    continue;
        #contentsKRTemp[i][1] = str(contentsKRTemp[i][1]).strip()
        contentsKR.append(list(contentsKRTemp[i]))
        contentsKR[i][0] = pTime.sub('', contentsKR[i][0])
        #smart_str(contentsKR[i][1])
        #print (contentsKR[i][0])
        #print (contentsKR[i][1])
            
    for i in range(0, len(contentsENTemp)):
        contentsEN.append(list(contentsENTemp[i]))
        contentsEN[i][0] = pTime.sub('', contentsEN[i][0])
   
    #print (contentsKR[0][1])
    #print contentsEN
    oneTotalSubList = joinKREN(contentsKR, contentsEN)
    #pprint.pprint(oneTotalSubList)
    return oneTotalSubList
    

def joinKREN(list_kr, list_en):
   
    totalSubList = []
    totalSubListTemp = []
    totalSubListTemp2 = []
   
    if (len(list_kr) <= len(list_en)):
        for i in range(0, len(list_kr)):
            for j in range(0, len(list_en)):
                if(list_kr[i][0] != list_en[j][0]):
                    pass
                else:
                    totalSubListTemp.insert(0, list_kr[i][0])
                    totalSubListTemp.insert(1, list_en[j][1])
                    totalSubListTemp.insert(2, list_kr[i][1])
                    totalSubList.append(list(totalSubListTemp[0:3]))
                    break
    else:
        for i in range(0, len(list_en)):
            for j in range(0, len(list_kr)):
                if(list_en[i][0] != list_kr[j][0]):
                    pass
                else:
                    totalSubListTemp.insert(0, list_en[i][0])
                    totalSubListTemp.insert(1, list_en[i][1])
                    totalSubListTemp.insert(2, list_kr[j][1])
                    totalSubList.append(list(totalSubListTemp[0:3]))
  
    return totalSubList
 
def makeFileName(_FileList):
    mkFileNameList = _FileList[:]
    pStyle = re.compile('./smi/')
    for i in range(0, len(FileList)):
        mkFileNameList[i] = pStyle.sub('', mkFileNameList[i])
        
    return mkFileNameList


def getKorNoun(body):#태그없앤 content에서 명사만 추출하기
    contents = body[:]
    
    contents = re.sub('[^가-힣 \n]+', '', contents)
    #print (contents)
   
    kkma = konlpy.tag.Kkma() #-Xmx128m 로 바꾸기
    #print("Get nouns from contents...")
    keywords = kkma.nouns(contents)
    #print (type(keywords))
    #print ("kkma   : ", keywords)
    pSub = re.compile("sub_")
    for i in range(0, len(keywords)):
        keywords[i] = re.sub(keywords[i], "sub_"+str(keywords[i]), keywords[i])
    #keywords = list(set(keywords))
    print ("Keywords : ", keywords)
    return keywords
    
def getEngNoun(contents):
    tokenizer = RegexpTokenizer("[\w']+")
    keywords = tokenizer.tokenize(contents)
    pStyle = re.compile("'")
    pStyle2 = re.compile(r"\.")
    #pSub = re.compile("sub_")
    for i in range(0, len(keywords)):
        keywords[i] = pStyle.sub("", keywords[i])
        keywords[i] = pStyle2.sub("", keywords[i])
        keywords[i] = re.sub(keywords[i], "sub_"+str(keywords[i]), keywords[i])
    keywords = list(set(keywords))
    print ("keywords : ", keywords)
    return keywords

def FillSpacePacket(dataLen, index):
    """패킷의 자릿수를 채워야 할때 공백(' ')으로 빈공간을 채워줌
    dataLen : 분석을 원하는 변수의 길이
    index : space로 채울 인덱스 최대값
    ex)
    data = 'abcd'
    data += FillSpacePacket(data.__len__(), 5)
    print(data)
    결과 : 'abcd  '
    빈칸 두개 생성"""
    index += 1
    space = ''
    if dataLen < index:
        for count in range(0, index-dataLen):
            space += ' '
    return space

def isASCII(text): 
   """ASCII문자인지 판별. text에 ASCII가 아닌 문자가 한개라도 있으면 False, 없으면 True"""
   return not bool(re.search('[^\x00-\x7E]', text))

def __Len_Cstyle__(text):
   """text를 C 스타일 길이로 구함"""
   CLen = 0
   for i in text:
      if isASCII(i):
         CLen += 1
      else: CLen += 2
   return CLen
   
if __name__ == '__main__':
    print ('starting SubEditor.py...')
    totalSubList = []
    oneTotalSubList= []
    fileNameList = []
    #openFile()
    sendSubList = []
    sendSubListTemp = []
    tempFileList = allFiles(dir)
    
    FileList = checkKREN(tempFileList)
    fileNameList = makeFileName(FileList)
    #print (fileNameList)
    for i in range(0, len(FileList)):
        oneTotalSubList = sortTXT(FileList[i])
        
        for j in range(0, len(oneTotalSubList)):
            sendTitle = fileNameList[i]
            pStyle = re.compile(".smi")
            sendTitle = pStyle.sub('', sendTitle)
            sendEN = oneTotalSubList[j][1]
           
            sendKO = oneTotalSubList[j][2]
            #print ("sendEN : ", sendEN)
            sendENKeywords = getEngNoun(sendEN)
            sendENKeywordsLen = len(sendENKeywords)

            sendKOKeywords = getKorNoun(sendKO)
            sendKOKeywordsLen = len(sendKOKeywords)

            pStyle = re.compile("'")
            sendEN = pStyle.sub("''", sendEN)
            sendKO = pStyle.sub("''", sendKO)

            sendSubList.insert(0, sendTitle) # 0 : 타이틀
            sendSubList.insert(1, sendEN) # 1 : 영문장
            sendSubList.insert(2, sendKO) # 2 : 한국어문장
            sendSubList.insert(3, sendENKeywordsLen+sendKOKeywordsLen) # 3 : 영단어+한단어 개수                
            for k in range(4, 4+sendENKeywordsLen):
                sendSubList.insert(k, sendENKeywords[k-4])
                
            for k in range(0, sendKOKeywordsLen):
                sendSubList.insert(k+4+sendENKeywordsLen, sendKOKeywords[k])
           
            sendSubtitle(sendSubList)       
    #pprint.pprint (sendTitle)

    #sendPacket(sendList)
