# coding: utf-8

import requests
import bs4
import random


def findchain(fisrt_spell, _entry=0):
    sess = requests.Session()

    url = "http://m.krdic.naver.com/search/entry/"

    entry = str(_entry)+"/"
    
    param = fisrt_spell

    response = sess.get(url+entry+param+"*")

    response.text

    text = response.text

    bs = bs4.BeautifulSoup(text,'html.parser')

    finds = bs.find_all("a", attrs={'class':'ft'})

    fin = finds[0]

    fin.contents

    gin = finds[0].find("strong")

    gin.contents

    ret = []
    
    for f in finds:
        word = (f.find("strong").contents[0]+f.contents[1])
        if ' ' in word:
            word = word[0:word.find(' ')]
            
        if word not in ret:
            ret.append(word)
            
    return ret


records = list()

fail=False

first = input("시작하세요 \n")

answers = findchain(first)

ans = answers[random.randint(0,len(answers)-1)]


print(ans)

while ans not in records:
    records.append(ans)
    first = input("당신의 단어 :")
    while len(first) == 1:
        first = input("당신의 단어 :")
    answers = findchain(first[-1])
    ans = answers[random.randint(0,len(answers)-1)]
    print(ans)

