import requests
import os
import re
from glob import glob

root='www.desmos.com'
website='https://desmos.com/'
urls=['calculator','assets/img/touch-icon-192x192.png','favicon.ico']

js_pattern=r'/assets/build/calculator_desktop-(.*).js'
css_pattern=r'/assets/build/calculator_desktop-(.*).css'

#Update files

def write_to_file(text,file):
    with open(file,'wb') as f:
        f.write(text)

def download(urls):
    for url in urls:
        os.makedirs((root+'/'+url).rpartition('/')[0],exist_ok=True)
        print('Capturing '+website+url)
        write_to_file(requests.get(website+url).content,root+'/'+url)

download(urls)



with open(root+'/calculator','r') as f:
    html=f.read()

js_url=re.search(js_pattern,html).group(0)
html=re.sub(js_pattern,js_pattern.replace('-(.*)',''),html)

css_url=re.search(css_pattern,html).group(0)
html=re.sub(css_pattern,css_pattern.replace('-(.*)',''),html)

urls=[js_url,css_url]
download(urls)

write_to_file(html.encode('utf-8'),root+'/calculator')

#Move calculator to calculator.html
os.rename(root+'/calculator',root+'/index.html')
try:
    os.rename(glob(root+js_pattern.replace('(.','').replace(')',''))[0],root+js_pattern.replace('-(.*)',''))
    os.rename(glob(root+css_pattern.replace('(.','').replace(')',''))[0],root+css_pattern.replace('-(.*)',''))
except:
    pass

# with open(root+js_pattern.replace('-(.*)','')) as f:
#     js_file=f.read()

# js_file=js_file.split('\n')
# for i in range(len(js_file)):
#     if js_file[i].startswith("define('text!example_graphs'"):
#         del js_file[i]
#         break

# with open(root+js_pattern.replace('-(.*)',''),'w') as f:
#     f.write('\n'.join(js_file))