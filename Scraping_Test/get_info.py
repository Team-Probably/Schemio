from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import csv
import bs4 , requests  , re
from Scraper import *
import pprint

all_depart = ['Revenue Department', 'Rural Development and Panchayat Raj Department', 'Labour Department', 'Water Resources Department', 'Industries Department', 'Forest Department', 'Department of Registration & Stamps (IGR)', 'Department of Co-Operation Marketing and Textiles', 'Law and Judiciary Department', 'Home Department', 'Transport Department', 'Industries Department', 'Municipal Corporation of Greater Mumbai', 'Housing Department - MHADA', 'Housing Department - Mumbai Building Repairs and Reconstruction Board', 'Housing Department - Slum Rehabilitation Authority', 'Maharashtra Jeevan Pradhikaran', 'Urban Development', 'Maharashtra Pollution Control Board', 'Maharashtra Industrial Development Corporation', 'Nagpur Municipal Corporation', 'Social Justice and Special Assistance Department', 'Medical Education and Drug Department - AYUSH', 'Medical Education and Drug Department - MIMH', 'Medical Education and Drug Department - DMER', 'Higher Education and Technical Department', 'Home Department- Maharashtra Maritime Board', 'Tourism and Cultural Affairs - Gazetteers Department', 'Tourism and Cultural Affairs - Directorate of Archives', 'Energy - Maharashtra State Electricity Distribution co Ltd', 'Women And Child Development department', 'Public Health Department', 'Tribal Development Department', 'DEPARTMENT OF ANIMAL HUSBANDRY & DAIRYING', 'DEPARTMENT OF FISHERIES', 'School Education and Sports Department', 'Agriculture', 'Food & Public Distribution System (PDS)', 'Tourism and Cultural Affairs Department - Directorate of Cultural', 'Tourism and Cultural Affairs Department - MTDC', 'Tourism and Cultural Affairs Department - P L Deshpande Maharashtra Kala Academy', 'Tourism and Cultural Affairs Department - Stage Performances Scrutiny Board', 'Land Record Department', 'Energy Department', 'State Excise Department', 'Minority Development Department']
departments = {}



        

def name_link_parser(number):
	raw_link = number.replace('+','').replace('-','').replace(' ','')
	return raw_link

def get_csv(file_name):
    name_link = []
    name_lk = []
    csvfile = open('./Database/'+file_name, 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader :
        name_link.append(row)
    name_lk = name_link[1:]
    for scheme in name_lk:
        scheme[1] = name_link_parser(scheme[1])
    
    return name_lk

def open_sel(link):
    link = 'https://aaplesarkar.mahaonline.gov.in' + link
    try:
        driver.get(link)
        driver.get(link)
    except:
        print("hello")
    html = driver.page_source
    return html

def normalize_docs(text):
    text = re.sub(" +"," ",text)
    text = re.sub("\n","",text)
    text = re.sub("\r","",text)
    text = re.sub("\d\\)","",text)
    text = text.strip()
    
    return text

def parse_bs4(html):
    dict_ = {}
    soup = bs4.BeautifulSoup(html)
    
    docs = soup.select('.popup .panel-body .col-md-12')
   # print(docs)
    type_docs = {}
    for i in docs:
        doc_field_name = normalize(i.select('h3')[0].getText())
        doc_list = []
        no_of_docs = i.select('.col-xs-12')
        dict_ = {}
        for j in no_of_docs:
            doc_list.append(normalize_docs(j.getText()))
        type_docs[doc_field_name] = doc_list
        #print(doc_list)
    dict_["docs"] = type_docs
    
    return dict_
    

driver = webdriver.Firefox()
for i in all_depart:

    department = {"Name" : i}
    all_schemes = get_csv(i + ".csv")
    for sname,link in all_schemes:
        html = open_sel(link)
        
        scheme = parse_bs4(html)
        department[sname] = scheme
    print(department)

    departments[i] = department

print(departments)

