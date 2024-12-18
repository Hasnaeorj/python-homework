
years = int(input("Enter the number of years: "))

def years_to_days(years):
    return years * 365

def years_to_weeks(years):
    return years * 52

def years_to_months(years):
    return years * 12

def years_to_hours(years):
    return years * 365 * 24

    
days = years_to_days(years)
weeks = years_to_weeks(years)
months = years_to_months(years)
hours = years_to_hours(years)
    

print(f"{days} days")
print(f"{weeks} weeks")
print(f"{months} months")
print(f"{hours} hours")

