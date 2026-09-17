# 🚀 NASA Near-Earth Object (NEO) Tracker

> A Python CLI tool that retrieves, analyzes, and displays Near-Earth Object (NEO) data using NASA's NeoWs API.

```text
..   .    .   ..   .   ..  ..   ..   .   ..   .   
 .-+:.... ...  ..   .   ..   .    .   ..  ..   ..  ..   .    .   
..  :*####++=:++: .... ..  .. ....   .   ..   .   ..   .   ..   ..
      .=*####+++**+==+: .--:..:..                         
        ..-**#**+=######*=+=++===+=::::. ...                   
            :-:+**##**#*+:::-++=----====-==-----.                 
   .   ..  ...  ==:==+==+=:.:++==:..:---:::---=:-.  ..   .   .   
..   .    .   ..  ...:-=--==:.:+***+-.......:-*%#+=*+-+.   ..   ..
   .   ..  ...  ..   .  ..-:=-..:--+=-:.  .=##*#%%#=+-::.    .   
..   .    .   ..   .   ..  ..::=---.:-+++:.*##+# +%%#+%**--:.   ..
   .   ..  ...  ..   .   ..  .-=++++-=-=\**--**#%%%##%%%+=#%*=#==.
..   .   ..   ..   .   ..  ... :---+===++\**#%%%%%%%%%#***#*#%-=-...
        .   .                      .:-==-=-+##%%%%%%%%%%#*+=**=-  
                                  ..:::-:-+\**#%%%%%%%%%%%%=+**+.
                                    ..:--:-#%%%%%%%%%#%%%#**
   .   ..  ...  ..   .   ..   .   ..   ..  ...:+*#%%%%###%%%%%%%
..   .   ..   ..   .   ..  ..   ..   .   ..   .. =##*##%#%%#%=....
   .   .   ..  ..   .   ..   .    .   ..  ..   ..  ...  .    .
```

---

## 🌌 About

**NASA NEO Tracker** is a command-line Python project that uses NASA's **Near Earth Object Web Service (NeoWs)** API to retrieve asteroid data for a selected date range.

The project started as a simple API-based asteroid tracker and evolved into a data-analysis project using **Pandas**.

### Current Version

**Version 2 — Pandas Analysis & CLI Improvements**

---

## ✨ Features

* 🔭 Search for Near-Earth Objects using a custom date range
* 🪨 Display asteroid names and estimated diameters
* ⚠️ Identify potentially hazardous asteroids
* 📏 Find the largest asteroid in the selected date range
* 📐 Find the smallest asteroid in the selected date range
* 🌍 Find the closest asteroid based on miss distance
* 📅 Display the closest approach date
* 📊 Calculate average asteroid diameter
* ⚠️ Calculate the percentage of potentially hazardous asteroids
* 🏆 Display the top 5 largest asteroids
* 📆 Group potentially hazardous asteroids by date
* 🔢 Sort asteroid data by estimated diameter
* ✅ Validate date formats and date ranges
* 🛡️ Handle API request errors
* 💻 Simple command-line interface
* 🌌 ASCII art splash screen
* ✨ Improved CLI formatting and presentation

---

## 🛠️ Technologies Used

* **Python**
* **NASA NeoWs API**
* **Requests**
* **Pandas**
* **python-dotenv**
* **Git & GitHub**

Pandas is used to organize the API response into a DataFrame and perform operations such as filtering, sorting, grouping, and calculating statistics.

---

## 📋 Requirements

Before running the project, make sure you have:

* Python 3.x
* A NASA API key
* Internet connection

The required Python packages are listed in `requirements.txt`.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/TheCreatorJJ/Nasa-asteroid-tracker.git
```

### 2. Enter the project directory

```bash
cd Nasa-asteroid-tracker
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

This project uses a NASA API key to access the NeoWs API.

Create a file named `.env` in the project folder:

```env
NASA_API_KEY=your_nasa_api_key_here
```

Your project structure should look similar to:

