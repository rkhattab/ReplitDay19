print("--Loan Calculator--")
#loan of $1000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.
loan = 1000
apr = float(0.05)
year = 0
print()

for i in range(10):
  loan += (loan*apr)
  year += 1
  print("In Year", year, "you will owe $", round(loan, 2),".")
