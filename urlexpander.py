#!/usr/bin/env python

import requests

#expands url
def expand_url(url):
    if "http" not in url:
        url = "http://" + url
    return requests.head(url, allow_redirects=True).url

if __name__ == "__main__":
    url = input()
    print(expand_url(url))