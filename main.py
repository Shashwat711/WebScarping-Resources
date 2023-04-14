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
driver.get("https://www.guru99.com/web-scraping-tools.html")
header = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/main/div/article/div/div/h3/a')
for i in range(len(header)):
    print(len(header))
    header = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/article/div/div/h3['+str(i+1)+']/a').get_attribute('textContent')
    # /html/body/div[1]/div/div/div/main/div/article/div/div/p[4]
    # 4,9,14,19
    # content = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/article/div/div/p['+str(i+1)+']').get_attribute('textContent')

    temp_du={
        'Names': header   
    }
    a.append(temp_du)
    df=pd.DataFrame(a)
    df.to_csv('Links.csv')  
df = pd.DataFrame(a)
data=df.to_csv(r'links.csv')






