from selenium import webdriver
import pandas as pd
import csv
import os
import numpy
PATH = "C:\\Users\\Lenovo\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=PATH,options=options)
a=[]
b=[]
driver.get("https://www.nirfindia.org/2022/UniversityRanking.html")
pdf_link = driver.find_elements_by_xpath('//*[@id="tbl_overall"]/tbody/tr/td[2]/div[1]/a[3]')
for i in range(len(pdf_link)):
    pdf_link = driver.find_element_by_xpath('//*[@id="tbl_overall"]/tbody/tr['+str(i+1)+']/td[2]/div[1]/a[3]')
    sentence = driver.find_element_by_xpath('//*[@id="tbl_overall"]/tbody/tr['+str(i+1)+']/td[2]').get_attribute('textContent')
    Institute_name=Institute_name.replace('More','')
    pdf_url = pdf_link.get_attribute("href")
    temp_du={
        'Links': pdf_url,
        'Institute Name':Institute_name,
    }
    a.append(temp_du)
    df=pd.DataFrame(a)
    df.to_csv('Links.csv')  
    # print(a)
df = pd.DataFrame(a)
data=df.to_csv(r'C:\Users\Lenovo\Desktop\College\Minor Project\NIRF\SELENIUM\links.csv')
