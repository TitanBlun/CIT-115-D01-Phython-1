def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def getMedian(numbers):
    count = len(numbers)

    # If the list has an odd number of values
    if count % 2 == 1:
        middle = count // 2
        median = float(numbers[middle])

    # If the list has an even number of values
    else:
        middle = count // 2
        median = (numbers[middle] + numbers[middle - 1]) / 2

    return float(median)


def main():
    salesList = []

    repeat = "Y"

    while repeat.upper() == "Y":
        sales = getFloatInput("Enter sales value: ")
        salesList.append(sales)

        while True:
            repeat = input("Enter another value Y or N: ")

            if repeat.upper() == "Y" or repeat.upper() == "N":
                break
            else:
                print("Please enter Y or N only.")

    # Sort list
    salesList.sort()

    print("\nSales Values")
    for value in salesList:
        print("${:,.2f}".format(value))

    # Calculations
    minimum = min(salesList)
    maximum = max(salesList)
    total = sum(salesList)
    average = total / len(salesList)
    median = getMedian(salesList)
    commission = total * 0.03

    # Output results
    print("\nStatistics")
    print("Minimum:   ${:,.2f}".format(minimum))
    print("Maximum:   ${:,.2f}".format(maximum))
    print("Total:     ${:,.2f}".format(total))
    print("Average:   ${:,.2f}".format(average))
    print("Median:    ${:,.2f}".format(median))
    print("Commission:${:,.2f}".format(commission))


main()
