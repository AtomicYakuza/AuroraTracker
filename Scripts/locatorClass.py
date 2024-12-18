#Aurora Prediction locatorClass.py
#--Last Version Changed: v0.3
#Created by AtomicYakuza on 17/12/2024

class Locator:
    import urllib.request #import a request module
    import json
    APIurl = "https://ipinfo.io"

    def getLocationFromAPI(self):
        try:
            response = self.urllib.request.urlopen(self.APIurl) #request location data
            data = response.read().decode('utf-8') #convert response into text
            json_data = self.json.loads(data) #convert response into json format
            location = json_data.get('loc', '') #get the latitude and longitude into 1 string
            city = json_data.get('city','') #get the city location for printing
            found = False 
            count = 0 #as the loop amount is unkown, a while loop was better. Needed another variable for count
            while found == False:
                if location[count] == ",": #if found a comma (seperates the latitude and longitude)
                    latitude = location[:count] #latitude is the first part of the stirng up to the comma
                    longitude = location[count+1:] #longitude is the last part of the string after the comma
                    found = True #found is true, breaks the loop
                if count == len(location): #if the count is 
                    print("error") #
                    found = True #break loop
                count += 1 #increment loop
        except self.urllib.error.URLError as e: #error when requesting the data
            print(f"Error fetching data (401): {e}") 
        except self.json.JSONDecodeError as e: #error when decoding json
            print(f"Error decoding JSON (402): {e}")
        return latitude, longitude, city #return all required data