initial_capital   =   float(input("Please enter the initial capital:"))
pososto_epitokiou =   float(input("Please enter the pososto epitokiou:"))
number_of_years   =   int(input("Please enter the number of years:"))
final_capital     =   initial_capital * (1 + pososto_epitokiou / 100)**(number_of_years)
print(f"The final capital is:{final_capital}")
synoliko_kerdos   =   final_capital - initial_capital
print(f"The synoliko is:{synoliko_kerdos}")
year_1            = initial_capital * (1 + pososto_epitokiou / 100)
print(f"The year 1 is:{year_1}")
year_2            = initial_capital *  (1 + pososto_epitokiou / 100) ** 2
print(f"The year 2 is:{year_2}")



