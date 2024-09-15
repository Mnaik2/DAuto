# filename: process_results_data.py
import pandas as pd
import os

# Load the entire sheet to verify column headers if columns are not as expected
results_path = os.path.join('HackMIT2024', 'results', 'Results_Not_Formated.xlsx')

# Load the spreadsheet to check headers and print them for verification
results_df_initial = pd.read_excel(results_path)
print("Available columns in Results_Not_Formated.xlsx: ", results_df_initial.columns)

# Review the column names from the printed output and update the script accordingly
# Assuming other necessary columns for processing

# Adjusted `usecols` list based on checked headers
# Replace these with the actual column names if they differ
usecols = [
    # Ensure these columns reflect actual headers in the results Excel sheet
    'Record Type', 'Group Number', 'Division', 'Insured I.D.', 'Member Number', 
    'Person Code', 'Relationship', 'Last Name', 'First Name',
    # Exclude or adjust 'Middle Initial' if it does not exist
    'Date of Birth', 'Gender', 'Address 1', 'Address 2', 'SSN', 
    'Effective Date', 'Term Date'
]

# Load the adjusted columns
results_df = pd.read_excel(results_path, usecols=usecols)

# Now, step 4 from the previous script is applicable, adjust further as necessary
# Assuming continuation for the next preprocessing and combining steps

# Print the first few rows for quick verification
print(results_df.head())

# Load and handle other operations as previously specified (steps 3 to 6)
# ...

# Save the new combined dataset and output
output_path = os.path.join('FirstOutput', 'first_fill.xlsx')
os.makedirs('FirstOutput', exist_ok=True)
results_df.to_excel(output_path, index=False)

# Verify the output
print("Data processing complete. First few rows of output:")
print(results_df.head())