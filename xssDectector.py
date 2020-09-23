from bs4 import beautifulsoap
from urllib.request import Request, urlopen, ConnectionError
import sys
from time import sleep

def xssfind(url):
    req = Request(url)
    query = req + "?query="
    html = url.read().decode('UTF-8')
    bs = beautifulsoap(html)

    count = 0
    with open("xss.txt",'r',encoding='UTF-8') as file:
        f = file.readlines()
        try:
            while count < len(f):
                res = urlopen(query)
                sleep(random.randint(1,3))
                count += 1
                if count == len(a):
                    url.close()
        except ConnectionError:
            print("Injection success!!")
            print("url = " + url + f[count-1])
            sleep(10)




inputurl = input("input the website")
xssfind(inputurl)