```text
Nasa-asteroid-tracker/
│
├── main.py
├── art.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

> [!IMPORTANT]
> Never upload your `.env` file or NASA API key to GitHub. The `.env` file is excluded using `.gitignore`.

---

## 🚀 Usage

Run the program with:

```bash
python main.py
```

The program will display the NASA NEO Tracker menu.

Enter a start date and end date using:

```text
YYYY-MM-DD
```

Example:

```text
Enter the start date (YYYY-MM-DD): 2026-01-01
Enter the end date (YYYY-MM-DD): 2026-01-07
```

The program retrieves the Near-Earth Object data from NASA and then analyzes the results using Pandas.

---

## 📊 Data Analysis

Version 2 introduced Pandas to make the project more than just an API data viewer.

The program currently performs analysis such as:

### Largest Asteroid

Finds the asteroid with the largest estimated maximum diameter.

### Smallest Asteroid

Finds the asteroid with the smallest estimated maximum diameter.

### Closest Approach

Finds the asteroid with the smallest recorded miss distance.

### Average Diameter

Calculates the average estimated maximum diameter of the retrieved asteroids.

### Hazardous Asteroids

Counts the number of potentially hazardous asteroids and calculates their percentage of the total results.

### Top 5 Largest

Sorts the asteroid DataFrame by diameter and displays the five largest asteroids.

### Hazardous Asteroids by Date

Groups potentially hazardous asteroids by their close-approach date.

---

## 🖥️ Example Output

```text
================================
        ASTEROID SUMMARY
================================
Total Asteroids: 36
Potentially Hazardous: 7
Hazardous Percentage: 19.44%
Largest Asteroid: 418265 (2008 EA32)
Diameter: 2,992.54 meters
Smallest Asteroid: (2018 TV5)
Diameter: 7.48 meters
Closest Asteroid: (2014 AF16)
Miss Distance: 3,071,593.48 km
Approach Date: 2026-01-04
Average Diameter: 285.73 meters

================================
      TOP 5 LARGEST ASTEROIDS
================================
1. 418265 (2008 EA32) - 2,992.54 meters
2. 26663 (2000 XK47) - 1,412.67 meters
3. 620103 (2018 LC3) - 1,042.41 meters
4. (2018 LC3) - 1,032.86 meters
5. 367390 (2008 MB5) - 924.78 meters

================================
       HAZARDOUS BY DATE
================================
2026-01-01: 3
2026-01-02: 1
2026-01-04: 1
2026-01-05: 1
2026-01-07: 1
```

> **Note:** The values above are example results. Results will vary depending on the selected date range and the data returned by NASA's API.

---

## 🧠 What I Learned

This project is part of my Python learning journey.

While building it, I practiced:

* Working with APIs
* Making HTTP requests with `requests`
* Using environment variables
* Working with JSON data
* Working with dictionaries and lists
* Using loops
* Using conditional statements
* Creating functions
* Working with dates using `datetime`
* Handling errors with `try` and `except`
* Building a CLI application
* Creating Pandas DataFrames
* Filtering DataFrames
* Sorting DataFrame data
* Finding maximum and minimum values
* Calculating averages
* Grouping and counting data
* Iterating through DataFrame rows
* Formatting numerical output
* Using Git
* Using GitHub
* Managing project dependencies

---

## 🗂️ Project Structure

```text
Nasa-asteroid-tracker/
│
├── main.py              # Main application
├── art.py               # ASCII art
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── .gitignore           # Files excluded from Git
└── .env                 # Private NASA API key
```

> `.env` is intentionally excluded from GitHub.

---

## 📈 Project Versions

### Version 1 — NASA API Tracker

The first version focused on learning how to work with an external API.

* NASA NeoWs API integration
* Custom date-range search
* Basic asteroid information
* Hazardous asteroid identification
* Largest asteroid detection
* Closest asteroid detection
* Close-approach date
* Date validation
* API error handling
* Basic CLI

### Version 2 — Data Analysis & CLI Improvements

The second version expanded the project into a small data-analysis application.

* Added Pandas
* Added DataFrame-based analysis
* Added smallest asteroid detection
* Added average diameter calculation
* Added hazardous asteroid percentage
* Added top 5 largest asteroid ranking
* Added hazardous asteroids grouped by date
* Added sorting and filtering
* Improved numerical formatting
* Improved CLI layout
* Added ASCII art
* Improved project documentation

---

## 🔮 Future Improvements

Possible improvements for future versions:

* 📊 Add Matplotlib visualizations
* 📈 Create charts showing asteroid data
* 📁 Add CSV export
* 🔎 Add more detailed asteroid filtering
* 📊 Add additional statistics
* 🖥️ Further improve the CLI
* 🌐 Eventually build a web-based dashboard
* 🚀 Expand the project for NASA Space Apps Challenge

---

## 🌎 Data Source

Asteroid data is provided by NASA's **Near Earth Object Web Service (NeoWs)** API.

NASA API:

https://api.nasa.gov/

---

## 📚 Project Purpose

This project was created as a hands-on Python learning project.

The goal is to gradually develop the project while learning new programming and data-analysis concepts rather than building everything at once.

**V1 → API**

**V2 → Pandas & Analysis**

**V3 → Visualization**

**Future → More advanced data science**

---

## 👨‍💻 Author

Created by **TheCreatorJJ** as a Python learning project.

⭐ If you find the project interesting, feel free to explore the code and follow its development.
