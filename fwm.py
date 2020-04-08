#!/usr/bin/env python
#fraudulent website matcher

import urlfinder
import urlexpander

def check_website(url):
    url = urlexpander.expand_url(url)
    fraudlist = urlfinder.find_urls()
    status = "Not in list."
    for i in fraudlist:
        if i.casefold() in url.casefold():
            status = i + " is fake news :(."
            break
    return status
if __name__ == "__main__":
    print(check_website("https://bit.ly/3a0ttC9"))
