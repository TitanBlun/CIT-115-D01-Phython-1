def main():
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the monthly interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months the account will be active: "))
    goal = float(input("Enter the goal amount you want your money to reach: "))

    current_amount = deposit
    month = 0

    while month < months and current_amount < goal:
        current_amount += current_amount * interest_rate
        month += 1

    print(f"After {month} months, your money will be: ${current_amount:.2f}")
    if current_amount >= goal:
        print("Congratulations! You reached your goal.")
    else:
        print("You did not reach your goal within the given time.")

if __name__ == "__main__":
    main()
