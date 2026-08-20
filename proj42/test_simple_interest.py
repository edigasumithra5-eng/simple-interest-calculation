# Testbench for Simple Interest Calculator

from simple_interest import calculate_simple_interest


def run_test(principal, rate, time, expected_interest, expected_amount):

    interest, amount = calculate_simple_interest(
        principal, rate, time
    )

    print(f"Input: P={principal}, R={rate}, T={time}")

    if interest == expected_interest and amount == expected_amount:
        print("Result: TEST PASSED")
    else:
        print("Result: TEST FAILED")

    print(
        f"Calculated Interest = {interest:.2f}, "
        f"Total Amount = {amount:.2f}"
    )

    print("--------------------------------------")


print("======================================")
print("     SIMPLE INTEREST TESTBENCH")
print("======================================")

run_test(10000, 5, 2, 1000, 11000)

run_test(5000, 10, 3, 1500, 6500)

run_test(20000, 7.5, 2, 3000, 23000)

print("TESTBENCH COMPLETED")