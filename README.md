# NASA Near-Earth Object (NEO) Tracker

A Python CLI tool that retrieves and analyzes Near-Earth Object (NEO) data using NASA's NeoWs API.

## Features

* Search for asteroids using a custom date range
* Display asteroid names and estimated diameters
* Identify potentially hazardous asteroids
* Find the largest asteroid in the selected date range
* Find the closest asteroid based on miss distance
* Display the closest approach date
* Validate date formats and date ranges
* Handle API request errors
* Simple command-line interface

## Technologies Used

* Python
* NASA NeoWs API
* Requests
* python-dotenv

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

Do **not** upload your `.env` file to GitHub.

The `.env` file is excluded using `.gitignore`.

## Usage

Run the program:

```bash
python main.py
```

The program will display a menu:

```text
================================
NASA Near-Earth Object (NEO) Data
================================
1. Search asteroids
2. Exit
================================
```

Choose `1` to search for asteroid data.

Enter dates using:

```text
YYYY-MM-DD
```

For example:

```text
Enter the start date (YYYY-MM-DD): 2026-01-01
Enter the end date (YYYY-MM-DD): 2026-01-07
```

The program then displays information about the asteroids found during the selected date range.

## Example

```text
================================
Date: 2026-01-01
--------------------
Name: (Example Asteroid)
Is Potentially Hazardous: False
Estimated Diameter (MIN): 123.45
Estimated Diameter (MAX): 276.89
Miss Distance (Kilometers): 5,123,456.78
```

At the end of the search, the program displays statistics such as:

```text
================================
Total asteroids: 33
Total potentially hazardous asteroids: 4
Largest asteroid diameter: 648.69
Largest asteroid name: (Example Asteroid)
Closest asteroid distance: 8,907,846.53
Closest asteroid name: (Example Asteroid)
Closest approach date: 2026-01-02
```

The example values above are for demonstration purposes.

## What I Learned

This project was built as part of my Python learning journey. It helped me practice:

* Working with APIs
* Making HTTP requests with `requests`
* Using environment variables
* Working with JSON data
* Using loops and conditional statements
* Handling errors with `try` and `except`
* Working with dates using `datetime`
* Creating functions
* Building a CLI application
* Using Git and GitHub

## Data Source

The asteroid data comes from NASA's Near Earth Object Web Service (NeoWs) API.

NASA API:
https://api.nasa.gov/

## Future Improvements

Possible improvements for future versions:

* Add sorting and filtering options
* Add a more detailed asteroid search
* Add data visualization
* Add CSV export
* Add more statistics
* Improve the CLI interface

## Author

Created by **TheCreatorJJ** as a Python learning project.
