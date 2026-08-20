# Simple Interest Calculator
# Python Project for GitHub

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    return simple_interest, total_amount


print("======================================")
print("       SIMPLE INTEREST CALCULATOR")
print("======================================")

try:
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest (%): "))
    time = float(input("Enter Time (years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Please enter positive values.")
    else:
        interest, amount = calculate_simple_interest(
            principal, rate, time
        )

        print("\n----- RESULT -----")
        print(f"Principal Amount : ₹{principal:.2f}")
        print(f"Interest Rate    : {rate:.2f}%")
        print(f"Time             : {time:.2f} years")
        print(f"Simple Interest  : ₹{interest:.2f}")
        print(f"Total Amount     : ₹{amount:.2f}")

except ValueError:
    print("Invalid input! Please enter numbers only.")