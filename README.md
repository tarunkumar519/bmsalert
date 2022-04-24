# BookMyShow-Booking-Alert
Alerts by sending SMS using Twilio whenever a theater opens booking on specific movie

## Requirements

Python 3 or greater
pip3

You need a Twilio account to obtain the sid and authid to send SMS. Get here https://twilio.com

## Installation

Clone repo using
```
git clone https://github.com/tarunkumar519/bmsalert.git
cd bmsalert/
```

Install dependencies using
```
pip3 install -r requirements.txt
```
## Running
```
python3 bmsalert.py
```

Run this and put it aside. Whenever tickets are available, script sends the SMS to all the numbers and exits.
By default delay is set to 30 Seconds, you can change this inside the script.

Due to the dependencies used in this script, you can easily run this on a RaspberryPi, Android, iOS(iSH) and other devices with ease.. or spin up a server.

# Support
If you like this repo , give it a star to support me for future updates.

<a href="https://www.buymeacoffee.com/ga1325117D" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## License

MIT License

Copyright (c) 2022 Tarun kumar

