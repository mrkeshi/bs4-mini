import requests
from bs4 import BeautifulSoup
x=1
f=open("alireza.txt","w+",encoding="utf-8")
for x in range(1,100):
    page=requests.get("***.blogfa.com/?p="+str(x))
    soup=BeautifulSoup(page.text,"html.parser")
    result=soup.select('.post')
    for re in result:
        if("علیرضا" in re.text):
            print("ok")
            save=re.find("a",class_="text-my-1")
            f.write("+\n"+save['href'])
