#James B McMillan
#Assignment: Real estate with Lists
#Reflection: I can't say I liked a lot of things, fiddiling with the .format was oddly enjoyable?
#A list is just a built-in data type or "storage" to really just store things for us to call back on
#nothing that i really struggled with honestly! everything was pretty simple this time around!
#I didn't really add the notation this time around because it slipped my mind

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Not a valid input. Please enter a number.")


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
            repeat = input("Are you entering another sale? Y/N ")

            if repeat.upper() == "Y" or repeat.upper() == "N":
                break
            else:
                print("Are you entering another sale? Y/N.")

    # the sorter
    salesList.sort()

    print("\nSales Values")
    for value in salesList:
        print("${:,.2f}".format(value))

    # my calculations 
    minimum = min(salesList)
    maximum = max(salesList)
    total = sum(salesList)
    average = total / len(salesList)
    median = getMedian(salesList)
    commission = total * 0.03

    # This is where the outputs are put to rest
    print("\nStatistics")
    print("Minimum:   ${:,.2f}".format(minimum))
    print("Maximum:   ${:,.2f}".format(maximum))
    print("Total:     ${:,.2f}".format(total))
    print("Average:   ${:,.2f}".format(average))
    print("Median:    ${:,.2f}".format(median))
    print("Commission:${:,.2f}".format(commission))


main()
