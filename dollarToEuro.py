# States the title and purpose of the program and version number as well as programmer credit
print("Money converter")
print("This Program takes dollar amount from user and converts to euros")
print("Program version 1.00")
print("Written by MrBladez")

# While loop to let the user convert
# Dollars to Euros multiple times
while(True):
    # Ask the user if he wants to convert dollar to euro
    continueInput = input("Would you like to convert dollars to euros? ")
    if continueInput == "no":
        # if user entered no, than break the loop
        break
    elif continueInput == "yes":
        # if user entered yes, that the program gets the dollar
        # amount from the user and converts it to euros
        # then prints the euro amount
        dollar = float(input("Enter dollar amount to be converted: "))
        euro = dollar * 0.94540

        print("Euro amount is " + str(euro))
    
    
