# Written by Chat GPT, thanks

import csv
import pandas as pd

def convert_text_to_csv(input_file, output_file):
    """
    Convert a text file to a CSV where the words are lined up in columns.
    Missing words in any line are replaced with NaN.
    
    Args:
    input_file (str): Path to the input text file.
    output_file (str): Path to the output CSV file.
    """
    
    # Read the input text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize a set to hold all unique words in the text file
    all_words = set()

    # Process each line to collect unique words
    for line in lines:
        # Tokenize the line into words (split by whitespace)
        words = line.strip().split()
        all_words.update(words)  # Add words to the set (duplicates are automatically handled)

    # Convert all_words to a sorted list to ensure consistent column order
    all_words = sorted(all_words)

    # Prepare the rows for the CSV
    csv_data = []

    # For each line in the input file, create a row with words in the proper columns
    for line in lines:
        words_in_line = line.strip().split()  # Tokenize the line into words
        row = []

        # Check for each word in all_words if it's in the current line
        for word in all_words:
            if word in words_in_line:
                row.append(word)
            else:
                row.append("NaN")  # If the word is not found, add "NaN"

        csv_data.append(row)

    # Write the CSV data to the output file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(all_words)  # Write the header row (words as columns)
        writer.writerows(csv_data)  # Write the data rows

    print(f"Data successfully saved to {output_file}")

def extract_columns_with_custom_headers(input_csv, output_csv, columns_to_extract, new_headers):
    """
    Extract specific columns from a CSV and add custom headers.
    
    Args:
    input_csv (str): Path to the input CSV file.
    output_csv (str): Path to the output CSV file.
    columns_to_extract (list): List of column indices or column names to extract.
    new_headers (list): List of custom headers for the extracted columns.
    """
    
    # Read the input CSV file
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)
    
    # Check if the number of custom headers matches the number of columns to extract
    if len(columns_to_extract) != len(new_headers):
        raise ValueError("The number of columns to extract and the number of custom headers must match.")
    
    # Get the header row (first row in the CSV)
    original_headers = rows[0]

    # Extract the indices of the columns to be extracted
    if isinstance(columns_to_extract[0], str):
        # If columns are provided as names, convert them to indices
        column_indices = [original_headers.index(col) for col in columns_to_extract]
    else:
        # If columns are provided as indices, use them directly
        column_indices = columns_to_extract
    
    # Create a new list to store the extracted rows
    extracted_data = []

    # Extract the data for each row based on the column indices
    for row in rows[1:]:  # Skip the header row
        extracted_row = [row[index] for index in column_indices]
        extracted_data.append(extracted_row)
    
    # Write the extracted data to the output CSV file with new headers
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_headers)  # Write the custom headers
        writer.writerows(extracted_data)  # Write the data rows

    print(f"Extracted data successfully saved to {output_csv}")


# Example usage:
# Provide the path to the text file and the output CSV file
input_file = 'predictions/txtfiles/pdr_test'
output_file = 'predictions/txtfiles/pdr_test.csv'

convert_text_to_csv(input_file, output_file)

# Example usage:
# Provide the path to the input CSV, output CSV, columns to extract, and custom headers
input_csv = 'predictions/txtfiles/pdr_test.csv'  # Path to the input CSV
output_csv = 'predications/csvfiles/pdr_test.csv'  # Path to the output CSV

# Columns to extract: specify by either column index (0-based) or column name
columns_to_extract = [4, 7, 9, 11, 13]  # Example: Extract 'Name' and 'Age' columns

# Custom headers: the new headers for the extracted columns
new_headers = ['Frame Number', 'Num Airspeed Detected', 'Num Altitude Detected ', 'Num RPM Detected', 'Time (ms)']

# Call the function
extract_columns_with_custom_headers(input_csv, output_csv, columns_to_extract, new_headers)

# https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file
c = pd.read_csv(output_csv)
c['Time(s)'] = c['Time (ms)'] / 1000
c.to_csv(output_csv, index=False)
