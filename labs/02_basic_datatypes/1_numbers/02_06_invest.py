'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
monthlyInterestRate = (annualInterestRate) / 10 / 12
numberOfYears = eval(input("Enter number of years: "))
numberOfMonths = numberOfYears * 12

futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) **\
                 numberOfMonths
print("The future value of your investment is", futureInvestmentValue)