from bs4 import BeautifulSoup
import requests

url = "https://www.brightermonday.co.ke/jobs/"
job_no = 0
while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    jobs = soup.find_all('article',{'class':'search-result'})
    
    for job in jobs:
        title = job.find('a',{'class':'search-result__job-title metrics-apply-now'}).text
        #company = job.find('div',{'class': 'search-result__body'})
        #JobFunc = job.find('div',{'class': 'search-result__job-function'})
        print('Job Title: ',title)
        job_no+=1
    url_tag = soup.find('li',{'class':'page-item'})
    if url_tag.get('href'):
        url = 'https://www.brightermonday.co.ke'+ url_tag.get('href')
        print(url)
    else:
        break
    
print("Total Number Of Jobs: ",job_no)