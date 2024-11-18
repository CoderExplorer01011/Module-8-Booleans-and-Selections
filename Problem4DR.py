# David Ramirez
# 11/12/2024 


def year_anw(year):

return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
  
user_year = int(input("Type in a year: "))
print(year_anw(year))