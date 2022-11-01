import calendar

try:
    year = int(input("Enter the year: "))
    if calendar.isleap(year):
        print(year, "is a leap year")
    else:
        print(year, "is a non-leap year")
except ValueError:
    print("The year entered is incorrect")
except KeyboardInterrupt:
    print("\nDo not press ctrl + c")
except:
    print("An unknown error has occurred") 
