from datetime import date 
from datetime import timedelta

s = "https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/REPLACE WITH YOUR MOBILE NUMBER/GLUSR_MOBILE_KEY/REPLACE WITH YOUR KEY/Start_time/"

t = date.today()
day = (t.strftime("%d-"))

mon = (t.strftime("%b-"))
mon = mon.upper()

year = (t.strftime("%Y/End_Time/"))

s += day + mon + year

y = t - timedelta(days = 1)

day = (y.strftime("%d-"))

mon = (y.strftime("%b-"))
mon = mon.upper()

year = (y.strftime("%Y/"))

s += day + mon + year

print(s)