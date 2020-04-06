#!/usr/bin/env python
import requests

#returns stuff if url is one of the threatTypes
def test_urls(urls):
    stuff =   {
    "client": {
      "clientId":      "yourcompanyname",
      "clientVersion": "1.5.2"
    },
    "threatInfo": {
      "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING", "THREAT_TYPE_UNSPECIFIED", "POTENTIALLY_HARMFUL_APPLICATION", "UNWANTED_SOFTWARE"],
      "platformTypes":    ["ANY_PLATFORM"],
      "threatEntryTypes": ["URL"],
      "threatEntries": [
          urls
      ]
    }
  }
    url = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=APIKEY"
    r = requests.post(url, json = stuff)
    print(r.json())
    #https://developers.google.com/safe-browsing/v4/lookup-api
    #To get an api key: https://support.google.com/cloud/answer/6158862?hl=en&ref_topic=6262490
if __name__ == "__main__":
    #just a janky way of inputting x amount of urls
    num = int(input())
    urllist = []
    for i in range(num):
        url = input()
        urllist.append({"url": url})
    test_urls(urllist)