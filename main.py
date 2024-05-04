from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import json


driver_path = binary_path
service = Service(driver_path)
service.start()
driver = webdriver.Chrome(service=service)
headers_browser = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
link = 'https://www.dw.com/en'

data = []

response = requests.get(link, headers=headers_browser).text
soup = BeautifulSoup(response, 'lxml')
news_focus = soup.find(class_='focus-menu')
links = news_focus.find_all('a')

for items in links:
    href = items.get('href').replace('/en', '')
    driver.get(link + href)
    response_item = driver.page_source
    soup_item = BeautifulSoup(response_item, 'lxml')
    reports_items = soup_item.find_all(class_='teaser-wrap')

    for reports in reports_items:
        item_data = {}

        image_link = reports.find(class_='teaser-image-wrap').find('img')['src'].strip().replace('_600', '_602')
        if len(image_link) > 10:
            item_data['image_prev'] = image_link

        news_title_prep = reports.find(class_='title-above-md')
        if news_title_prep is not None:
            news_title = news_title_prep.text.strip()
            item_data['news_title'] = news_title

            news_link_prep = news_title_prep.a.get('href')
            news_link = link + news_link_prep.replace('/en', '')
            item_data['news_link'] = news_link

            news_response = requests.get(news_link, headers=headers_browser).text
            news_soup = BeautifulSoup(news_response, 'lxml')
            news_body = news_soup.find(class_='rich-text').text.strip()
            if len(news_body) < 10:
                news_body = news_soup.find(class_='teaser-text').text.strip()
            item_data['news_body'] = news_body

        data.append(item_data)

driver.quit()

with open('latest_in_focus.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
