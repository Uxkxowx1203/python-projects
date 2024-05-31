from datetime import date
try:
    year1 = int(input("DATE1 YEAR(YYYY): "))
    month1 = int(input("DATE1 MONTH (MM): "))
    day1 = int(input("DATE1 DAY(DD): "))
    date1 = date(year1, month1, day1)

    year2 = int(input("DATE2 YEAR(YYYY): "))
    month2 = int(input("DATE2 MONTH (MM): "))
    day2 = int(input("DATE3 DAY(DD): "))
    date2 = date(year2, month2, day2)

except ValueError:
    print("INVALID FORMAT")
d= date2 - date1
print(f"DIFFERENCE: {d.days} DAYS")