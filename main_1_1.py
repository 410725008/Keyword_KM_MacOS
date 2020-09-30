import os 
import requests
from datetime import datetime , date
from datetime import timedelta
from bs4 import BeautifulSoup

searchDays = 7
searchPages = 1
today = date.today() - timedelta(days = searchDays)
dirpath = os.path.join(os.path.expanduser("~"),"Desktop") + "/Keyword_KM"
if not os.path.isdir(dirpath):
    os.mkdir(dirpath)
output_file_path = dirpath + "/Output.txt"
keyword_file_path = dirpath + "/Keyword.txt"
output = open(output_file_path,'w')
if not os.path.isfile(keyword_file_path):
    mkKeyword = open(keyword_file_path,'w')
    mkKeyword.write('//可以使用以下參數控制搜尋項目 -排除關鍵字 @搜尋社群媒體 sites=(搜尋網域)\n')
    mkKeyword.write('//例『拉麵-九湯屋@Twitter sites=twitter.com』會搜尋twitter上拉麵但不包含九湯屋的內容\n')
    mkKeyword.write('搜尋幾天內的內容：1\n')
    mkKeyword.write('搜尋頁數：1\n')
    mkKeyword.close()
keyword = open(keyword_file_path,'r')

'''
def image_path(n):
    return ".\\img\\"+str(n)
if not os.path.isdir('img'):
    os.mkdir('img')'''

def google(key_word):
    for Pagei in range(searchPages):
        print("正在搜尋：" + key_word + " 的第"+str(Pagei+1)+"頁內容......")
        output.write("＝＊＝＊＝＊＝＊＝＊＝＊＝＊＝＊以下為 "+key_word+ " 的第"+str(Pagei+1)+"頁內容＊＝＊＝＊＝＊＝＊＝＊＝＊＝＊＝\n\n")
        web = requests.get("https://www.google.com/search?q=" + key_word + " after:" + str(today)+"&start="+str((Pagei)*10))
        soup = BeautifulSoup(web.text,"lxml")
        get = soup.find_all("div",class_="kCrYT")    
        for i in get:
            if i.find("h3") != None:
                try:
                    output.write(i.div.string)
                    output.write("\n")
                except:
                    pass
                data = str(i)
                try:
                    url = data[data.find('href="/url?q=')+13:data.find('&amp')]
                    output.write(url)
                    output.write("\n\n")
                except:
                    pass
    output.write("\n")


line = keyword.readline()
while line:
    if line[0:8] == '搜尋幾天內的內容':
        searchDays = int(line[9:])
        today = date.today() - timedelta(days = searchDays)
        print("搜尋來自"+str(today)+"之後的內容！")
        output.write("搜尋來自"+str(today)+"之後的內容！\n")
        line = keyword.readline()
        continue
    if line[0:4] == '搜尋頁數':
        searchPages = int(line[5:])
        print("搜尋"+str(searchPages)+"頁的內容！")
        output.write("搜尋"+str(searchPages)+"頁的內容！\n")
        line = keyword.readline()
        continue
    if line[0:2] == '//':
        line = keyword.readline()
        continue
    google(line)
    word = line.split(" ")
    for i in range(len(word)):
        for j in range(i + 1 , len(word)):
            google(str(word[i]) + ' ' + str(word[j]))
    line = keyword.readline()

output.close()
keyword.close()
