#! /usr/bin/python3
# period.py is a program to control and keep track of
# the ovulation and highest and least pregnancy probability.
# It allows you to find out when you'll be most fertile.
import datetime
cycleLen = datetime.timedelta(days=28)
periodLen = datetime.timedelta(days=6)
lutealPhaseLen = 14
print('When did your period start? ')
day = input('day: ')
month = input('month: ')
year = input('year: ')
# fpd = firstPeriodDate
fpd = datetime.datetime(int(year), int(month), int(day))
# lpd = lastPeriodDate
lpd = fpd + periodLen - datetime.timedelta(days=1)
# fmc = firstMediumChance of getting pregnant.
fmc = fpd + datetime.timedelta(days=9)
# lmc = lastMediumChance of getting pregnant.
lmc = fpd + datetime.timedelta(days=11)
# fhc = firstHighChance of getting pregnant.
fhc = fpd + datetime.timedelta(days=12)
# lmc = lastHighChance of getting pregnant.
lhc = fpd + datetime.timedelta(days=13)
# od = ovulationDate
od = fpd + datetime.timedelta(days=14)
# npd = nextPeriodDate
npd = fpd + datetime.timedelta(days=28)
print()
print('Medium chance of getting pregnant from ' + str(fmc.date()) + ' to ' + str(lmc.date()))
print('High chance of getting pregnant from ' + str(fhc.date()) + ' to ' + str(lhc.date()))
print('Your Ovulation Date: ' + str(od.date()))
print('Your next period comes on: ' + str(npd.date()))
