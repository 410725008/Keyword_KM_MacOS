import os 
import requests
from datetime import datetime , date
from datetime import timedelta
from bs4 import BeautifulSoup

searchDays = 7
today = date.today() - timedelta(days = searchDays)
dirpath = os.path.join(os.path.expanduser("~"),"Desktop") + "/Keyword_KM"
if not os.path.isdir(dirpath):
    os.mkdir(dirpath)
output_file_path = dirpath + "/Output.txt"
keyword_file_path = dirpath + "/Keyword.txt"
output = open(output_file_path,'w')
if not os.path.isfile(keyword_file_path):
    mkKeyword = open(keyword_file_path,'w')
    mkKeyword.write('搜尋幾天內的內容：1')
    mkKeyword.close()
keyword = open(keyword_file_path,'r')

'''
def image_path(n):
    return ".\\img\\"+str(n)
if not os.path.isdir('img'):
    os.mkdir('img')'''

def google(key_word):
    output.write(key_word)
    output.write("\n")
    web = requests.get("https://www.google.com/search?q=" + key_word + " after:" + str(today))
    soup = BeautifulSoup(web.text,"lxml")
    get = soup.find_all("div",class_="kCrYT")    
    for i in get:
        if i.find("h3") != None:
            output.write(i.div.string)
            output.write("\n")
            data = str(i)
            url = data[data.find('href="/url?q=')+13:data.find('&amp')]
            output.write(url)
            output.write("\n\n")
    output.write("\n")


line = keyword.readline()
while line:
    if line[0:8] == '搜尋幾天內的內容':
        searchDays = int(line[9:])
        today = date.today() - timedelta(days = searchDays)
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
