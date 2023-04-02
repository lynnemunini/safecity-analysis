from faker import Faker
from geopy.geocoders import Nominatim
import random
import csv
import datetime

faker = Faker()
geolocator = Nominatim(user_agent="crime_report", timeout=10000)

# Define Nairobi's latitude and longitude boundaries
nairobi_bounds = {
    'north': -1.160757,
    'south': -1.450000, # Updated value to include Ongata Rongai's latitude
    'east': 36.996153,
    'west': 36.654915
}

# Define the crime categories
crime_categories = ['theft', 'burglary', 'assault', 'vandalism', 'fraud']

# Define the timeframe for the crime reports (1 year)
start_date = datetime.date.today() - datetime.timedelta(days=365)
end_date = datetime.date.today()

# Define gender categories
gender_categories = ["male", "female"]

# Define age between 18 and 60
age_categories = [i for i in range(18, 61)]

# Suspect's Gender
suspect_gender = ["male", "female"]

# Define demographic categories
demographic_categories = ["poor", "rich", "middle class"]

# Define the weather categories
weather_categories = ["sunny", "rainy", "cloudy", "windy"]


# Generate fake crime reports and write to a CSV file
with open('fake_crime_reports.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Latitude', 'Longitude', 'Location Name', 'Date', "Victim Gender", "Victim Age", "Suspect Gender", "Demographic", "Weather"])

    for i in range(1000):
        # Generate a random and location
        location = geolocator.reverse(
            (random.uniform(nairobi_bounds['south'], nairobi_bounds['north']),
             random.uniform(nairobi_bounds['west'], nairobi_bounds['east']))
        )

        # Ensure the location is within Nairobi's boundaries
        while location.address.find('Nairobi') == -1:
            location = geolocator.reverse(
                (random.uniform(nairobi_bounds['south'], nairobi_bounds['north']),
                 random.uniform(nairobi_bounds['west'], nairobi_bounds['east']))
            )

        
        reports = random.randint(10,30)

        # Generate the reports
        for j in range(reports):
            # Generate a random crime category
            category = random.choice(crime_categories)
            # Generate a random date within the specified timeframe
            date = faker.date_between(start_date=start_date, end_date=end_date)

            # Generate a random gender
            gender = random.choice(gender_categories)

            # Generate a random age
            age = random.choice(age_categories)

            # Generate a random suspect's gender
            suspect = random.choice(suspect_gender)

            # Generate a random demographic
            demographic = random.choice(demographic_categories)

            # Generate a random weather
            weather = random.choice(weather_categories)


            # Write the report to the CSV file
            writer.writerow([category, location.latitude, location.longitude, location.address, date, gender, age, suspect, demographic, weather])