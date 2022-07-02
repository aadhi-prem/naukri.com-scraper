#scraper for naukri.com

import requests
import pprint


url= "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=pyhton&location=bangalore%2Fbengaluru&pageNo=1&k=pyhton&l=bangalore%2Fbengaluru&seoKey=pyhton-jobs-in-bangalore-bengaluru&src=jobsearchDesk&latLong="

headers={"appid" : "109","systemid" : "109"}
r = requests.get(url,headers=headers)
data = r.json()

pprint.pprint(data)

