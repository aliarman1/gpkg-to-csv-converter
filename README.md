
# GeoPackage to CSV Converter

This repository contains a Python script to convert GeoPackage (.gpkg) files to CSV format. The script searches for all .gpkg files in the specified source directory and its subdirectories, and converts them into CSV files in the specified destination directory.

## Features

- Automatically searches for .gpkg files in the source directory and its subdirectories.
- Converts each .gpkg file to a CSV file.
- Displays progress with a progress bar.
- Handles errors gracefully and prints error messages for problematic files.

## Requirements

- Python 3.6 or higher
- `geopandas` library
- `tqdm` library

You can install the required libraries using pip:

```sh
pip install geopandas tqdm
```

## Usage

1. Clone the repository:

```sh
git clone https://github.com/aliarman1/gpkg-to-csv-converter.git
cd gpkg-to-csv-converter
```

2. Place your .gpkg files in the directory you want to use as the source directory.

3. Run the script:

```sh
python convert_gpkg.py
```

By default, the script uses the current working directory as the source directory and creates an `output` directory within it for the CSV files.

## Script Details

The script `convert_gpkg.py` contains the following main function:

```python
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
```

The script sets the base path as the current working directory and creates an `output` directory for the CSV files:

```python
# Base path is the current working directory
base_path = os.getcwd()

# Destination directory (output directory within the current working directory)
dest_directory = os.path.join(base_path, 'output')

print(f"Base path: {base_path}")
print(f"Destination path: {dest_directory}")

# Convert .gpkg files in the current directory and all subdirectories
convert_gpkg_to_csv(base_path, dest_directory)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [Ali Arman](https://github.com/aliarman1).
