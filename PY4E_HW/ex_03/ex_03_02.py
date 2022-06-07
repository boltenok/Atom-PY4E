pay_rate = input("Enter the pay rate: \n")
hours = input("Enter work hours: \n")

try:
    pay_rate_float = float(pay_rate)
    hours_float = float(hours)
except:
    print("Error, please enter a numeric input")
    quit()

if hours < 40:
    gross_pay = round((pay_rate_float * hours_float), 2)
else:
    gross_pay = round((pay_rate_float * hours_float) + (0.5 * pay_rate_float * (hours_float - 40)))
print(str(gross_pay))
