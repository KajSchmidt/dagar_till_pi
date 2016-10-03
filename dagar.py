
from datetime import date, datetime



idag = date.today()



def dagar_till(datum):
	nu = date(idag.year,idag.month,idag.day)
	sen = datetime.strptime(datum, '%Y-%m-%d').date()
	dagar = sen - nu
	return dagar.days;


def dagar_till_pi():
	nu = date(idag.year,idag.month,idag.day)
	sen = date(2017, 3, 14)
	dagar = sen - nu
	return dagar.days;


def dagar_till_jul():
	nu = date(idag.year, idag.month, idag.day)
	sen = date(idag.year, 12, 24)
	dagar = sen - nu
	if dagar.days < 0:
			sen = date(idag.year+1, 12, 24)
			dagar = sen - nu
	return dagar.days;
