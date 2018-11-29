#eul19.py

#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?




#7th day = 1st Sunday
#1st days of months are numerically:
#1 (first of Jan)
#32 (first of Feb)
#60/61 (First of March)
#91/92 (first of April)
#121/122 (first of May)
#152/153 (first of June)
#182/183 (first of July)
#213/214 (first of August)
#244/245 (first of September)
#274/275 (first of October)
#305/306 (first of November)
#335/336 (first of December)



def first_days_list(year):	#gives list of days in year that are first days of month
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):	#defines leap year
		leap_year = 1
		first_days = [1,32,61,92,122,153,183,214,245,275,306,336]	#leap year list

	else:
		leap_year = 0
		first_days = [1,32,60,91,121,152,182,213,244,274,305,335]	#non-leap year list

	return(leap_year,first_days)

def sundays_in_year(year,offset):

	sundays_number = 0 #initializing


	#uses above function on year
	(leap_year,first_days) = first_days_list(year)


	for i in range(1,365+leap_year+1):

		if (i-offset+6)%7 == 0 and i in first_days: 	#checks if i is a sunday and first day of a month, adds one to sundays_number if it is

			sundays_number = sundays_number + 1

	return sundays_number 

			


def main():

	year = 1901
	offset = 1	 #(represents starting on Tuesday)
	sundays = 0

	while year <= 2000:

		
		sundays = sundays + sundays_in_year(year,offset)	#adds number of relevant sundays
		(leap_year,first_days) = first_days_list(year)		#uses previous function to find if a year is a leap year or not
		offset = offset + (365 + leap_year) % 7			#calculates new offset for start of next year
		year = year + 1						#increments year counter

	print(sundays)






