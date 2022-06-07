pay_rate = float(input("Enter the pay rate: \n"))
hours = float(input("Enter work hours: \n"))

if hours < 40:
    gross_pay = round((pay_rate * hours), 2)
else:
    gross_pay = round((pay_rate * hours) + (0.5 * pay_rate * (hours - 40)))
print(str(gross_pay))
