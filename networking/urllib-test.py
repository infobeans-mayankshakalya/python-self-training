import urllib.error
import urllib.request

try:
    url = urllib.request.urlopen('https://www.python.org')
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print('URL not accessible.')

f = open('python.html', 'wb')
f.write(content)
f.close()