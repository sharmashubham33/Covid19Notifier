### COVID-19 DESKTOP NOTIFIER

from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {"User-Agent":"Mozilla"}
req = Request('https://www.worldometers.info/coronavirus/country/india/' , headers = header)
html = urlopen(req)


obj = bs(html,features="html5lib")

new_cases = obj.find('li' , {"class":"news_li"}).strong.text.split()[0]

new_deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
             

### NOTIFIER

notifier = ToastNotifier()

message = "NEW CASES = "+ new_cases + "\nNEW DEATHS = "+ new_deaths

notifier.show_toast(title="COVID-19 DAILY NOTIFIER",msg=message,duration=10,icon_path=r"virus.ico")