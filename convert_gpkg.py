import os
import geopandas as gpd
from tqdm import tqdm

def convert_gpkg_to_csv(src_directory, dest_directory):
    # Collect all .gpkg files
    gpkg_files = []
    for root, _, files in os.walk(src_directory):
        for file in files:
            if file.endswith('.gpkg'):
                gpkg_files.append(os.path.join(root, file))
    
    if not gpkg_files:
        print(f"No .gpkg files found in {src_directory}")
        return
    
    # Create output directory if it doesn't exist
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    
    # Iterate over the .gpkg files with a progress bar
    for gpkg_path in tqdm(gpkg_files, desc="Converting .gpkg files"):
        try:
            # Define the output CSV file path in the destination directory
            filename = os.path.splitext(os.path.basename(gpkg_path))[0] + '.csv'
            csv_path = os.path.join(dest_directory, filename)
            
            # Load the GeoPackage
            gdf = gpd.read_file(gpkg_path)
            
            # Save the GeoDataFrame as a CSV file
            gdf.to_csv(csv_path, index=False)
            print(f"Converted {gpkg_path} to {csv_path}")
        except Exception as e:
            print(f"Error converting {gpkg_path}: {e}")

# List of directories to search for .gpkg files
directories = [
    'citycorporation',
    'district',
    'division',
    'enumerationarea',
    'mauza',
    'municipality',
    'union',
    'upazila',
    'village'
]

# Base path where these directories are located (current working directory)
base_path = os.getcwd()

# Destination directory (output directory within the current working directory)
dest_directory = os.path.join(base_path, 'output')

print(f"Base path: {base_path}")
print(f"Destination path: {dest_directory}")

# Convert .gpkg files in each directory
for dir_name in directories:
    full_path = os.path.join(base_path, dir_name)
    if os.path.isdir(full_path):
        print(f"Processing directory: {full_path}")
        convert_gpkg_to_csv(full_path, dest_directory)
    else:
        print(f"Directory not found: {full_path}")
