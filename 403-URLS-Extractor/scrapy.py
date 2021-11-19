import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import numpy as np
from requests.exceptions import HTTPError
import sys

#pip3 install requests-html
#https://www.thepythoncode.com/article/extracting-email-addresses-from-web-pages-using-python




#url = input("Enter the URL:- ")
#EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


# initiate an HTTP session
#session = HTMLSession()

# get the HTTP Response
#r = session.get(url)

# for JAVA-Script driven websites
#r.html.render()


#for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
#    print(re_match.group())

#da = pd.read_csv("data.csv")
#arrayy=np.array(da.iloc[:,1:])
#for i in arrayy:
#	print(i)


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