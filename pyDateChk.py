#!/usr/bin/python3

import datetime
from datetime import date

###################################################
# read from file of dates/description
# and determine how many days until that day
###################################################
def check_upcoming():
    date_file = open("../apptfile.txt",'r')
    x = datetime.datetime.now()
    print(x.strftime("%m"))
    print("today: %s %s %s" % (x.month,x.day,x.year))
    to_date=date(x.year,x.month,x.day)

    for line in date_file:
        desc_data = ' '.join(line.split()[1:])
        line_date=line.split()[0]
        curr_date=line_date
        #print("to date: ")
        #print(to_date)
        from_year = curr_date[-4:]
        from_month = curr_date[:2]
        from_day =  curr_date[2:4]
        print("Currently reading:  year month day: %s %s %s %s" % (from_year,from_month,from_day,desc_data))
        from_date = date(int(from_year),int(from_month), int(from_day))
        delta = to_date - from_date
        print("NUMBER OF DAYS UNTIL %s: %d " % (desc_data,abs(delta.days)) )



###################################################
# append to  file apptfile.txt dates/description
# in format:
# MMDDYYYY <description>
###################################################
def make_entry():
    date_file = open("../apptfile.txt",'a')
    #print('{:%Y-%m-%d %H:%M}'.format(datetime(2019,8,22,8,12)))
    x = datetime.datetime.now()
    print("today: %s %s %s" % (x.month,x.day,x.year))
    month = input("Enter month (1-12): ")
    if int(month) < 10:
        month = "0" + month
    day = input("Enter Day (1-31): ")
    if int(day) < 10:
        day = "0" + day
    year = input("Enter year: ")
    print("you entered: %s %s %s " % (month,day,year))
    newappt = month + day + year
    desc = input("Enter description of appt: ")
    print(newappt)
    date_file.write(newappt)
    date_file.write(' ')
    date_file.write(desc)
    date_file.write("\n")

def main():
    make_entry()
    check_upcoming()

if __name__=='__main__':
    main()
