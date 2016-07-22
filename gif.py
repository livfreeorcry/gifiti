from urllib import quote
import re
import requests

def gif(term, unsafe=False, index=0, vote=False):
    term = quote(term)
    safe = "&safe=" if unsafe else "&safe=active"
    uri = "https://www.google.ca/search?tbm=isch&tbs=itp:animated&q=site:imgur.com+{0}{1}".format(term, safe)
    agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Versio  n/4.0.5 Mobile/8A293 Safari/6531.22.7"
    result = requests.get(uri, headers={"User-agent": agent}).text
    gifs = re.findall(r'imgurl.*?(http.*?)\\', result)
    if not gifs:
        return ""
    elif vote:
        return gifs[:5]
    else:
        return gifs[0]