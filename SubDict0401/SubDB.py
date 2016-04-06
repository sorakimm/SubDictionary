#-*- coding:cp949-*-
import socket
import re
import pprint
sType = dict(B_C_NOTIFY_SUBTITLE = '201', B_C_NOTIFY_SUBURL = '202', B_C_REQ_SUBURL = '203' , B_S_ANS_SUBURL = '204', B_C_REQ_WORD = '509', B_S_ANS_SUBTITLE = '504', B_S_ANS_COUNT = '503') # 패킷 타입
sMode = dict(MODE_PAGE_URL = '1', MODE_TITLE_URL = '2') # URL 타입
from C_Python_Socket import C_Python_Socket
import time

##############################################################
# SOCKET NETWORKING
HOST = '192.168.0.185'                # The remote host
#HOST = '127.0.0.1'
PORT = 10000        # The same port as used by the server
s = socket.socket()
##############################################################

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
   return not bool(re.search('[^\x00-\x7F]', text))

def __Len_Cstyle__(text):
   """text를 C 스타일 길이로 구함"""
   CLen = 0
   for i in text:
      if isASCII(i):
         CLen += 1
      else: CLen += 2
  
   return CLen
 
class SubDB():
    def connect(self, ip, port):
        """사용하기 전 주의 사항
        1) import socket
        2) 전역변수 s = socket.socket()를 선언"""
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = ip                # The remote host
        PORT = port              # The same port as used by the server
        s.connect((HOST, PORT))

    def closesocket(self):
        s.close() 

    def sendSubtitle(self, sendSubList):
        
        data = ''
        dataLen = ''
        sendData = ''
        eachWordLenList = []
        subEnLen = 0
        subKOLen = 0
        wordNumLen = 0
        data2 = ''
        titleLen = __Len_Cstyle__(sendSubList[0])
        
        subENLen = __Len_Cstyle__(sendSubList[1])
        
        subKOLen = __Len_Cstyle__(sendSubList[2])
        
        #wordNumLen = __Len_Cstyle__(str(sendSubList[3]))
       
        for i in range(0, int(sendSubList[3])):
            eachWordLen = __Len_Cstyle__(sendSubList[4+i])
            eachWordLenList.append(eachWordLen)
        

        #wordTupleList = []
        #titleTuple = (titleLen, sendSubList[0])
        #subENTuple = (subENLen, sendSubList[1])
        #subKOTuple = (subKOLen, sendSubList[2])
        #wordNumTuple = (wordNumLen, str(sendSubList[3]))
        #for i in range(0, wordNumLen):
        #    wordTupleList.append((eachWordLenList[i], sendSubList[4+i]))
        #sendSub = C_Python_Socket.generalSend(B_C_NOTIFY_SUBTITLE,)
              
            
        
        data += sType['B_C_NOTIFY_SUBTITLE']
        data += '\0'
        data += FillSpacePacket(data.__len__(), 3)
       
        data += str(titleLen)
        data += '\0'
        data += FillSpacePacket(data.__len__(), 3+4)
        data += sendSubList[0]
        
        data += str(subENLen)
        data += '\0'
        subENLenSpace = FillSpacePacket(str(subENLen).__len__(), 2)
        data += subENLenSpace
        data += sendSubList[1]

        data += str(subKOLen)
        data += '\0'
        subKOLenSpace = FillSpacePacket(str(subKOLen).__len__(), 2)
        data += subKOLenSpace
        data += sendSubList[2]

        #data += sendSubList[3]
        #data += '\0'
        #wordNumLenSpace = FillSpacePacket(str(sendSubList[3]).__len__(), 2)
        #data += wordNumLenSpace
        data2 = data

        for i in range(0, int(sendSubList[3])):
            sendData = ''
            data += str(eachWordLenList[i])
            data += '\0'
            eachWordSpace = FillSpacePacket(str(eachWordLenList[i]).__len__(), 2)
            data += eachWordSpace
            data += sendSubList[4+i]


            dataLen = __Len_Cstyle__(data) + 8
            dataLen = str(dataLen)
            dataLen += '\0'
            dataLen += FillSpacePacket(dataLen.__len__(), 7)
            sendData += dataLen
            sendData += data
            sendData = sendData.encode('cp949')
      
            pprint.pprint (sendData.decode('cp949'))

            f = open('./smi/edit6.txt', 'a')
            f.write(sendData.decode('cp949'))
            f.write('\n\n')
            f.close()

            try:
                #pprint.pprint (sendSubList[0])
                self.connect(HOST, PORT)
                time.sleep(0.5)
                s.sendall(sendData)
                #data = data2
                self.closesocket()
            except:
                print("packet send error!")
                pass

            data = data2

    def sendURL(self, sendURLList):
        data = ''
        dataLen = ''
        sendData = ''
        #print ("sendURLList[0] : ", sendURLList[0]) # 패킷 타입
        #print ("sendURLList[2] : ", sendURLList[1]) # url 길이
        #print ("sendURLList[3] : ", sendURLList[2]) # url
        
        #sendURLLen = __Len_Cstyle__(str(sendURLList[1]))
        sendURLLen = __Len_Cstyle__(sendURLList[1])
                         
        data += sendURLList[0] # 패킷 타입
        data += '\0'
        data += FillSpacePacket(data.__len__(), 3)
       
        data += sendURLList[1] # url 길이
        data += '\0'
        subPageURLLenSpace = FillSpacePacket(sendURLLen, 2)
        data += subPageURLLenSpace
       
        data += sendURLList[2] # url

        dataLen = __Len_Cstyle__(data) + 8
        dataLen = str(dataLen)
        dataLen += '\0'
        dataLen += FillSpacePacket(dataLen.__len__(), 7)
        sendData += dataLen
        sendData += data
        sendData = sendData.encode('cp949')
        
        #pprint.pprint (sendData)
        s.sendall(sendData)
        
    
    def reqURL(self):
        print("reqURL!")
        data = ''
        dataLen = ''
        sendData = ''
        
                  
        data += sType['B_C_REQ_SUBURL']
        data += '\0'
        data += FillSpacePacket(data.__len__(), 3)
       
        dataLen = __Len_Cstyle__(data) + 8
        dataLen = str(dataLen)
        dataLen += '\0'
        dataLen += FillSpacePacket(dataLen.__len__(), 7)
        sendData += dataLen
        sendData += data
        sendData = sendData.encode('cp949')
        
        print ("send req url data")
        s.sendall(sendData)
   
    def recvURL(self):
        b_size = ''
        b_type = ''
        b_urllen = ''
        b_url = ''
        data = s.recv(1024)
        data = data.decode('cp949')
             
        if not data:
            print ("no data received")
            pass

        print ('Received URL----------', data)
        b_listTemp = []
        
        for i in range(0, 7):
            if(data[i] != '\0'):
                b_size += data[i]

        for i in range(8, 11):
            if(data[i] != '\0'):
                b_type += data[i]
        
        for i in range(12, 15):
            if(data[i] != '\0'):
                b_urllen += data[i]
        
        for i in range(0, 0+int(b_urllen)):
            b_url += data[i+16]             
        

       
        #print ("b_type : ", b_type)
        #print ("b_urllen : ", b_urllen)
        #print ("b_url : ", b_url)
        
        #b_list = "".join(b_listTemp)
        
        #print ("b_list : ", b_list)

        print ("-------------------------")
     
        return b_url

   