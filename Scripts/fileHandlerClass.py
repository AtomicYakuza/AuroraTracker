#Aurora Prediction fileHandlerClass.py
#--Last Version Changed: v1.1
#Created by AtomicYakuza on 18/12/2024
class FileHander:
    import os
    import csv
    filePath = "Data/historicData.csv"
    fileFolder = filePath.split('/')[0] #gets the parent folder for the file path
    def checkLocationExists(self):
        #function checks if the folder and file exists and then creates the file
        if self.os.path.exists(self.fileFolder):
            if self.os.path.exists(self.filePath):
                #file exists then exit function
                return True
            else:
                #try to create a new file
                try:
                    with open(self.filePath, "w"):
                        pass
                except Exception as e:
                    print(f"An error occurred (501): {e}")
                    return False
                else:
                    return True
        else:
            #if no 'fileFolder' var folder exists create one
            try:
                self.os.makedirs(self.fileFolder) #create the folder
            except Exception as e:
                print(f"An error occurred (502): {e}")
            try:
                with open(self.filePath, "w"):  #assumed as no folder, no file will also be there so just create automatically
                    pass
            except Exception as e:
                print(f"An error occurred (501): {e}")
            else:
                return True

    def loadFile(self):
        #check if file exists
        fileFound = self.checkLocationExists()
        #just a double check and exits the sub-routine
        if fileFound == False:
            #exit, no error given to use as should have been given in the try statemnt within the checkLocationExists function
            return
        #file is found and function continues

        with open(self.filePath, 'r') as file: #read the file
            saveData = file.readlines() #read all lines at once
            return saveData # return the data

    def convertData(self, saveData):
        #this whole function converts the read data into a list of data for easier manipulaton
        newData = []
        for i in range(len(saveData)): #for each record in savedata
            tempsaveData = saveData[i].split(',') #ta
            if "\n" in tempsaveData[2]:
                tempsaveData[2] = tempsaveData[2][:-1]
                #tempsaveData[2] = tempsaveData[2][1:]
            newDate = tempsaveData[0]
            newTime = tempsaveData[1]
            newValue = tempsaveData[2]
            newData.append(newDate)
            newData.append(newTime)
            newData.append(newValue)
        return newData

    def saveFile(self, newData, newDates, newTimes):
        #get existing data
        try:
            oldSaveData = self.loadFile()
        except Exception as e:
            print(f"Tried to load data from file for saving, error occured (503): {e}")
        
        saveData = self.convertData(oldSaveData)
        #add new data into existing data
        foundCount = -1
        foundDataCount = -1
        updatedData = [False, False, False]
        for i in range(len(newDates)): #loop every new date we need to slot in
            foundDataCount += 1
            foundTimeCount = -1
            for j in range(len(saveData)): #loop every entry in the saved data
                if newDates[i] == saveData[j]:
                    updatedData[i] = True
                    foundTimeCount += 1
                    #update record
                    saveData[j+1] = newTimes[foundTimeCount] #time
                    saveData[j+2] = newData[foundTimeCount][foundDataCount]#value

        #once data has been updated, must find which date is new and add
        for i in range(len(updatedData)):
            if updatedData[i] == False:
                #not updated must add
                for j in range(len(newTimes)):
                    #add date
                    saveData.append(newDates[i])
                    #add time
                    saveData.append(newTimes[j])
                    #add value
                    saveData.append(newData[j][i])
                    
        #save fileå
        with open(self.filePath, "w", newline="") as file:
            writer = self.csv.writer(file, quoting=self.csv.QUOTE_MINIMAL)

            for i in range(0, len(saveData), 3):
                row = saveData[i:i+3] #get every 3 values as a row
                writer.writerow(row)


    def printHistoricTable(self):
        try:
            oldSaveData = self.loadFile()
        except Exception as e:
            print(f"Tried to load data from file for table, error occured (504): {e}")
        
        saveData = self.convertData(oldSaveData) #convert data into usable list
        #find largest length of column 1 (Date)
        currentLongestValue = 0
        for i in range(round((len(saveData)/3)+0.5)): #+0.5 always makes it round up
            if len(saveData[i*3]) > currentLongestValue:
                currentLongestValue = len(saveData[i*3])
        column1Length = currentLongestValue
        #find the largest length of column 2 (Time)
        currentLongestValue = 0
        for i in range(round((len(saveData)/3)+0.5)): #+0.5 always makes it round up
            if len(saveData[(i*3)+1]) > currentLongestValue:
                currentLongestValue = len(saveData[(i*3)+1])
        column2Length = currentLongestValue
        #find the largest length of column 3 (Value)
        currentLongestValue = 0
        for i in range(round((len(saveData)/3)+0.5)): #+0.5 always makes it round up
            if len(saveData[(i*3)+2]) > currentLongestValue:
                currentLongestValue = len(saveData[(i*3)+2])
        column3Length = currentLongestValue

        #build the columns/ seperators
        column1 = "+"
        for i in range(column1Length+1):
            column1 += "-"
        column1 += "+"
        column2 = ""
        for i in range(column2Length):
            column2 += "-"
        column2 += "+"
        column3 = ""
        for i in range(column3Length+6):
            column3 += "-"
        column3 += "+"

        betweenLine = column1 + column2 + column3
        
        #print the column headers
        print(betweenLine)
        print("| Date | Time  | KP Value |")

        #print the table
        for i in range(round((len(saveData)/3)+0.5)):
            print(betweenLine)
            print("|" + saveData[i*3] + " |" + saveData[(i*3)+1] + "|   " + saveData[(i*3)+2] +"   |")
        print(betweenLine)
        print("| Date | Time  | KP Value |")
        print(betweenLine)


