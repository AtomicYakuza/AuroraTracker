#Aurora Prediction auroraClass.py
#--Last Version Changed: v1.0
#Created by AtomicYakuza on 10/12/2024

class Aurora:
    import urllib.request #import a request module

    #global variable declaration
    totalSteps = 3 #total number of steps in the loading process - dont have to edit multiple strings when changes are made
    APIurl = "https://services.swpc.noaa.gov/text/3-day-forecast.txt" #APIurl declared here for quick changing/ checking
    development = False


    def request(self):
        #requesting the data from the source
        try:
            response = self.urllib.request.urlopen(self.APIurl) #this line requests the data from the NOAA
            data = response.read().decode('utf-8')  # Decode the response to a string
        except Exception as e:
            #if error does occur
            print(f"An error occurred (101): {e}") #print the error for debug --most likely an issue with the requesting of data eg: server down
        return data #provide data to the parent function

    def cleanData(self, data):
        #Function is split into 2 parts.
        #Part 1: trims the data from the request by removing all non essential data
        #Part 2: puts the data into different arrays to be used in other functions
        #PART 1
        lines = data.splitlines()  # Split the text into individual lines
        complete = False 
        found = False
        cleanedData = ""
        # Example: Find specific lines by keywords
        try:
            for line in lines: #for the amount of lines there are. Each line is in a variable of "line" within the loop
                if complete == False: #if string has not been found
                    if found == True:
                        if line.startswith("Rationale:"): # if line starts with "Rationale:" it is assumed we have passed the data and already got what we need
                            complete = True #completed = true and when the loop repeats nothing will occur
                        else:
                            tempLine = line.replace(" ", "") #removes all the spaces in the current line, only should leave the data
                            cleanedData += tempLine #add the temp line to the cleaned data string
                    else:
                        if line.startswith("NOAA Kp index"):
                            #just before the text that we want, the title starts with this
                            found = True #after finding the data found = True to start the reading of information
                        elif line.startswith("Rationale:"): #this is for reduency, should never execute as found should == True by the time this function reads the "Rationale:" line
                            complete = True
        except Exception as e:
            print(f"An error occurred (301): {e}")

        
        #PART 2
        arrayDates = []
        #put dates into a 2d array
        try:
            for i in range(3): #3 days, loops for the number of days
                arrayDates.append(cleanedData[:5]) #add the next five characters into a new entry into the arrayDates list
                cleanedData = cleanedData[5:] #remove the first 5 letters that have just been put into the list from the string

            arrayTimes = []
            arrayData = []
            for i in range(8): #8 time entries are given
                if cleanedData[0] == "(":
                    cleanedData = cleanedData[4:] #fixed bug here if the extra info was provided for the 3rd day 
                arrayTimes.append(cleanedData[:7]) # get the next five characters and put them into the time list. 
                cleanedData = cleanedData[7:] #Again, remove the first 7 letters
                for i in range(3): #for each of the days, data is provided
                    if cleanedData[0] == "(":
                        #extra information about geomagnetic storms has been provided must be removed
                        cleanedData = cleanedData[4:] #remove the extra data for the array
                    arrayData.append(cleanedData[:4]) #get the next 4 characters as all data is provided in a "x.xx" format
                    cleanedData = cleanedData[4:] #remove the characters just taken

            w , h = len(arrayDates), len(arrayTimes) #declare w(idth) and h(eigh) varaibles
            combinedData = [[0 for x in range(w)] for y in range(h)] #create a 2d array with a width of how many dates we have and a hieght of how many times we have
            count = 0 #need an external count as there is a sub loop
            for i in range(h): #re-use of variables as the size of the 2darray is known already
                for j in range(w): #same here ^
                    combinedData[i][j] = arrayData[count] #put data into this array
                    count += 1 #increment count variable to shift the pointer of the arrayData array
        except Exception as e:
            print(f"An error occurred (302): {e}")
        if self.development == True:
            print(combinedData)
            print(arrayDates)
            print(arrayTimes)
        #this part 2 returns the combined data in a 2dArray like [[x.xx,x.xx,x.xx],[x.xx,x.xx,x.xx]...] with each of the smaller arrays representing a specific time across 3 days.
        return combinedData, arrayDates, arrayTimes #returns an array of the data values, the dates and the times

    def dataAnalysis(self, data, time, date, longAndLat,latitude, kpValueThreshold=9): # kpValueThreshold should be 9 for coventry -thats why its the default value
        #https://www.swpc.noaa.gov/content/tips-viewing-aurora --this is a source of information to know at what strength the northn lights would be visible in location
        AuroraGoingToHappen = [False, False, False]
        AuroraGoingToHappenTime = []
        #loop and find anytime the arora would be present in the uk
        #KP dictionary/ lookup table for latitude to KP value  
        latitudeList = [[62.7,3],[58.5,5],[54.3, 7], [50.1,9]]
        if longAndLat == True: #if using latitude to find KP value/ threshold
            valueFound = False
            for i in range(len(latitudeList)):
                if latitude >= latitudeList[i][0]:
                    #kp value found
                    valueFound = True
                    kpValueThreshold = latitudeList[i][1] #get variable from the 'KP dictionary'
        
            if valueFound == False:
                #still havent found anything due to latitude being too low
                kpValueThreshold = 10


        AuroraGoingToHappenTime = []
        AuroraGoingToHappenTimeAll=[]
        for i in range(len(date)):
            for j in range(len(time)):
                if float(data[j][i]) >= kpValueThreshold: #if the value is greater or equal to the threshold then will be visible
                    AuroraGoingToHappen[i] = True #change the correct day to true
                    AuroraGoingToHappenTime.append(time[j])
            if float(data[j][i]) >= kpValueThreshold:
                AuroraGoingToHappenTimeAll.append(AuroraGoingToHappenTime)
            else:
                AuroraGoingToHappenTimeAll.append([])
            AuroraGoingToHappenTime = []


        return AuroraGoingToHappen, AuroraGoingToHappenTimeAll#return array of True or Falses and optional times