import os
import requests

files = os.listdir()

q = [i for i in files if i.endswith('.js')]
for i in q:
    open('bundle.min.js',
         'a').write("\n /* COMPILED FROM " + i + " */" + open(i).read())

import requests

url = 'https://www.toptal.com/developers/javascript-minifier/raw'
data = {'input': open('bundle.min.js', 'rb').read()}
response = requests.post(url, data=data)

open("bundle.min.js", 'w').write(response.text)
