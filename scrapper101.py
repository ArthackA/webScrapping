from bs4 import BeautifulSoup
import requests

url = "https://www.brightermonday.co.ke/jobs/"
response = requests.get(url)


data = response.text


soup = BeautifulSoup(data,'html.parser')

titles = soup.find_all('a',{'class':'search-result__job-title metrics-apply-now'})

for title in titles:
    print(title.text)
