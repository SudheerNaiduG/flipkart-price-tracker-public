# flipkart-price-tracker-public

Deploy this in heroku and the python script will check every 30 secs for the price and will update you if the price is less than the price which you set.
You can edit the number of messages and the time for which it has to check everytime according to you convinience.

## Note

You can also use this code for any other website you want to track the price for.
But you have to make some changes in the code since the class variables change for every website.
So this particular code works only for flipkart.


## Twilio

This script uses [**Twilio**](http://twilio.com/) services to send a message to your phone number to update you about the price.

Sign up for a free twilio account from [http://twilio.com](http://twilio.com/). You will be assigned with an account sid and auth token. You may also have to verify the mobile number to which you will send the message. Once this is successful, you will also get a sender twilio mobile number that can be used in your code.You have to install twilio module if you want to make it from scratch . Install twilio by this command `pip3 install twilio` . Ignore this if you are directly deploying this in heroku.

## Heroku

If you dont know how to fork a repo just hit the fork option on the top of the page or you can google how to fork a repo.

Fork this repo and Deploy the app in [heroku](http://heroku.com/deploy). You can also run only the script in your terminal or colab but you have to keep it running all the time. So its better to deploy it in heroku and then forget about it.

Deploying is an easy process.After selecting deploy, selcect the country US or Europe and follow further instructions. Connect your github account and select the forked repo and thats it.


## Process

Edit the code according to your requirements i.e **set the sender and reciever phone number and auth token and sid** which will be provided in the project **settings** in the twilio website  and also declare the URl of the product you want to track. 

**Buy** a twilio number for free from the dashboard itself and use the **Live credentials** in the **settings** to get auth token and sid for the message to be sent.

Set the **trackingPrice** in line 13 to your required threshold price.

**Replace** the url in **line 11** with the url of your product.

**Replace** the `myTwilionumber` in line 21 and `destnumber` in line 22 with your phone number and the destination phone number i.e the number to which you want to get the updates about the product respectively.

**Deploy** the forked repo in Heroku.

**Thats it** now the script will check the price of your product for every 30 secs (you can change this by changing the time in **line 43**) and will send a message if the price fall below or equal to the **TrackingPrice**.









