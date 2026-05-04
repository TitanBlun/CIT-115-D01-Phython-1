#James Blaze McMillan
#Assignment: Paint Estimator
#I'm not gonna lie to you. I did NOT like this assignment. I had to redownload the textbook to do the assignment and i really had a hard time.
#This whole assignment was a whole struggle. Working with the tax and such was a real hassle
#It's 11:52 PM on sunday so I'll take the docked points at this point 
#
#
#
import math

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Value must be positive and non-zero. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

#Rounded it up the nearest gallon
def getGallonsOfPaint(squareFeet, feetPerGallon):
    gallons_needed = squareFeet / feetPerGallon
    return math.ceil(gallons_needed)  

# Function to total hours * gallons
def getLaborHours(laborHoursPerGallon, totalGallons):
    return laborHoursPerGallon * totalGallons

def getLaborCost(laborHours, laborRate):
    return laborHours * laborRate

def getPaintCost(paintPrice, totalGallons):
    return paintPrice * totalGallons

def getSalesTax(state):
    state = state.upper()
    if state == "CT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return 0.07
    elif state == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(gallons, laborHours, paintCost, laborCost, taxRate, taxAmount, totalCost, lastName):
#unoptimized because im rushing
    output_lines = []
    output_lines.append("PAINT JOB ESTIMATE")
    output_lines.append(f"Gallons of paint required: {gallons}")
    output_lines.append(f"Hours of labor required: {laborHours:.2f}")
    output_lines.append(f"Cost of paint: ${paintCost:.2f}")
    output_lines.append(f"Labor charges: ${laborCost:.2f}")
    output_lines.append(f"Sales tax rate: {taxRate * 100:.2f}%")
    output_lines.append(f"Sales tax amount: ${taxAmount:.2f}")
    output_lines.append(f"Total cost of paint job (including tax): ${totalCost:.2f}")

    # Printing
    for line in output_lines:
        print(line)

    # File to write
    filename = f"{lastName}_PaintJobOutput.txt"
    with open(filename, "w") as file:
        for line in output_lines:
            file.write(line + "\n")
    print(f"\nFile created: {filename}")

def main():
    #Ask the main questions
    wallSpace_JBM = getFloatInput("Enter square feet of wall space: ")
    paintPrice_JBM = getFloatInput("Enter price of paint per gallon: $")
    feetPerGallon_JBM = getFloatInput("Enter square feet covered per gallon of paint: ")
    laborHoursPerGallon_JBM = getFloatInput("Enter labor hours required per gallon: ")
    laborRate_JBM = getFloatInput("Enter labor charge per hour: $")

    # Get the state and customers last name.
    state_JBM = input("Enter the state (CT, MA, ME, NH, RI, VT): ").strip()
    lastName_JBM = input("Enter customer's last name: ").strip()

    # The calcuations
    totalGallons_JBM = getGallonsOfPaint(wallSpace_JBM, feetPerGallon_JBM)
    totalLaborHours_JBM = getLaborHours(laborHoursPerGallon_JBM, totalGallons_JBM)
    laborCost_JBM = getLaborCost(totalLaborHours_JBM, laborRate_JBM)
    paintCost_JBM = getPaintCost(paintPrice_JBM, totalGallons_JBM)
    taxRate_JBM = getSalesTax(state_JBM)
    taxAmount_JBM = paintCost_JBM * taxRate_JBM
    totalCost_JBM = paintCost_JBM + laborCost_JBM + taxAmount_JBM

    # Show the estimate and pray it works
    showCostEstimate(totalGallons_JBM, totalLaborHours_JBM, paintCost_JBM,
                     laborCost_JBM, taxRate_JBM, taxAmount_JBM, totalCost_JBM, lastName_JBM)

# Praying this works
if __name__ == "__main__":
    main()
