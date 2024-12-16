#Aurora Prediction main.py
#--Last Version Changed: v0.1
#Built by AtomicYakuza on 10/12/2024

#from AuroraClass.py (file) import tthe Aurora Class
from auroraClass import Aurora #import custom class from file (For file readability)

MainAurora = Aurora() #instantiate the class as a global variable

def main():
    menuPrint("Aurora Forecasting Application")  # Print a nice title
    responseData = MainAurora.request()  # Requesting data from NOAA
    trimmedData, dates, times = MainAurora.cleanData(data=responseData)  # Trim the data and prepare it from plain text to lists
    daysAroraCouldHappen = MainAurora.dataAnalysis(trimmedData, times, dates)  # Validate if aurora is visible in Coventry
    menuPrint("Aurora Prediction")  # Print a nice title again
    printAuroraPrediction(daysAroraCouldHappen, dates) # Display Aurora prediction
    # menuSelection = menuInput() -- here in v0.1 as foundation for next version

def menuPrint(menuText):
    STRmenuDressing = menuDressing(menuText)  # Call function MenuDressing to determine the menu dressing
    print(STRmenuDressing)  # Print the top border
    print(" " + menuText)  # Print the menu title
    print(STRmenuDressing)  # Print the bottom border

def printAuroraPrediction(days, dates):
    count = 0  # Count variable for visible auroras
    for i in range(len(days)):  # Loop through the days
        if days[i]:  # Check if aurora is visible
            count += 1  # Increment count if true

    if count != 0:  # If there is at least one visible aurora
        print("An Aurora will be visible in Coventry on: ", end="")  # Start the output message
        for i in range(len(days)):  # Loop through the days again
            if days[i]:  # If aurora is visible
                count -= 1  # Decrement count
                print(dates[i], end="")  # Print the date
                if count == 0:  # If no more dates are left
                    print(". ", end="")  # End with a period
                else:
                    print(", ", end="")  # Print a comma
    else:  # If no aurora is visible
        print("Unfortunately, there will be no Aurora visible in Coventry in the next 3 days")  # Inform the user

def menuDressing(Menustring):
    menuDressing = "+"  # Start the menu dressing with "+"
    for i in range(len(Menustring)):  # Repeat for the length of the string
        menuDressing += "-"  # Add "-" for each character
    menuDressing += "+"  # End with "+"
    return menuDressing  # Return the dressing

def menuInput():
    choice = input(">")  # Input prompt with ">"
    return choice  # Return the user input

# invoke the main method
main()