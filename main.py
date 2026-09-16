import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("NASA_API_KEY")  # Get the NASA API key from environment variables

base_url = "https://api.nasa.gov/neo/rest/v1/feed"

def get_neo_data(start_date, end_date, api_key):

    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": api_key,
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def search_asteroids():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        exit()

    #this validate the date range to be between 0 and 7 days, if not it will print an error message and exit the program.
    date_diff = (end - start).days
    if date_diff < 0 or date_diff > 7:
        print("Date range must be between 0 and 7 days.")
        exit()

   
    #Get NASA DATA
    try:
        data = get_neo_data(start_date, end_date, api_key)

    except requests.RequestException as e:
        print(f"Error fetching NEO data: {e}")
        exit()

    #Statistics
    total_asteroids = 0
    hazardous_asteroids = 0

    largest_diameter = 0
    largest_asteroid_name = ""

    #float("inf") means infinity, which is a very large number that any real number will be smaller than.
    closest_distance = float('inf') 
    closest_asteroid_name = ""
    closest_approach_date = ""


    #Loop Through Dates
    for date in data["near_earth_objects"]:
        
        print("================================")
        print(f"Date: {date}")

        for asteroid in data["near_earth_objects"][date]:
            
            print("--------------------")

            print(f"Name: {asteroid['name']}")

            print(f"Is Potentially Hazardous: {asteroid['is_potentially_hazardous_asteroid']}") 

            print(f"Estimated Diameter (MIN): {float(asteroid['estimated_diameter']['meters']['estimated_diameter_min']):,.2f}")

            print(f"Estimated Diameter (MAX): {float(asteroid['estimated_diameter']['meters']['estimated_diameter_max']):,.2f}")

            print(f"Miss Distance (Kilometers): {float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']):,.2f}")


            #Find the Largest Asteroid and Closest Asteroid
            current_diameter = asteroid['estimated_diameter']['meters']['estimated_diameter_max']

            if current_diameter > largest_diameter:
                    largest_diameter = current_diameter
                    largest_asteroid_name = asteroid['name']

            #Count Asteroids
            total_asteroids += 1

            #Find the Closest Asteroid
            current_distance = float(
                asteroid['close_approach_data'][0]['miss_distance']['kilometers']
                )
            
            if current_distance < closest_distance:
                    closest_distance = current_distance
                    closest_asteroid_name = asteroid['name']
                    closest_approach_date = asteroid['close_approach_data'][0]['close_approach_date']

            #Count Hazardous Asteroids
            if asteroid['is_potentially_hazardous_asteroid']:
                hazardous_asteroids += 1


    #Display Statistics
    print("================================")

    print(f"Total asteroids: {total_asteroids}")

    print(f"Total potentially hazardous asteroids: {hazardous_asteroids}")

    print(f"Largest asteroid diameter: {float(largest_diameter):,.2f}")

    print(f"Largest asteroid name: {largest_asteroid_name}")

    print(f"Closest asteroid distance: {float(closest_distance):,.2f}")

    print(f"Closest asteroid name: {closest_asteroid_name}")

    print(f"Closest approach date: {closest_approach_date}")

#CLI MENU

while True:

    print()
    print("================================")
    print("NASA Near-Earth Object (NEO) Data")
    print("================================")
    print("1. Search asteroids")
    print("2. Exit")
    print("================================")


    choice = input("choose and option:")

    if choice == "1":
        search_asteroids()

    elif choice == "2":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")