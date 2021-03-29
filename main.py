import requests
import xmltodict
import json
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/udemyfreebies/new/.rss'
ua = 'Mozilla/5.0 Gecko Firefox' # Generic user agent

headers = {
    'User-Agent': ua
}

response = requests.get(url, headers)
response = response.decode('utf-8') # Convert byte response to string

content = xmltodict.parse(response.content) # Convert XML response to dict format
posts = content['feed']['entry'] # Extract all Reddit posts from the response

# List of keywords to monitor post titles for
keywords = ['python', 'django', 'flask', 'linux', 'kali', 'hack', 'pen']


# Iterate through posts; check if any of the keywords are in the post title. Print post title and links
for entry in posts['feed']['entry']:
	for kw in keywords:
		if kw in entry['title'].lower():
			print(entry['title'])
			print(entry['link']['@href'])
			html = entry['content']['#text']
			S = BeautifulSoup(html)
			print(S.find_all('a')[2]['href'])
			print()
			pass