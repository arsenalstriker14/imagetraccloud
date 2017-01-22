from django.test import TestCase

# Create your tests here.
def getCurrMonth(date):
        date = str(date)
        y = str(date[2:4])
        m = str(date[5:7])
        d = str(date[-2:])
        return m,y

datelist = getCurrMonth(date)
cmonth = datelist[0]
if cmonth == '12':
    nmonth = '01'
else:
    nmonth = str(int(cmonth) + 1)
if len(nmonth) == 1:
    nmonth = "0" + nmonth

if cmonth == '01':
    lmonth = '12'
else:
    lmonth = str(int(cmonth) - 1)
if len(nmonth) == 1:
    lmonth = "0" + lmonth



cyear = datelist[1]
