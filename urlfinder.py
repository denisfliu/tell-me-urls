#!/usr/bin/env python
import requests
#reads text.txt and returns things if they are a url, checks for periods so there could be false positives
def find_urls():
    txt = ""
    with open('text.txt', 'r') as file:
        txt = file.read()
    wlist = txt.split()
    i = 0
    while i != len(wlist):
        num = wlist[i].find(".")
        if num == -1:
            wlist.pop(i)
            continue
        else:
            length = len(wlist[i])
            if num == length - 1:
                wlist.pop(i)
                continue 
            if (wlist[i][length - 1] == "."):
                wlist[i] = wlist[i][0:length - 1]
            i += 1           
    return wlist
#this is probably useless, checks if urls return a status code 200 and returns a new list with the ones that do
def check_url(urllist):
    rlist = []
    for i in urllist:
        if "http" not in i:
            i = "http://" + i
        if requests.get(i).status_code == 200:
            rlist.append(i)
    return rlist
if __name__ == "__main__":
    print(find_urls())
