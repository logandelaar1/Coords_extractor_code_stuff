import os
import re

# Define regex patterns to extract latitude and longitude
lat_lon_regex = re.compile(r'\$GPGGA,.*?,(\d{2})(\d{2}\.\d+),([NS]),(\d{3})(\d{2}\.\d+),([EW]),')
timestamp_regex = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) -')

def parse_lat_long(match):
    lat_deg = match.group(1)
    lat_min = match.group(2)
    lat_dir = match.group(3)
    lon_deg = match.group(4)
    lon_min = match.group(5)
    lon_dir = match.group(6)
    
    lat = float(lat_deg) + float(lat_min) / 60.0
    if lat_dir == 'S':
        lat = -lat
    
    lon = float(lon_deg) + float(lon_min) / 60.0
    if lon_dir == 'W':
        lon = -lon
    
    return lat, lon

def process_file(input_folder, output_folder, filename):
    input_file_path = os.path.join(input_folder, filename)
    
    output_filename = f'LAT_LON_{filename}'
    output_file_path = os.path.join(output_folder, output_filename)
    
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            timestamp_match = timestamp_regex.match(line)
            if timestamp_match:
                timestamp = timestamp_match.group(1).replace(' ', '__').replace('-', '/')
            
            lat_lon_match = lat_lon_regex.search(line)
            if lat_lon_match:
                latitude, longitude = parse_lat_long(lat_lon_match)
                outfile.write(f'Timestamp: {timestamp}, Latitude: {latitude}, Longitude: {longitude}\n')
                print(f"Writing data to {output_filename}: Timestamp: {timestamp}, Latitude: {latitude}, Longitude: {longitude}")

def process_folder(input_folder):
    output_folder = os.path.join(input_folder, 'Parsed_Files')
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            print(f"Processing file {filename}...")
            process_file(input_folder, output_folder, filename)
    
    print(f"Parsing complete. Data saved to folder: {output_folder}")

# Example usage:
input_folder = '/Users/logandelaar/Desktop/USMA/HIGH VALUE TARGET/High Value Target 3 copy'  # Specify the folder containing the .txt files
process_folder(input_folder)
