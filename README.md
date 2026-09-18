# 🚀 NASA Near-Earth Object (NEO) Tracker

> *A Python CLI tool that retrieves, analyzes, and visualizes Near-Earth Object (NEO) data using NASA's NeoWs API.*

```text
..   .    .   ..   .   ..  ..   ..   .   ..   .
.-+:.... ...  ..   .   ..   .    .   ..  ..   ..  ..   .   .
..  :*####++=:++: .... ..  .. ....   .   ..   .   ..   .   ..
      .=*####+++**+==+: .--:..:..                        
        ..-**#**+=######*=+=++===+=::::. ...              
            :-:+**##**#*+:::-++=----====-==-----.         
   .   ..  ...  ==:==+==+=:.:++==:..:---:::---=:-.  ..   .   .
..   .    .   ..  ...:-=--==:.:+***+-.......:-*%#+=*+-+.   ..   ..
   .   ..  ...  ..   .  ..-:=-..:--+=-:.  .=##*#%%#=+-::.    .
..   .    .   ..   .   ..  ..::=---.:-+++:.*##+# +%%#+%**--:.   ..
   .   ..  ...  ..   .  ..  .  .-=++++-=-=\**--**#%%%##%%%+=#%*=#==.
..   .   ..   ..   .   ..  ... :---+===++\**#%%%%%%%%%#***#*#%-=-...
        .   .                     .:-==-=-+##%%%%%%%%%%#*+=**=-
                                  ..:::-:-+\**#%%%%%%%%%%%%=+**+.
                                    ..:--:-#%%%%%%%%%#%%%#**
   .   ..  ...  ..   .   ..   .   ..   ..  ...:+*#%%%%###%%%%%%%
..   .   ..   ..   .   ..  ..   ..   .   ..   .. =##*##%#%%#%=....
   .   .   ..  ..   .   .   ..   .    .   ..  ..   ...  .    .
```

## 🌌 About

**NASA NEO Tracker** is a command-line Python project that uses NASA's **Near Earth Object Web Service (NeoWs)** API to retrieve asteroid data for a selected date range.

The project started as a simple API-based asteroid tracker and evolved into a data-analysis and visualization project using **Pandas** and **Matplotlib**.

### Current Version

**Version 3.0 — Data Visualization with Matplotlib**

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
* 📊 Visualize the top 5 largest asteroids using a bar chart
* 📈 Generate graphical representations of asteroid data
* 🖥️ Access visualizations through the CLI menu

---

## 🛠️ Technologies Used

* **Python**
* **NASA NeoWs API**
* **Requests**
* **Pandas**
* **Matplotlib**
* **python-dotenv**
* **Git & GitHub**

Pandas is used to organize the API response into a DataFrame and perform operations such as filtering, sorting, grouping, and calculating statistics.

Matplotlib is used to visualize asteroid data through charts and graphs.

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

> ⚠️ `.env` contains your private API key and should never be uploaded to GitHub.

---

## 🚀 Usage

Run the program with:

```bash
python main.py
```

The program will display the NASA NEO Tracker menu:

```text
======================================
           NASA NEO TRACKER
 Near-Earth Object (NEO) Data Analyzer
======================================

1. Search asteroids
2. Show top 5 Largest
3. Exit
```

### Search Asteroids

Select option:

```text
1
```

Enter a start date:

```text
Enter the start date (YYYY-MM-DD):
```

Then enter an end date:

```text
Enter the end date (YYYY-MM-DD):
```

Example:

```text
Enter the start date (YYYY-MM-DD): 2026-01-01
Enter the end date (YYYY-MM-DD): 2026-01-07
```

The program retrieves Near-Earth Object data from NASA and analyzes the results using Pandas.

### View Top 5 Largest

After searching for asteroid data, select:

```text
2
```

The program displays a Matplotlib bar chart showing the top 5 largest asteroids from the searched date range.

> ℹ️ Asteroid data must be loaded using option 1 before the visualization can be displayed.

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

## 📈 Data Visualization

Version 3.0 introduced **Matplotlib** for visualizing the analyzed asteroid data.

The current visualization allows the user to view the **top 5 largest asteroids** in a bar chart.

The chart displays:

* Asteroid names
* Estimated maximum diameter
* Formatted data labels
* Rotated x-axis labels for improved readability

### Visualization Menu

The visualization feature is accessed through the CLI.

Users must first search for asteroid data before viewing the available visualization.

---

## 🖥️ Example Output

Example results from a previous search:

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
```

### Top 5 Largest Asteroids

```text
================================
      TOP 5 LARGEST ASTEROIDS
================================

1. 418265 (2008 EA32) - 2,992.54 meters
2. 26663 (2000 XK47) - 1,412.67 meters
3. 620103 (2018 LC3) - 1,042.41 meters
4. (2018 LC3) - 1,032.86 meters
5. 367390 (2008 MB5) - 924.78 meters

================================
```

### Hazardous Asteroids by Date

```text
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
* Creating data visualizations
* Using Matplotlib
* Creating bar charts
* Formatting chart labels
* Improving chart readability
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

---

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

### Version 3.0 — Data Visualization

The third version introduced data visualization using Matplotlib.

* Added Matplotlib
* Added Top 5 largest asteroid bar chart
* Added formatted chart data labels
* Added rotated x-axis labels for readability
* Added visualization option to the CLI
* Added Matplotlib to project dependencies
* Improved graphical presentation of analyzed data
* Visualizes the top 5 largest asteroids
* Displays asteroid names and estimated diameters

---

## 🔮 Future Improvements

Possible improvements for future versions:

* 🖥️ Add a Pandas-based CLI data viewer
* 📊 Allow users to select different visualization types
* 📈 Add histogram visualizations
* 📉 Add scatter plot visualizations
* 📅 Add line charts for asteroid activity by date
* 📊 Add an option to display all visualizations
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

**V1 → API Integration**

**V2 → Pandas & Data Analysis**

**V3 → Data Visualization with Matplotlib**

**V4 → Data Exploration & Advanced CLI**

**Future → More advanced data science**

---

## 👨‍💻 Author

Created by **TheCreatorJJ** as a Python learning project.

⭐ If you find the project interesting, feel free to explore the code and follow its development.