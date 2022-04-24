import os
from twilio.rest import Client
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import time
i = 0
while i==0:
    site= "https://in.bookmyshow.com/buytickets/doctor-strange-in-the-multiverse-of-madness-hyderabad/movie-hyd-ET00326386-MT/20220506" #Replace this wiht your url after you click on book tickets button
    date="20220506" #replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
    site=site+date
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    venue ='AMBH' #this can be found by inspecting the element data-id for the venue where you would like to watch for ex here it is data-venue-code="AMBH"
    show='08:00 PM' #just replace it with your prefered show timing
    delay=30 #timegap in seconds between 2 script runs
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    soup2=soup.find_all('div', {'data-online': 'Y'})
    line = str(soup2)
    soup3= BeautifulSoup(line, "html.parser")
    soup4=soup3.find_all('a', {'data-venue-code': venue})
    line1=str(soup4)
    soup5=BeautifulSoup(line1, "html.parser")
    result=re.findall('data-availability="A"',line1) #This script mainly focuses on venue availability, means whenever bookings in a theater opens-you get alert
    if len(result)>0:
    #Twilio code to send SMS starts here
        account_sid = os.environ['TWILIO_ACCOUNT_SID']='PASTE_YOUR_SID_HERE'
        auth_token = os.environ['TWILIO_AUTH_TOKEN']='PASTE_AUTH_TOKEN_HERE'
        client = Client(account_sid, auth_token)
        numbers_to_message = ['+91XXXXXXXXXX', '+9XXXXXXXXXX'] #multiple numbers can be placed this way
        for number in numbers_to_message:
            message = client.messages.create(  
                                messaging_service_sid='TWILIO_MESSAGESERVICEID_FOUND_ON_TWILIO_CONSOLE', 
                                body='Dr.Strange Tickets available now on AMB.Book here https://in.bookmyshow.com/buytickets/amb-cinemas-gachibowli/cinema-hyd-AMBH-MT/20220424',  #you can replace your own sms message here    
                                to=number #sends to each number in numbers_to_message array
                            ) 

        print(message.sid) #prints sid to screen
        i=1

    else :
        time.sleep(delay) #based on pre-set delay in seconds above.Here it's 30 seconds
