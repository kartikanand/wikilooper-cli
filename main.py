import requests
from bs4 import BeautifulSoup

args = input("Enter Starting wiki topic : ")
while(args != "Philosophy"):
    print(args)
    wiki_url = "http://en.wikipedia.org/wiki/"

    r = requests.get(wiki_url+args)
    if r.status_code != 200:
        print(args + "Not a valid wiki link")
        break

    data = r.text
    soup = BeautifulSoup(data)
    div = soup.find_all(id="mw-content-text")[0]

    para = None
    for child in div.children:
        if child.name == 'p':
            para = child
            break

    if para is None:
        break

    #print(para)

    bracket = 0
    next_link = None
    for tag in para.children:
        if tag.name is None and tag.string is not None:
            if '(' in tag.string.strip():
                bracket = bracket + 1
            if ')' in tag.string.strip():
                bracket = bracket - 1

        if tag.name == 'a' and bracket == 0:
            next_link = tag['href']
            break

    if next_link is not None:
        args = next_link.split("/")[-1]
    else:
        break

print(args)
