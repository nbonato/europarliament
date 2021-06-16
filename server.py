from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from apscheduler.schedulers.background import BackgroundScheduler





def reload():
	pages = 43 #this is hard-coded for now, but will be scraped as well in a future update
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


	traineeships['Posto'] = offer
	traineeships['Candidati'] = candidates
	traineeships['link'] = link_offer
	traineeships = traineeships.sort_values('Candidati', ascending=False)

	traineeships["link"] = "<a href=" + traineeships['link'].astype(str) + " target='_blank'>Candidatura</a>"
	

	#traineeships.to_excel('traineeships.ods', index=False, encoding='UTF-8')
	traineeships.to_html('templates/traineeships.html', index=False, encoding='UTF-8', render_links=True, escape=False)
reload()


sched = BackgroundScheduler(daemon=True)
sched.add_job(reload,'interval',minutes=20)
sched.start()

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')



if __name__ == '__main__':

  app.run()	
