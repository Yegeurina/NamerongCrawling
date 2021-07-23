import requests
from requests import exceptions
from urllib import request
from requests.models import HTTPError
from bs4 import BeautifulSoup
import re
import os

def getDownload(accessUrl,fileName,path) :
    try :
        os.chdir(path)
        request.urlretrieve(accessUrl,fileName)
        print("다운로드 완료")
    except HTTPError as e :
        print("Error")
        return

def DownFile(Tag) :
    url = 'http://www.digitalforensics.or.kr'
    link = Tag.get('href')
    if(len(link)>1) :
        print(len(link))
        accessUrl = url+link
        print(accessUrl)
        fileNAME = re.sub('<.+?>', '', str(Tag), 0)
        path = "F:\\BoB10th\\트랙교육\\유현 멘토님\\나메롱 웹크롤링\\IMG\\"
        if os.path.isfile(path+fileNAME) : 
            print("다운로드 실패")
        else :
            getDownload(accessUrl,fileNAME,path)
    
def URLparser():
    url = 'http://www.digitalforensics.or.kr/images/'
    res = requests.get(url)

    html = res.text
    soup = BeautifulSoup(html,'html.parser') 

    for tag in soup.select('a[href]') :
        DownFile(tag)

if __name__ == '__main__':
    URLparser()