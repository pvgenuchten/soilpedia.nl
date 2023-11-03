# Goal of the script is export an existing site to hugo markdown
# use httrack or some other tool to download the full website
# then run this script to convert the local copy to markdown
# verify that the header and footer are properly removed (by setting the split point)
# copy the markdowns into the hugo content section

import os
import requests
from lxml import etree
from io import StringIO, BytesIO
import pandoc
import urllib

r = requests.get('https://soilpedia.nl/wp-sitemap-posts-dlp_document-1.xml', headers={'User-agent': 'Mozilla/5.0'}, timeout=5)

root = etree.fromstring(r.content)

locs = root[0].xpath('url/loc')

for u in root:
    f = requests.get(u[0].text, headers={'User-agent': 'Mozilla/5.0'}, timeout=5)
    try:
      dl = str(f.content).split('dlp-document-info-buttons').pop().split('href="')[1].split('"')[0]
      
      #if dl.split('.').pop() == 'pdf':
         
         #pdf = requests.get(dl)
         #my = pandoc.read(pdf)
      urllib.request.urlretrieve(dl,'pdf/'+dl.split('/').pop())

      #else:
      #   print('no pdf',dl)
    except Exception as e:
      print(u[0].text, e)
    


print(dl)





