import requests
import sys

from myemail import sendmailall

if __name__ == "__main__":
	try:
		url= "http://182.73.225.195:1919/all-tags/"
	
		r1 = requests.get(url)
		if r1.status_code==500:
			sendmailall(0)
		else:
			sendmailall(1)
	except Exception as err:
		print err
		
    




  
