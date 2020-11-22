import requests
from bs4 import BeautifulSoup
import pandas as pd

pages = 42 #this is hard-coded for now, but will be scraped as well in a future update
traineeships = pd.DataFrame()
offer = []
candidates = []
link_offer = []


for i in range(1, pages):
    url = "https://ep-stages.gestmax.eu/search/index/page/" + str(i)
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll("div")
    for link in links:
        title = link.get("class")
        if str(title) == "['application_count_div']":
            text1 = (str(link.text))
            text2 = text1.lstrip()
            text2 = text2.split(' ', 1)[0]
            if text2 == "Be":
                candidates.append(0)
            else:
                candidates.append(int(text2))

    links = soup.findAll("h3")  # use a instead of h3 for links
    for link in links:
        if str(link.get("class")) == "['list-group-item-heading']":
            url_stage = str(link.text)
            offer.append(url_stage)


    links = soup.findAll("a")  # use a instead of h3 for links
    for link in links:
        if str(link.get("class")).startswith("['list-group-item"):
            link_offer.append(link.get("href"))



traineeships['offer'] = offer
traineeships['candidates'] = candidates
traineeships['link_offer'] = link_offer

traineeships.to_excel('traineeships.ods', index=False, encoding='UTF-8')
