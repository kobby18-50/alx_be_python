monthly_income = int(input('Enter your monthly income: '))

monthly_expenses = int(input('Enter your total monthly expenses: '))

# monthly savings
# def calculate_monthly_savings(monthly_income, total_monthly_expenses):
#     return monthly_income - total_monthly_expenses

# monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
monthly_savings = monthly_income - monthly_expenses
print('Your monthly savings are:', monthly_savings)

# projected yearly savings

def calculate_yearly_savings(monthly_savings):
    return (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

yearly_savings = calculate_yearly_savings(monthly_savings)

print('Your yearly savings is:', yearly_savings)