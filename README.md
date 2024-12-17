

# Aurora Forecasting Application (AuroraTracker)

Welcome to the Aurora Forecasting Application, a Python program that predicts the visibility of auroras (Northern Lights) in Coventry using NOAA data: [3-day-forecast](https://services.swpc.noaa.gov/text/3-day-forecast.txt).
## 📋 Overview

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

#### 📂 File Structure
```
📁 AuroraTracker/
├── README.md               # This file
├── .gitignore              # Files/folders to ignore when committing to GitHub
├── LICENSE                 # License details (MIT)
├── 📁 Scripts/
    ├── AuroraClass.py      # Contains the Aurora class for data fetching, cleaning, and analysis
    ├── main.py             # Main program file (Run program from here)
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
No external dependencies! this program uses only Python's built-in modules:
- 'time': For managing time-related operations
- 'urllib.request': For fetching data from NOAA
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
- 💾 **Historic Data**: Save and view past aurora forecasts
- 📊 **Advanced Visualisation**: Advanced data visualisation for better data representation

## 🚨 Error Codes
|**Code**|**Description**|**Solutions**|
|---|---|---|
|101|Error during fetching of data|Most likely cause of error is change in the data source|
|201|Unexpected User Input|Follow the program prompts or restart the program|
|301|Error during the editing of data|Unexpected logic issue|
|302|Error during the sorting of data|Unexpected logic issue|

 Submit and track issues [here](https://github.com/AtomicYakuza/AuroraTracker/issues), or contribute directly by fixing issues and submitting a pull request. See [Contributing](#🤝-contributing) for more info.

## 🛡️ License

This project is licensed under the **MIT** License. See the [LICENSE](/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. All code **must include comments** for a pull request to be reviewed and accepted.

## 🌟 Acknowledgments
- NOAA for providing aurora forecast data.
- Python community for resources and libraries.
