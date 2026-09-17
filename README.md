# NASA Near-Earth Object (NEO) Tracker

A Python CLI tool that retrieves, analyzes, and displays Near-Earth Object (NEO) data using NASA's NeoWs API.

## Features

* Search for asteroids using a custom date range
* Display asteroid names and estimated diameters
* Identify potentially hazardous asteroids
* Find the largest asteroid in the selected date range
* Find the smallest asteroid in the selected date range
* Find the closest asteroid based on miss distance
* Display the closest approach date
* Calculate the average asteroid diameter
* Calculate the percentage of potentially hazardous asteroids
* Display the top 5 largest asteroids
* Group potentially hazardous asteroids by date
* Validate date formats and date ranges
* Handle API request errors
* Display results through a simple command-line interface
* ASCII art splash screen and improved CLI layout

## Technologies Used

* Python
* NASA NeoWs API
* Requests
* Pandas
* python-dotenv

Pandas is used to organize the API data into a DataFrame and perform analysis such as filtering, sorting, grouping, and calculating statistics.

## Requirements

* Python 3.x
* A NASA API key

## Installation

Clone the repository:

```bash
git clone https://github.com/TheCreatorJJ/Nasa-asteroid-tracker.git
```

Go into the project folder:

```bash
cd Nasa-asteroid-tracker
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

This project uses a NASA API key to access the NeoWs API.

Create a file named `.env` in the project folder:

```env
NASA_API_KEY=your_nasa_api_key_here
```

**Do not upload your `.env` file to GitHub.**

The `.env` file is excluded using `.gitignore`.

## Usage

Run the program:

```bash
python main.py
```

The program will display a menu where you can search for asteroid data or exit the program.

Enter dates using:

```text
YYYY-MM-DD
```

For example:

```text
Enter the start date (YYYY-MM-DD): 2026-01-01

Enter the end date (YYYY-MM-DD): 2026-01-07
```

The program then retrieves and analyzes the Near-Earth Objects found during the selected date range.

## Analysis

The program uses Pandas to organize the retrieved asteroid data and perform several analysis operations.

Examples include:

* Finding the largest and smallest asteroids
* Finding the closest asteroid approach
* Calculating the average diameter
* Counting potentially hazardous asteroids
* Calculating the percentage of potentially hazardous asteroids
* Sorting asteroids by estimated diameter
* Displaying the top 5 largest asteroids
* Grouping potentially hazardous asteroids by approach date

Pandas provides functionality for sorting DataFrames and grouping data for calculations and counts.

## Example Output

```text
================================
        ASTEROID SUMMARY
================================
Total Asteroids: 36
Potentially Hazardous: 7
Hazardous Percentage: 19.44%
Largest Asteroid: 418265 (2008 EA32)
Diameter: 2992.54 meters
Smallest Asteroid: (2018 TV5)
Diameter: 7.48 meters
Closest Asteroid: (2014 AF16)
Miss Distance: 3,071,593.48 km
Approach Date: 2026-01-04
Average Diameter: 285.73 meters

================================
      TOP 5 LARGEST ASTEROIDS
================================
1. 418265 (2008 EA32) - 2992.54 meters
2. 26663 (2000 XK47) - 1412.67 meters
3. 620103 (2018 LC3) - 1042.41 meters
4. (2018 LC3) - 1032.86 meters
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

The values above are example results and may change depending on the selected date range and NASA's current data.

## What I Learned

This project was built as part of my Python learning journey. It helped me practice:

* Working with APIs
* Making HTTP requests with `requests`
* Using environment variables
* Working with JSON data
* Working with dictionaries and lists
* Using loops and conditional statements
* Handling errors with `try` and `except`
* Working with dates using `datetime`
* Creating functions
* Building a CLI application
* Creating and working with Pandas DataFrames
* Filtering DataFrame data
* Sorting data with Pandas
* Finding maximum and minimum values
* Calculating averages
* Grouping and counting data
* Using Git and GitHub

## Data Source

The asteroid data comes from NASA's Near Earth Object Web Service (NeoWs) API.

NASA API:

https://api.nasa.gov/

## Project Versions

### Version 1

* NASA NeoWs API integration
* Custom date-range asteroid search
* Basic asteroid information
* Hazardous asteroid identification
* Largest asteroid detection
* Closest approach detection
* Date validation
* API error handling
* Basic CLI

### Version 2

* Added Pandas for data analysis
* Added smallest asteroid detection
* Added average diameter calculation
* Added hazardous asteroid percentage
* Added top 5 largest asteroid ranking
* Added hazardous asteroids grouped by date
* Improved number formatting
* Improved CLI presentation
* Added ASCII art
* Updated project documentation

## Future Improvements

Possible improvements for future versions:

* Add data visualization with Matplotlib
* Add CSV export
* Add more detailed asteroid filtering
* Add additional asteroid statistics
* Improve the CLI interface
* Create visual charts for asteroid data
* Eventually build a graphical or web-based dashboard

## Author

Created by **TheCreatorJJ** as a Python learning project.
