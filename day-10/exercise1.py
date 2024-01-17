def is_leap(year_to_check):
    leap = False
    if year_to_check % 4 == 0:
        if year_to_check % 100 == 0:
            if year_to_check % 400 == 0:
                print("Leap Year")
                leap = True
            else:
                print("Not leap Year")
        else:
            print("Leap Year")
            leap = True
    else:
        print("Not Leap Year")
    return leap

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_getter = month_days[month - 1]

    check_leap = is_leap(year_to_check=year)
    if check_leap and month == 2:
        month_days[1] = 29
        return f"Since this year is leap, the month {month} has {days_getter} days."
    return f"The month {month} has {days_getter} days."

year_input = int(input("Year:  "))
month_input = int(input("Month:  "))
days = ''
if month_input >= 1 and month_input <= 12:
    days = days_in_month(year=year_input, month=month_input)
else:
    print("Please enter a valid digit for month [1 - 12].")
print(days)
