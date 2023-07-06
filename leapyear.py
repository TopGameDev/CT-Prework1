def is_leap_year(a_year):
    a_year = False
    if a_year % 4 == 0 and a_year % 100 != 0:
        a_year = True
        print(a_year)
    elif a_year % 400 == 0:
        a_year = True
        print(a_year)
    else:
        print("This is not a Leap Year! ")

is_leap_year(2024)