#Aurora Prediction calendarClass.py
#--Last Version Changed: v1.1
#Created by AtomicYakuza on 10/01/2025
class CalendarClass:
    import datetime
    import os

    def checkLocationExists(self, filePath, fileFolder):
        #function checks if the folder and file exists and then creates the file
        if self.os.path.exists(fileFolder):
            if self.os.path.exists(filePath):
                #file exists then exit function
                return True
            else:
                #try to create a new file
                try:
                    open(filePath, "w")
                except Exception as e:
                    print(f"An error occurred (501): {e}")
                    return False
                else:
                    return True
        else:
            #if no 'fileFolder' var folder exists create one
            try:
                self.os.makedirs(fileFolder) #create the folder
            except Exception as e:
                print(f"An error occurred (502): {e}")
            try:
                open(filePath, "w") #assumed as no folder, no file will also be there so just create automatically
            except Exception as e:
                print(f"An error occurred (501): {e}")
            else:
                return True


    def writeCalendar(self, eventName, startTime, endTime, location, date):
        #save to .ics file
        #convert month into a number
        if date[:3] == "Jan":
            month = 1
        elif date[:3] == "Feb":
            month = 2
        elif date[:3] == "Mar":
            month = 3
        elif date[:3] == "Apr":
            month = 4
        elif date[:3] == "May":
            month = 5
        elif date[:3] == "Jun":
            month = 6
        elif date[:3] == "Jul":
            month = 7
        elif date[:3] == "Aug":
            month = 8
        elif date[:3] == "Sep":
            month = 9
        elif date[:3] == "Oct":
            month = 10
        elif date[:3] == "Nov":
            month = 11
        elif date[:3] == "Dec":
            month = 12
        finalStartTime = startTime[:2]
        finalEndTime = endTime[3:5]
        endMinute = 0
        if finalEndTime == "00":
            finalEndTime = "23"
            endMinute = 59
        finalDate = date[-2:]
        #create datetimes
        start_time = self.datetime.datetime(self.datetime.datetime.now().year, month, int(finalDate), int(finalStartTime), 0, 0).strftime("%Y%m%dT%H%M%S")
        end_time = self.datetime.datetime(self.datetime.datetime.now().year, month, int(finalDate), int(finalEndTime), endMinute, 0).strftime("%Y%m%dT%H%M%S")

        description = "An Aurora will be visible from: " + finalStartTime + " to " + finalEndTime + " in " + location + "."
        #if month is only 1 number add a zero for readability of the file name
        if month > 9:
            FileName = "event-" + str(self.datetime.datetime.now().year) + "-" + str(month) + "-" + str(finalDate) + "_" + finalStartTime + "_to_" + finalEndTime
        else:
            FileName = "event-" + str(self.datetime.datetime.now().year) + "-0" + str(month) + "-" + str(finalDate) + "_" + finalStartTime + "_to_" + finalEndTime
        filePath = "Calendar Events/"+FileName+".ics"
        fileFolder = filePath.split('/')[0] #gets the parent folder for the file path
        file = filePath.split('/')[1]


        #ics file formating
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
BEGIN:VEVENT
SUMMARY:{eventName}
DTSTART:{start_time}
DTEND:{end_time}
DESCRIPTION:{description}
LOCATION:{location}
END:VEVENT
END:VCALENDAR"""
        #check if file exists
        self.checkLocationExists(filePath, fileFolder) #check if file and folder exists
        #write to file
        with open(filePath, "w") as file:
            file.write(ics_content)
        
        return FileName + ".ics"




        

