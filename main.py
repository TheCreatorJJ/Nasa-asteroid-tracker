import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from art import ASCII_ART
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
    asteroid_rows = []  #we are going to put the asteroid data in list of rows here

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

 
    for date in data["near_earth_objects"]:
         for asteroid in data["near_earth_objects"][date]:

            asteroid_row = {
                "Name" : asteroid['name'],
                "Diameter" : float(asteroid['estimated_diameter']['meters']['estimated_diameter_max']),
                "Hazardous" : asteroid['is_potentially_hazardous_asteroid'],
                "Miss Distance" : float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                "Date" : asteroid['close_approach_data'][0]['close_approach_date']
            }
            asteroid_rows.append(asteroid_row)

    df = pd.DataFrame(asteroid_rows)

    #Analysis
    hazardous_df = df[df["Hazardous"] == True]
    hazardous_by_date = hazardous_df.groupby("Date").size()

    largest_index = df["Diameter"].idxmax()
    largest_diameter = df["Diameter"].max()

    smallest_index = df["Diameter"].idxmin()
    smallest_diameter = df["Diameter"].min()

    closest_index = df["Miss Distance"].idxmin()
    closest_distance = df["Miss Distance"].min()

    total_asteroids = df.shape[0]

    hazardous_count = hazardous_df.shape[0]
    hazardous_percentage = (hazardous_count / total_asteroids) * 100

    sorted_df = df.sort_values("Diameter", ascending=False)
    
    top_5 = sorted_df.head()

    average_diameter = df["Diameter"].mean()

    

    
    #DISPLAY
    print()
    print("================================")
    print("        ASTEROID SUMMARY        ")
    print("================================")

    print(f"Total Asteroids: {total_asteroids}")
    print(f"Potentially Hazardous: {hazardous_count}")
    print(f"Hazardous Percentage: {hazardous_percentage:,.2f}%")

    print()

    print(f"Largest Asteroid: {df.loc[largest_index, 'Name']}")
    print(f"Diameter: {largest_diameter:,.2f} meters")

    print()

    print(f"Smallest Asteroid: {df.loc[smallest_index, 'Name' ]}")
    print(f"Diameter: {smallest_diameter:,.2f} meters")

    print()

    print(f"Closest Asteroid: {df.loc[closest_index, 'Name']}")
    print(f"Miss Distance: {closest_distance:,.2f} km")
    print(f"Approach Date: {df.loc[closest_index, 'Date']}")

    print()

    print(f"Average Diameter: {average_diameter:,.2f} meters")

    print("================================")

    print("================================")
    print("    TOP 5 LARGEST ASTEROID      ")
    print("================================")

    for number, (index, asteroid) in enumerate(top_5.iterrows(), start=1):
        print(f"{number}. {asteroid['Name']} - {asteroid['Diameter']:,.2f} meters")

    print("================================")
    print("       HAZARDOUS BY DATE        ")
    print("================================")

    for date, count in hazardous_by_date.items():
        print(f"{date}: {count}")


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

    return top_5

#CHART SECTION
def show_top_5_chart(top_5):
    bars = plt.bar(top_5["Name"], top_5["Diameter"])
    
    plt.xticks(rotation=40, ha="right")
    plt.bar_label(bars, fmt="{:,.2f} m ", padding=3)
    
    plt.title("Top 5 Largest Asteroid")
    plt.xlabel("Asteroid Names")
    plt.ylabel("Diameters in Meters")

    plt.tight_layout
    plt.show()
    plt.close()
    
    
top_5_data = None 
#CLI MENU

while True:

    print()
    print(ASCII_ART)
    print()
    print("======================================")
    print("        NASA NEO TRACKER V3.0         ")
    print(" Near-Earth Object (NEO) Data Analzyer")
    print("======================================")
    print()
    print("1. Search asteroids")
    print("2. Show top 5 Largest")
    print("3. Exit")
    print()
    print("Note: Search Asteroid first to use function 2")
    print("================================")


    choice = input("Choose and option:")

    if choice == "1":
        top_5_data = search_asteroids()

    elif choice == "2":
        if top_5_data is None:
            print()
            print("No asteroid Loaded")
            print("Please use option 1 first")
        else:
            show_top_5_chart(top_5_data)
            

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")