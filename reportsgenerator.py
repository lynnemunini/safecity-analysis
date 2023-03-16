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
    'south': -1.364849,
    'east': 36.996153,
    'west': 36.654915
}

# Define the crime categories
crime_categories = ['theft', 'burglary', 'assault', 'vandalism', 'fraud']

# Define the timeframe for the crime reports (1 year)
start_date = datetime.date.today() - datetime.timedelta(days=365)
end_date = datetime.date.today()

# Generate fake crime reports and write to a CSV file
with open('fake_crime_reports.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Latitude', 'Longitude', 'Location Name', 'Date'])

    for i in range(100000):  # Generate 100000 fake reports
        # Generate a random crime category and location
        category = random.choice(crime_categories)
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

        # Generate a random date within the specified timeframe
        date = faker.date_between(start_date=start_date, end_date=end_date)

        # Write the report to the CSV file
        writer.writerow([category, location.latitude, location.longitude, location.address, date])