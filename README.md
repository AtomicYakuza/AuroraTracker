# Aurora Forecasting Application (AuroraTracker)

Welcome to the Aurora Forecasting Application, a Python program that predicts the visibility of auroras (Northern Lights) in Coventry using NOAA data: [3-day-forecast](https://services.swpc.noaa.gov/text/3-day-forecast.txt).
## 📋 Overview

### Version 0.4
🛠️ New Features
- Added an automatic data-saving feature to store results locally.
- Introduced a view historical data option, displaying all locally stored data in a table.
- Redesigned the menu input system for an improved user experience.

🐛 Bug Fixes
- Fixed an issue where entering “location” caused the program to incorrectly display an “invalid input” error

### Version 0.3
🛠️ New Features
- Added auto-location detection to provide an accurate forecast based on the user's current location (use a VPN to simulate different locations).
- Added file / location to Error Codes in README.md ([See here](#-error-codes))

🐛 Bug Fixes
- Fixed multiple occurrences of the misspelling "forcast" to "forecast."

### Version 0.2
🛠️ New Features
- Added location input after the initial Coventry check
- Added error codes for easier debugging ([See here](#-error-codes))
- Added multiple new try statements to catch errors and handle them

🐛 Bug Fixes
- Fixed README.md file with spelling and code changes
- Fixed crash when added information about geomagnetic storms was provided in the data from NOAA
- Changed the Coventry KP value to 9 (more accurate)

### Version: 0.1

🛠️ Features
- Real-time Data Fetching: Retrieves aurora forecast data.
- Visibility Prediction: Analyses the data to determine when an aurora might be visible in Coventry.
- User-Friendly Output: Displays predictions in an intuitive and readable format.

#### 🧰 Requirements

To run this program, you’ll need:
- Python 3.9 or higher (Oldest supported release at time of publish) [python.org](https://www.python.org/downloads/)
- Internet connection (for fetching NOAA data)

#### 🔍 How it Works
1. The Aurora class in AuroraClass.py handles:
    - Fetching NOAA data.
    - Cleaning and trimming the raw data.
    - Analysing data to determine aurora visibility.
2.	The main.py script:
    - Initialises the program.
    - Displays results in a user-friendly format.
3. The Locator class in locatorClass.py:
    - Uses the 'ipinfo.io' API to determine the user's current location.
    - Returns latitude, longitude and city where the user is - not exact location but close enough

#### 📂 File Structure
```
📁 AuroraTracker/
├── README.md               # This file
├── .gitignore              # Files/folders to ignore when committing to GitHub
├── LICENSE                 # License details (MIT)
├── 📁 Scripts/
│   ├── AuroraClass.py      # Contains the Aurora class for data fetching, cleaning, and analysis
│   ├── locatorClass.py     # Contains the Locator class for finding the user's: latitude, longitude & city
│   ├── main.py             # Main program file (Run program from here)
├── 📁 Data/
    ├── historicData.csv    # Contains the stored data requested by the program
```
## 🚀 How to Run

1.	Clone the Repository:
```
git clone https://github.com/AtomicYakuza/AuroraTracker.git
```
2. Move into the new directory
```
cd AuroraTracker
```

3.	~~Install Dependencies:~~

```
No external dependencies! This program uses only Python's built-in modules:
- 'time': For managing time-related operations
- 'urllib.request': For fetching data from NOAA and ipinfo
- 'json': For parsing text to json
- 'csv': For handling loading and saving
- 'os': For creating saving file locaitons
```

4.	Run the Program:
Execute the program using Python:
```
python scripts/main.py 
```
or
```
python3 scripts/main.py
```


## 📝 Future Features (Planned for Next Versions)
- 🎨 **UI Redesign**: Revamp the program’s starting interface for a cleaner and more user-friendly experience.
- 📊 **Advanced Visualisation**: Advanced data visualisation for better data representation

## 🚨 Error Codes
|**Code**|**File / location**|**Description**|**Solutions**|
|---|---|---|---|
|101|auroraClass.py|Error during fetching of data (NOAA)|Most likely cause of error is change in the data source|
|201|main.py|Unexpected User Input|Follow the program prompts or restart the program|
|301|auroraClass.py|Error during the editing of data|Submit issue|
|302|auroraClass.py|Error during the sorting of data|Submit issue|
|401|locatorClass.py|Error during fetching of data (ipinfo)| Submit issue|
|402|locatorClass.py|Error during json parse|Submit issue|
|501|fileHandlerClass.py|Error during file creation|Ensure no other programs are interfering in the working directory or files|
|502|fileHandlerClass.py|Error during folder creation|Ensure no other programs are interfering in the working directory or files|
|503|fileHandlerClass.py|Error during loading of data before saving|Ensure no other programs are interfering in the working directory or files|
|504|fileHandlerClass.py|Error during loading of data before table printing|Ensure no other programs are interfering in the working directory or files|

 Submit and track issues [here](https://github.com/AtomicYakuza/AuroraTracker/issues), or contribute directly by fixing issues and submitting a pull request. See [Contributing](#-contributing) for more info.

## 🛡️ License

This project is licensed under the **MIT** License. See the [LICENSE](/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. All code **must include detailed comments** for a pull request to be reviewed and accepted.

## 🌟 Acknowledgments
- NOAA for providing aurora forecast data.
- Python community for resources and libraries.
