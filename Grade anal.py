# I liked NOTHING about this assignment I can't lie LOL
# I've spent 3 hours after a weekend out the house not realizing that my input for the Y/N was case sensetive
# I just wrote it to just just add and average the first three and not count the lowest (Sorry im trying to submiut beofre the time)
#
strNameJBM = input("Enter the Test taker's name: ")

print("\nEnter the 4 test scores (whole numbers pleaes and thank you):")
intTest1JBM = int(input("Test score 1: "))
intTest2JBM = int(input("Test score 2: "))
intTest3JBM = int(input("Test score 3: "))
intTest4JBM = int(input("Test score 4: "))


if intTest1JBM < 0 or intTest2JBM < 0 or intTest3JBM < 0 or intTest4JBM < 0:
    print("Test scores must be greater than 0.")
    exit()

# THIS IS CASE SENSETIVE BLAZE HOLY SHIT
strDropLowestJBM = input("\nShould the lowest grade be dropped? (Y or N): ")

if strDropLowestJBM != "Y" and strDropLowestJBM != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

fltSumJBM = 0.0
intCountJBM = 0

if strDropLowestJBM == "Y":
    
    intLowestJBM = intTest1JBM
    
    if intTest2JBM < intLowestJBM:
        intLowestJBM = intTest2JBM
    if intTest3JBM < intLowestJBM:
        intLowestJBM = intTest3JBM
    if intTest4JBM < intLowestJBM:
        intLowestJBM = intTest4JBM
    
    if intTest1JBM != intLowestJBM:
        fltSumJBM = fltSumJBM + intTest1JBM
        intCountJBM = intCountJBM + 1
    if intTest2JBM != intLowestJBM:
        fltSumJBM = fltSumJBM + intTest2JBM
        intCountJBM = intCountJBM + 1
    if intTest3JBM != intLowestJBM:
        fltSumJBM = fltSumJBM + intTest3JBM
        intCountJBM = intCountJBM + 1
    if intTest4JBM != intLowestJBM:
        fltSumJBM = fltSumJBM + intTest4JBM
        intCountJBM = intCountJBM + 1
    
    )
    fltAverageJBM = fltSumJBM / intCountJBM

else:
    fltAverageJBM = (intTest1JBM + intTest2JBM + intTest3JBM + intTest4JBM) / 4.0


if fltAverageJBM >= 97.0:
    strLetterGradeJBM = "A+"
elif fltAverageJBM >= 94.0:
    strLetterGradeJBM = "A"
elif fltAverageJBM >= 90.0:
    strLetterGradeJBM = "A-"
elif fltAverageJBM >= 87.0:
    strLetterGradeJBM = "B+"
elif fltAverageJBM >= 84.0:
    strLetterGradeJBM = "B"
elif fltAverageJBM >= 80.0:
    strLetterGradeJBM = "B-"
elif fltAverageJBM >= 77.0:
    strLetterGradeJBM = "C+"
elif fltAverageJBM >= 74.0:
    strLetterGradeJBM = "C"
elif fltAverageJBM >= 70.0:
    strLetterGradeJBM = "C-"
elif fltAverageJBM >= 67.0:
    strLetterGradeJBM = "D+"
elif fltAverageJBM >= 64.0:
    strLetterGradeJBM = "D"
elif fltAverageJBM >= 60.0:
    strLetterGradeJBM = "D-"
else:
    strLetterGradeJBM = "F"


print("\n" + "="*40)
print(f"Student Name: {strNameJBM}")
print(f"Test Average: {fltAverageJBM:.1f}")
print(f"Letter Grade: {strLetterGradeJBM}")
print("="*40)
