# Multi-Clipboard Storage Script

## Description
This Python script allows users to store multiple clipboard entries and retrieve them later using a key. It utilizes the `clipboard` module to interact with the system clipboard and `json` for data storage.

## Features
- Save clipboard content with a unique key
- Load clipboard content using a saved key
- List all stored clipboard entries

## Requirements
Ensure you have Python installed on your system. Additionally, install the required dependencies using:
```sh
pip install clipboard
```

## Usage
Run the script with a command-line argument specifying the action you want to perform.

### Saving Clipboard Content
```sh
python script.py save
```
- The script will prompt you to enter a key.
- The current clipboard content will be saved under the provided key.

### Loading Clipboard Content
```sh
python script.py load
```
- The script will prompt you to enter a key.
- If the key exists, the associated content will be copied to the clipboard.

### Listing All Saved Entries
```sh
python script.py list
```
- Displays all saved keys and their corresponding clipboard contents.

## Notes
- Data is stored in `clipboard.json`.
- Ensure the script has the necessary permissions to read and write the JSON file.

## Issues & Improvements
- Handle missing `clipboard.json` file gracefully.
- Implement better error handling for invalid inputs.
- Encrypt clipboard data for added security.

## License
This script is open-source. Feel free to modify and distribute it.

