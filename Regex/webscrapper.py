import re
import urllib.request as scrapper
urls = ['www.google.com', 'projexai.tech']
for url in urls:
    print('Searching for ', url)
    response = scrapper.urlopen('https://'+url)
    text = response.read()
    title = re.sub(r'</*title>', '', str(re.findall(r'<title>.*</title>', str(text), re.I)))
    print(title)