#-*- coding: cp949-*-
from SubDB import SubDB

sdb = SubDB()


class c_searcher:
    
    def __init__(self, keyword):
        self.keyword = keyword
    
    
    def SubSearcher(self):
        ret = []
        #sdb.reqSUB(keyword)
        #subNum = sdb.recvSUBNum()
        #for i in range(0, subNum):
        #    ret.append(sdb.recvSUB())
        ret = [["Downton.Abbey.S04E01.720p.HDTV.x264-FoV", "Was there really no warning?", '��ҿ� �ٸ� ���� ������?'], 
               ['Downton.Abbey.S04E01.720p.HDTV.x264-FoV', "We don't have a choice.", '�츮�� ���ñ��� ����'], 
               ['Dexter.S0E05', 'think this is our guy\'s work?', '�̰͵� �� �ڽ� ���ΰ� ����?'], 
               ['title4', 'good english4', '�� �ױ۸���4'], 
               ['title5', 'good english5', '�� �ױ۸���5'], 
               ['title6', 'good english6', '�� �ױ۸���6'],
               ['title7', 'good english7', '�� �ױ۸���7'], 
               ['title8', 'good english8', '�� �ױ۸���8'], 
               ['title9', 'good english9', '�� �ױ۸���9'], 
               ['title10', 'good english10', '�� �ױ۸���10'], 
               ['title11', 'good english11', '�� �ױ۸���11'],
               ['title12', 'good english11', '�� �ױ۸���11']]

        for i in range(0, len(ret)):
            ret[i] = tuple(ret[i])
        
        return tuple(ret)
    
    def DictSearcher(self):
        ret = []
        #sdb.reqSUB(keyword)
        #subNum = sdb.recvSUBNum()
        #for i in range(0, subNum):
        #    ret.append(sdb.recvSUB())
        #ret = [['title', 'good english', '�� �ױ۸���'.encode('utf-8')], ['title2', 'good english2', '�� �ױ۸���2'.encode('utf-8')], ['title3', 'good english3', '�� �ױ۸���3'.encode('utf-8')], ['title4', 'good english4', '�� �ױ۸���4'.encode('utf-8')], ['title5', 'good english5', '�� �ױ۸���5'.encode('utf-8')], ['title6', 'good english6', '�� �ױ۸���6'.encode('utf-8')], ['title7', 'good english7', '�� �ױ۸���7'.encode('utf-8')], ['title8', 'good english8', '�� �ױ۸���8'.encode('utf-8')], ['title9', 'good english9', '�� �ױ۸���9'.encode('utf-8')], ['title10', 'good english10', '�� �ױ۸���10'.encode('utf-8')]]
        ret = [['dicttitle1', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle2', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['dicttitle3', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['dicttitle4', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle5', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle6', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle7', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle8', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['dicttitle9', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['dicttitle10', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle11', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle12', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk']]
        for i in range(0, len(ret)):
            ret[i] = tuple(ret[i])
        
        return tuple(ret)
    
    def WebSearcher(self):
        ret = []
        #sdb.reqSUB(keyword)
        #subNum = sdb.recvSUBNum()
        #for i in range(0, subNum):
        #    ret.append(sdb.recvSUB())
        #ret = [['title', 'good english', '�� �ױ۸���'.encode('utf-8')], ['title2', 'good english2', '�� �ױ۸���2'.encode('utf-8')], ['title3', 'good english3', '�� �ױ۸���3'.encode('utf-8')], ['title4', 'good english4', '�� �ױ۸���4'.encode('utf-8')], ['title5', 'good english5', '�� �ױ۸���5'.encode('utf-8')], ['title6', 'good english6', '�� �ױ۸���6'.encode('utf-8')], ['title7', 'good english7', '�� �ױ۸���7'.encode('utf-8')], ['title8', 'good english8', '�� �ױ۸���8'.encode('utf-8')], ['title9', 'good english9', '�� �ױ۸���9'.encode('utf-8')], ['title10', 'good english10', '�� �ױ۸���10'.encode('utf-8')]]
        ret = [['webtitle1', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle2', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle3', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle4', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle5', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle6', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle7', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle8', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle9', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle10', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle11', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle12', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk']]
        
        for i in range(0, len(ret)):
            ret[i] = tuple(ret[i])
        
        return tuple(ret)

    def AllSearcher(self):
        ret = []
        #sdb.reqSUB(keyword)
        #subNum = sdb.recvSUBNum()
        #for i in range(0, subNum):
        #    ret.append(sdb.recvSUB())
        #ret = [['title', 'good english', '�� �ױ۸���'.encode('utf-8')], ['title2', 'good english2', '�� �ױ۸���2'.encode('utf-8')], ['title3', 'good english3', '�� �ױ۸���3'.encode('utf-8')], ['title4', 'good english4', '�� �ױ۸���4'.encode('utf-8')], ['title5', 'good english5', '�� �ױ۸���5'.encode('utf-8')], ['title6', 'good english6', '�� �ױ۸���6'.encode('utf-8')], ['title7', 'good english7', '�� �ױ۸���7'.encode('utf-8')], ['title8', 'good english8', '�� �ױ۸���8'.encode('utf-8')], ['title9', 'good english9', '�� �ױ۸���9'.encode('utf-8')], ['title10', 'good english10', '�� �ױ۸���10'.encode('utf-8')]]
        ret = [["Downton.Abbey.S04E01.720p.HDTV.x264-FoV", "Was there really no warning?", '��ҿ� �ٸ� ���� ������?'], 
               ['Downton.Abbey.S04E01.720p.HDTV.x264-FoV', "We don't have a choice.", '�츮�� ���ñ��� ����'], 
               ['Dexter.S0E05', 'think this is our guy\'s work?', '�̰͵� �� �ڽ� ���ΰ� ����?'], 
               ['dicttitle1', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['dicttitle2', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['dicttitle3', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle1', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'],
               ['webtitle2', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk'], 
               ['webtitle3', 'http://url.co.kr', 'text blablalaiealjffjk dfjkjek;jrfijfikaekjbnrfjkbvhbveuiaeorjopMdfmnrmgnrjhihIEr94uet4jkafjkc;kwleofihaDkjfk']]
               
        for i in range(0, len(ret)):
            ret[i] = tuple(ret[i])
        
        
        return tuple(ret)

#class DictSearcher(keyword):
#    def __init__(self, keyword):
#        self.keyword = keyword
    
#    def __MakeResultFormat(self, searcher):
#        #"�˻� ��� �ۼ�"
#        ret = []
#        sdb.reqSUB(keyword)
#        subNum = sdb.recvSUBNum()
#        for i in range(0, subNum):
#            ret.append(sdb.recvSUB())
        
#        return tuple(ret)

#class WebSearcher(keyword):
#    def __init__(self, keyword):
#        self.keyword = keyword
    
#    def __MakeResultFormat(self, searcher):
#        #"�˻� ��� �ۼ�"
#        ret = []
#        sdb.reqSUB(keyword)
#        subNum = sdb.recvSUBNum()
#        for i in range(0, subNum):
#            ret.append(sdb.recvSUB())
        
#        return tuple(ret)
        

        


if __name__ == '__main__':
    print ("start SubSearcher.py... ")
