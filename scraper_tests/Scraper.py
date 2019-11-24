from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import csv
import bs4 , requests  , re

url = 'https://aaplesarkar.mahaonline.gov.in/en/'

all_depart = [] 

def add_scheme(scheme_name,scheme_url,department):
	filename = './Database/' + department + '.csv'    
	csvfile = open(filename, 'a')
	with csvfile:
		csvwriter = csv.writer(csvfile,dialect='excel')
		csvwriter.writerow([scheme_name,scheme_url])

def department_csv(department):
    fields = ['Name','Link',]
    filename = './Database/' + department + '.csv'    #to be changed

    csv.register_dialect('myDialect', delimiter='|', quoting=csv.QUOTE_NONE)
    csvfile = open(filename, 'w')

    with csvfile:
        csvwriter = csv.writer(csvfile,dialect='excel')
        csvwriter.writerow(fields)

def normalize(text):
    
    text = re.sub(" +"," ",text)
    text = re.sub("\n","",text)
    text = re.sub("\r","",text)
    text = text.strip()
    
    return text

def make_db():
    flag = 0
    c = 0
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text)
    news_item = soup.select('.news-item')
    department = "unknown"

    for i in range(len(news_item)):
        class_text = news_item[i].select('.col-md-6')
        if class_text == []:
            department = normalize(news_item[i].getText())
           
            all_depart.append(department)
            department_csv(department)
        else:
            for i in news_item[i].select('a'):

                scheme_name = normalize(i.getText())
                scheme_url = i.get('href')
                add_scheme(scheme_name,scheme_url,department)
    print (all_depart)
    return all_depart
