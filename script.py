import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/nyles/Desktop/DS Project/Chrome Driver/chromedriver.exe') #this directory is for the chromedriver extension
driver.get('https://luxe.digital/lifestyle/style/luxury-watch-brands/') #choose the webpage you need to scrape from
results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser") #add feature html parser so it can grab data from webpage
driver.quit() #closes webpage after it runs

for element in soup.findAll(attrs='content'): #the attrs field is for the main() of whatever piece of information you are trying to grab
    name = element.find('li') #this is where the text or the title of the information is labeled as
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Luxury Watch Brands': results}) #find header/title for page
df.to_csv('names.csv', index=False, encoding='utf-8')
