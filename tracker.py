import requests
import bs4
from twilio.rest import Client
import time

#search my user agent in google and replace the useragent values below with yours.
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

url="Replace this with your product URL"

TrackingPrice=enter the threshhold price
count=0

res = requests.get(url,headers=HEADERS)
soup = bs4.BeautifulSoup(res.content, features='lxml')

#get the below 2 values from the twilio website settings page and check under the Live credentials tab
accountSid = "xxxxxxxxxxxxxxxxxxxxxx" 
authToken = "xxxxxxxxxxxxxxxxxxxxxxxx"  

client = Client(accountSid, authToken) 
myTwilioNumber = "number sholud be of the form +91123456789" #this number should be the bought twilio number. It is free
destCellPhone = "number should be of the form +91123456789"

while True:

  # to prevent script from crashing when there isn't a price for the product
  try:
    title = soup.find("span",{"class":"_35KyD6"}).get_text().strip()

    amount = float(soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).get_text().replace("₹","").replace(",","").strip())
    if amount<=TrackingPrice:
      msg="You got a offer on the {0} for {1}. Check out the product {2}".format(title,amount,url)
      myMessage = client.messages.create(body = msg, from_=myTwilioNumber, to=destCellPhone) 
      count+=1
      if count==5:
        TrackingPrice=amount-1
        count=0

  except:
    msg="Couldn't get details about product"
    myMessage = client.messages.create(body = msg, from_=myTwilioNumber, to=destCellPhone)
    
 #change the value to set the time for it to check everytime 
  time.sleep(30)
