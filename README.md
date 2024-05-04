Deutsche Welle scraper

Project scrapes the latest reports from the Deutsche Welle news website, focusing on the top stories of the day. It extracts data including the preview image, news headline, news link, and full text reportage, and saves it into a JSON file for further analysis.

     Features
Dynamic Content Scraping: The scraper utilizes Selenium and BeautifulSoup libraries to dynamically fetch the latest reports from the Deutsche Welle website, particularly focusing on the stories in the "In Focus" section.
Data Extraction: It extracts key information such as the preview image link, news headline, news link, and full text reportage from the HTML structure of the webpage.
Handling Dynamic Content: Selenium is used to handle dynamic content loading, ensuring that all necessary information is captured accurately.
JSON Serialization: Extracted data is serialized into a JSON file format for easy storage, retrieval, and further processing.
     How to Use

To use the project, ensure you have the necessary libraries installed (BeautifulSoup, requests, Selenium). Also, make sure you have the Chrome WebDriver installed and set up correctly. 
Simply run the provided Python script. It will automatically scrape the latest reports from Deutsche Welle's website and save them into a JSON file named "latest_in_focus.json". 
You can then access the JSON file to view the collected news articles and their details.
