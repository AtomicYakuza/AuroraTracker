#Aurora Prediction main.py
#--Last Version Changed: v0.4
#Created by AtomicYakuza on 10/12/2024

#from AuroraClass.py (file) import tthe Aurora Class
from auroraClass import Aurora #import custom classes from file (For file readability)
from locatorClass import Locator 
from fileHandlerClass import FileHander

MainAurora = Aurora() #instantiate the class as a global variable
MainLocator = Locator() 
MainFileHandler = FileHander()
#all of these dont have to global variables, but program is small and they would both be in main() what runs for the entirety of the program anyway


def main():
    menuPrint("Aurora Forecasting Application")  # Print a nice title
    latitude, longitude, city = MainLocator.getLocationFromAPI() #get current location from API, longitude is not used but returned just incase for future
    responseData = MainAurora.request()  # Requesting data from NOAA
    trimmedData, dates, times = MainAurora.cleanData(data=responseData)  # Trim the data and prepare it from plain text to lists
    MainFileHandler.saveFile(trimmedData,dates,times) #Call the fileHander to save the data to file
    daysAroraCouldHappen = MainAurora.dataAnalysis(trimmedData, times, dates, True, float(latitude))  # Validate if aurora is visible in Coventry
    menuPrint("Aurora Prediction")  # Print a nice title again
    printAuroraPrediction(daysAroraCouldHappen, dates, city) # Display Aurora prediction
    
    #input loop until done
    menuLoop = True #loop variable for while loop
    
    print("Would you like to conduct a forecast for a different area?")
    print("\n")
    printKPIMenu() #print the table 
    excepttedKPIMenuValues = ["1","2","3","4","5","6","7","8","9"] #list of values for the if statement to accept a new KP analysis
    while menuLoop == True: #creates an endless menu until user wants to exit the program
        print('''\
                List of Commands:
1 to 9 (inclusive)  -> Conducts a new forcast for that KP threshold
location            -> Outputs the current location forecast
history             -> Provides a table of all locally saved information
table               -> reprints the KP Value & Location table
n, no or exit       -> Exits the program''')
        inputSuccess=False #reset inputSucess
        try:
            menuSelection = menuInput() #try to take the user input
        except Exception as e:
            print(f"An error occurred (201): {e}") #if error occurs print the error
        else:
            inputSuccess=True #if completes with no errors, do input Success
        
        if inputSuccess == True: #only try to understand what the user has inputted if getting the input was a success
            if menuSelection in excepttedKPIMenuValues: #if KP value is entered conduct analysis
                daysAroraCouldHappen = MainAurora.dataAnalysis(trimmedData, times, dates,False, float(latitude), kpValueThreshold=int(menuSelection)) #call analysis function again with not using latitude
                printAuroraPrediction(daysAroraCouldHappen, dates, city ,location=int(menuSelection)) # Display Aurora prediction
            elif menuSelection.lower() == "no" or menuSelection.lower() == "n" or menuSelection.lower() == "exit": # if user wants to quit
                menuLoop = False # break loop and program ends
            elif menuSelection.lower() == "table": # if user wants table --force lower so if the user capitalises certain characters it shouldnt be an issue
                printKPIMenu() #print table
            elif menuSelection.lower() == "location":
                daysAroraCouldHappen = MainAurora.dataAnalysis(trimmedData, times, dates, True, float(latitude)) #call analysis function again with not using latitude
                printAuroraPrediction(daysAroraCouldHappen, dates, city) # Display Aurora prediction
            elif menuSelection.lower() == "history":
                MainFileHandler.printHistoricTable() #print historic data
            else: #an invalid message was inputted
                print("Invalid Input") #notify user input was invalid
        else:
            print("Seems like there was an error, please try again") #input error, prompt the user to try again
        print("")
            
        
        

def printKPIMenu():
    #This function justs prints the table for the user to understand what the value inputted means on location wise
    line1 = "+-------------+-------------+-------------+-------------+-------------+"
    line2 = "|  KP Value   |      3      |      5      |      7      |      9      |"
    line3 = "+-------------+-------------+-------------+-------------+-------------+"
    line4 = "|  Location   |    Alaska   | N. Scotland | N. Ireland  |  Whole UK   |"
    line5 = "+-------------+-------------+-------------+-------------+-------------+" 
    title = "KP Value & Location Table"
    line0 = ""
    loopAmount = round(len(line1)-len(title))/2 #finds the starting point for the title
    for i in range(int(loopAmount)): #until starting point
        line0 += " " # add white space to make it centered
    line0 += title # add the title of the table
    while len(line0) < len(line1): #untl string is same length as the next (un-needed really)
        line0 += " " # add white space
    #use of multiple variables makes it easier to edit the table as everything looks as it would be once printed to the user
    print(line0 + "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5)


def menuPrint(menuText):
    STRmenuDressing = menuDressing(menuText)  # Call function MenuDressing to determine the menu dressing
    print(STRmenuDressing)  # Print the top border
    print(" " + menuText)  # Print the menu title
    print(STRmenuDressing)  # Print the bottom border

def printAuroraPrediction(days, dates, customLocation, location=10):
    #locationlist holds all locations the program can provide analysis for. These are kept vague/ general areas as precise location is unkown.
    locationsList = ["The North Pole", "Above Alaska", "Alaska", "Between Alaska and North Scotland", "North Scotland", "Between North Scotland and Northen Ireland", "Northen Ireland", "Between Northen Ireland and South England", "Whole UK", customLocation]
    location -= 1 #the location is minused 1 to use location variable as a list pointer
    count = 0  # Count variable for visible auroras
    betweenStatements = [1,3,5,7] #All statement locations in the locationLists list that require special wording to make gramatical sense
    for i in range(len(days)):  # Loop through the days
        if days[i]:  # Check if aurora is visible
            count += 1  # Increment count if true

    if count != 0:  # If there is at least one visible aurora
        if location == 8: #This if statement is just to make sure the special wording of the statement makes gramatical sense
            print("An Aurora will be visible to the "+ locationsList[location] + " on: ", end="")  # Start the output message
        elif location in betweenStatements:
            print("An Aurora will be visible "+ locationsList[location] + " on: ", end="")  # Start the output message
        else:
            print("An Aurora will be visible in "+ locationsList[location] + " on: ", end="")  # Start the output message
        for i in range(len(days)):  # Loop through the days again
            if days[i]:  # If aurora is visible
                count -= 1  # Decrement count
                print(dates[i], end="")  # Print the date
                if count == 0:  # If no more dates are left
                    print(".")  # End with a period
                else:
                    print(", ", end="")  # Print a comma
    else:  # If no aurora is visible
        if location == 8: #This if statement is just to make sure the special wording of the statement makes gramatical sense
            print("Unfortunately, there will be no Aurora visible to the " + locationsList[location] + " in the next 3 days")  # Inform the user not visible
        elif location in betweenStatements:
            print("Unfortunately, there will be no Aurora visible " + locationsList[location] + " in the next 3 days")  # Inform the user not visible
        else:
            print("Unfortunately, there will be no Aurora visible in " + locationsList[location] + " in the next 3 days")  # Inform the user not visible

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