days = int(input("Enter the number of days: "))

year = days // 365
month = (days%365)//30
week = ((days%365)%30)//7

print("Number of years", year)
print("Number of months", month)
print("Number of weeks", week)
