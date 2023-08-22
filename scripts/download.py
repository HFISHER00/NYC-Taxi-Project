import os
import shutil
import urllib.request
from urllib.request import urlretrieve

# Download Yellow Taxi Data - Edited from Tutorial notebooks
# Define the range of years
START_YEAR = 2016
END_YEAR = 2019
MONTH_SEGMENT = 3

# Create a list to hold the URLs
download_urls = []

# This is the URL template as of 07/2023
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

# Data output directory is `data/raw`
tlc_output_dir = "../data/landing/yellow_taxi"

# Check if the `raw` directory exists. If not, create it.
os.makedirs(tlc_output_dir, exist_ok=True)

# Generate download URLs for yellow taxi data between 2016 and 2019
for year in range(START_YEAR, END_YEAR + 1):
    for month in range(1, 13):
        month_str = str(month).zfill(2)  # 0-fill i.e., 1 -> 01, 2 -> 02, etc
        url = f'{URL_TEMPLATE}{year}-{month_str}.parquet'
        download_urls.append((url, year, month_str))

# Download the yellow taxi data for each URL
for url, year, month_str in download_urls:
    print(f"Begin year {year}, month {month_str}")
    output_dir = f"{tlc_output_dir}/yellow_tripdata_{year}-{month_str}.parquet"
    
    try:
        # Download the file
        urlretrieve(url, output_dir) 
        print(f"Completed year {year}, month {month_str}")
    except Exception as e:
        print(f"Error while downloading year {year}, month {month_str}: {e}")
        
# Then organise yellow taxis into folders for every 3 months
# Source directory containing the downloaded Parquet files
source_dir = "../data/landing/yellow_taxi"

# Destination directory to organize Parquet files by segments
destination_base_dir = "../data/landing/yellow_taxi"

# Check if the destination base directory exists. If not, create it.
os.makedirs(destination_base_dir, exist_ok=True)

# Organize the Parquet files into separate folders
for year in range(2016, 2020):  # 2016 to 2019
    for start_month in range(1, 13, MONTH_SEGMENT):  # 1, 4, 7, 10 for each segment
        end_month = start_month + MONTH_SEGMENT
        end_month = min(end_month, 13)  # Limit to 12
        
        start_month_str = str(start_month).zfill(2)
        end_month_str = str(end_month - 1).zfill(2)
        
        destination_folder = f"{destination_base_dir}/{year}_{start_month_str}-{end_month_str}"
        
        # Create the destination folder
        os.makedirs(destination_folder, exist_ok=True)
        
        # Move Parquet files to the destination folder
        for month in range(start_month, end_month):
            month_str = str(month).zfill(2)
            source_file = f"{source_dir}/yellow_tripdata_{year}-{month_str}.parquet"
            destination_file = f"{destination_folder}/yellow_tripdata_{year}-{month_str}.parquet"
            shutil.move(source_file, destination_file)
        
        print(f"Organized year {year}, months {start_month_str}-{end_month_str}")

print("Organizing Parquet files complete.")

# Download shooting data - 
# Note this only downloads 1000 rows of the data so I manually downloaded the full dataset. The full dataset has been included in the Git repo
# I spoke to my Tutor (Lucas Fern) and he said this was ok.
# URL of the data you want to download 
url = ('https://data.cityofnewyork.us/resource/833y-fsy8.csv?$query=SELECT%0A'
       '%20%20%60incident_key%60%2C%0A%20%20%60occur_date%60%2C%0A'
       '%20%20%60occur_time%60%2C%0A%20%20%60boro%60%2C%0A'
       '%20%20%60loc_of_occur_desc%60%2C%0A%20%20%60precinct%60%2C%0A'
       '%20%20%60jurisdiction_code%60%2C%0A%20%20%60loc_classfctn_desc%60%2C%0A'
       '%20%20%60location_desc%60%2C%0A%20%20%60statistical_murder_flag%60%2C%0A'
       '%20%20%60perp_age_group%60%2C%0A%20%20%60perp_sex%60%2C%0A'
       '%20%20%60perp_race%60%2C%0A%20%20%60vic_age_group%60%2C%0A'
       '%20%20%60vic_sex%60%2C%0A%20%20%60vic_race%60%2C%0A'
       '%20%20%60x_coord_cd%60%2C%0A%20%20%60y_coord_cd%60%2C%0A'
       '%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A'
       '%20%20%60geocoded_column%60%2C%0A%20%20%60%3A%40computed_region_yeji_bk3q%60%2C%0A'
       '%20%20%60%3A%40computed_region_92fq_4b7q%60%2C%0A'
       '%20%20%60%3A%40computed_region_sbqj_enih%60%2C%0A'
       '%20%20%60%3A%40computed_region_efsh_h5xi%60%2C%0A'
       '%20%20%60%3A%40computed_region_f5dn_yrer%60')

# Download the data
urllib.request.urlretrieve(url, '../data/landing/shooting_data_1000.csv')
print("Data downloaded successfully.")
 


