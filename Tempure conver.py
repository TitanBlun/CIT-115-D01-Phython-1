# James Blaze McMillan
# Assignment: Temp converter
# Reflection: I wouldn't say i really 'enjoyed' this one. It was the most tedious one.
# I really struggled with the if/else I won't lie. That's what most of my spring break was really spent on.
# 'if' starts a conitional block while  elif will check for any additional conditions. Optional how ever. else is a carch all for when no conditions are true. I like it call it the last resort. 
# I used else as a backup as you can see rather than the first one so it could catch people and have a fall back in case someone does try to go above the given numbers, being 212/100
#1. if and else are my probably going to be used the most by me as i'll probably try to hard code a single condition and have aneasy back up with the else statement.
#2. Don't try and do Kelvin because that will cause more headaches than it's worth
#3. I don't really have a third thing i learned because i'm still trying to process everything.
#. UHhhh my favorite color is blue and the reason i havent been to class is due to a death in the family so i apologize for my absence. Paired with dealing with my nephew most days.
# Hi again professor!!
print("Welcome to the Temperature Converter by JBM!!")


tempEnteredJBM = float(input("Enter a temperature please: "))

# Faren or Celc
tempTypeJBM = input("Is this Fahrenheit (F) or Celsius (C)? ")

# Valid input check, please don't be stupid and put kelvin blaze.
if tempTypeJBM != "F" and tempTypeJBM != "f" and tempTypeJBM != "C" and tempTypeJBM != "c":
    print("Enter a F or C")

# Fahrenhiet
elif tempTypeJBM == "F" or tempTypeJBM == "f":
    if tempEnteredJBM > 212:
        print("Temp can not be > 212! Please input somehting lower!")
    else:
        celsiusJBM = (5.0 / 9) * (tempEnteredJBM - 32)
        print("The Celsius equivalent is:", format(celsiusJBM, ".1f"))

# Celsius
elif tempTypeJBM == "C" or tempTypeJBM == "c":
    if tempEnteredJBM > 100:
        print("Temp can not be > 100! Please input something lower!")
    else:
        fahrenheitJBM = ((9.0 / 5.0) * tempEnteredJBM) + 32
        print("The Fahrenheit equivalent is:", format(fahrenheitJBM, ".1f"))
