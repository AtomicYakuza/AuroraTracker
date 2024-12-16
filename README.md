

# Aurora Forecasting Application

Welcome to the Aurora Forecasting Application, a Python program that predicts the visibility of auroras (Northern Lights) in Coventry using NOAA data: [3-day-forcast](https://services.swpc.noaa.gov/text/3-day-forecast.txt).
## 📋 Overview

### Version: 0.1

🛠️ Features
- Real-time Data Fetching: Retrieves aurora forecast data.
- Visibility Prediction: Analyses the data to determine when an aurora might be visible in Coventry.
- User-Friendly Output: Displays predictions in an intuitive and readable format.

🧰 Requirements

To run this program, you’ll need:
- Python 3.7 or higher
- Internet connection (for fetching NOAA data)

📂 File Structure
```
📁 AuroraTracker/
├── Readme.md               # This file
├── .gitignore              # Files/folders to ignore when commiting to github
├── LICENSE                 # License details (MIT)
├── 📁 Scripts/
    ├── AuroraClass.py      # Contains the Aurora class for data fetching, cleaning, and analysis
    ├── main.py             # Main program file (Run program from here)
```
## 🚀 How to Run

1.	Clone the Repository:
```
git clone https://github.com/AtomicYakuza/AuroraTracker.git

cd aurora-forecasting
```

2.	~~Install Dependencies:~~

```
No dependencies! All modules used are built into python
- time
- urllib.request
```

3.	Run the Program:
Execute the program using Python:
```
python main.py
```

🔍 How It Works
1. The Aurora class in AuroraClass.py handles:
- Fetching NOAA data.
- Cleaning and trimming the raw data.
- Analysing data to determine aurora visibility.
2.	The main.py script:
- Initialises the program.
- Displays results in a user-friendly format.

## 📝 Future Features (Planned for Next Versions)
- Increase reliability
- Saving system for historic data
- Advanced data visualization.
- User input for location

## 🛡️ License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## 🌟 Acknowledgments
- NOAA for providing aurora forecast data.
- Python community for resources and libraries.
