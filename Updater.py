import requests
import os

root='./'
website='https://desmos.com/'
urls=['calculator','assets/build/calculator_desktop-7b66719f1a2452c0d8e7aa1c09f85534b2121ce2.js','assets/img/touch-icon-192x192.png','favicon.ico']

#Update files
for url in urls:
    os.makedirs((root+url).rpartition('/')[0],exist_ok=True)
    with open(root+url,'wb') as f:
        print('Capturing '+website+url)
        f.write(requests.get(website+url).content)
