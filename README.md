
# GeoPackage to CSV Converter

This repository contains a Python script for converting GeoPackage (.gpkg) files to CSV format. The script recursively searches for .gpkg files in specified directories and converts them to CSV files.

## Features

- Recursively searches for .gpkg files in specified directories.
- Converts each .gpkg file to a CSV file.
- Uses a progress bar to show the conversion progress.
- Handles errors gracefully and provides informative messages.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `geopandas`
  - `tqdm`

You can install the required packages using pip:

```sh
pip install geopandas tqdm
```

## Usage

1. Clone the repository:

```sh
git clone https://github.com/aliarman1/gpkg-to-csv-converter.git
cd gpkg-to-csv-converter
```

2. Place your GeoPackage (.gpkg) files in the appropriate directories (e.g., `citycorporation`, `district`, etc.) within the base directory.

3. Run the script:

```sh
python convert_gpkg.py
```

The script will search for .gpkg files in the specified directories, convert them to CSV format, and save the CSV files in the `output` directory within the base directory.

## Script Details

The script `convert_gpkg.py` performs the following steps:

1. Collects all .gpkg files from the specified directories.
2. Creates the output directory if it does not exist.
3. Iterates over the .gpkg files, converts each to a CSV file, and saves it in the output directory.
4. Provides informative messages about the conversion progress and any errors encountered.

## Example

```sh
Base path: /path/to/your/repository
Destination path: /path/to/your/repository/output
Processing directory: /path/to/your/repository/citycorporation
Converting .gpkg files: 100%|████████████████████████████████████████████████████| 3/3 [00:05<00:00,  1.01s/it]
Converted /path/to/your/repository/citycorporation/example.gpkg to /path/to/your/repository/output/example.csv
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
