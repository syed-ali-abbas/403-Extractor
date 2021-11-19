import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import numpy as np
from requests.exceptions import HTTPError
import sys

a=sys.argv[1:]
count=0
df = pd.read_csv(a[0],error_bad_lines=False)
lines=['URLS,']

for url in df['urls']:	
   try:
   	response= requests.get(url)
   	status= response.status_code
   	#df['Status']=status
   	if status == 403:
   		with open(a[1], 'a') as f:
   			for line in lines:
        			f.write(url)
        			f.write('\n')
        			count=count+1
        			print("\033[1;37;40m [ |-------------------------------------------|")
        			print("\033[1;31;40m [",count,"]")
        			print("\033[1;32;40m [ 403 Found\t\t\t\t\t\t")
        			print("\033[1;34;40m [ ",url,"\t\t\t\t\t\t\t\t")
        			print("\033[1;37;40m [ |-------------------------------------------|")
        			
        			
   except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
   except Exception as err:
        print(f'Other error occurred: {err}')     