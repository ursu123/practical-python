# mortgage.py
#
# Exercise 1.7

total_paid = 0.0
mortgage = 500000.0
interest_rate = 0.05 # 5% percent
monthly_payment = 2684.11

while mortgage > 0:
    mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
    total_paid += monthly_payment

print("Total paid", round(total_paid, 1))

# Exercise 1.8
# Suppose Dave pays an extra $1000/month for the first 12 months of the
# mortgage?

# Modify the program to incorporate this extra payment and have it print the
# total amount paid along with the number of months required.
#
# When you run the new program, it should report a total
# payment of 929,965.62 over 342 months.

total_paid = 0.0
mortgage = 500000.0
extra_payment = 1000.0
extra_payments_months = 12

while mortgage > 0:
    if extra_payments_months > 0:
        mortgage = mortgage * (1 + interest_rate / 12) - \
                    (monthly_payment + extra_payment)
        total_paid += monthly_payment + extra_payment
        extra_payments_months -= 1
    else:
        mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
        total_paid += monthly_payment

print("Total paid with 12 extra payments", round(total_paid, 2))

# Exercise 1.9

# Modify the program so that extra payment information can be more generally
# handled. Make it so that the user can set these variables:
#
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
# Make the program look at these variables and calculate the total paid
# appropriately.
#
# How much will Dave pay if he pays an extra $1000/month for 4 years starting
# in year 5 of the mortgage?

mortgage = 500000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

def total_paid(mortgage, interest_rate, monthly_payment, \
extra_payment_start_month, extra_payment_end_month, \
extra_payment):
    total_paid = 0.0
    current_month = 0

    while mortgage > 0:
        current_month += 1

        if current_month >= extra_payment_start_month and  \
        current_month <= extra_payment_end_month:
            mortgage = mortgage * (1 + interest_rate / 12) - \
                        (monthly_payment + extra_payment)
            total_paid += monthly_payment + extra_payment

        else:
            mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
            total_paid += monthly_payment

    return total_paid

total_paid = total_paid(mortgage, interest_rate, monthly_payment, \
extra_payment_start_month, extra_payment_end_month, extra_payment)

print("Total paid with extra $1000/month for 4 years starting in year 5", \
round(total_paid, 2))

# Exercise 1.10: Making a table

# Modify the program to print out a table showing the month, total paid so far,
#  and the remaining principal. The output should look something like this:
#
# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total paid 880074.1
# Months 310


total_paid = 0.0
mortgage = 500000.0
interest_rate = 0.05 # 5% percent
monthly_payment = 2684.11
month_no = 0

print("Month Total_Paid Remaining")

while mortgage > 0:
    mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
    total_paid += monthly_payment
    month_no += 1

    print(month_no, total_paid, mortgage)


# Exercise 1.11: Bonus
# While you’re at it, fix the program to correct for the overpayment that
# occurs in the last month.

total_paid = 0.0
mortgage = 500000.0
interest_rate = 0.05 # 5% percent
monthly_payment = 2684.11
month_no = 0
while mortgage > 0:
    if mortgage < monthly_payment:
        total_paid += mortgage
        mortgage = 0
    else:
        mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
        total_paid += monthly_payment
    month_no += 1

    print(f'{month_no:4d} ${total_paid:8.2f} ${mortgage:8.2f}')
