# europarliament

## UPDATE 
The script is now a Flask web app, the page for which is accessible here: http://eu-traineeships.herokuapp.com/ 
The page may take a while to load on the first visit.

## What it does
Script scraping the [gestmax.eu](ep-stages.gestmax.eu) website listing available traineeships at the European parliament and the number of candidates.
Once every six months, the European parliament opens trainees selections for around 400 places. Many thousands of people apply each time, but the number of applicants varies widely between vacancies.
This script scrapes the gestmax website and creates an .ods file (readable through spreadsheet software such as LibreOffice Calc and Excel) with three columns: Title of the traineeship offer, Number of candidates, Link to the offer. The .ods file is created from a pandas dataframe object, which can also be converted to other formats or used as such.

The number of candidates isn't completely accurate since this number changes on the gestmax website from the overview of all offers and the single offer's page.

## Dependencies
Modules to install:
* [pandas](https://pandas.pydata.org/) to create a dataframe object containing all the data, giving me the possibility to further expand the script's functionalities in the future
* [odfpy](https://pypi.org/project/odfpy/) to export the data to an .ods file using the [Dataframe.to_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html) pandas method 
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](https://requests.readthedocs.io/en/master/) for scraping the newsletters' pages and getting the latest issue
