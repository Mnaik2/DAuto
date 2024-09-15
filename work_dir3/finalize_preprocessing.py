# filename: finalize_preprocessing.py
import pandas as pd
import os

# Dictionary for basic to coded relationship conversion
relationship_to_code = {
    "Insured": "I", "Spouse": "S", "Child": "D", "Father or Mother": "D", "Grandfather or Grandmother": "D", 
    "Grandson or Granddaughter": "D", "Uncle or Aunt": "D", "Nephew or Niece": "D", "Cousin": "D", 
    "Adopted Child": "D", "Foster Child": "D", "Son-in-law or Daughter-in-law": "D", "Brother-in-law or Sister-in-law": "D", 
    "Mother-in-law or Father-in-law": "D", "Brother or Sister": "D", "Ward": "D", "Stepparent": "D", 
    "Stepson or Stepdaughter": "D", "Sponsored Dependent": "D", "Dependent of a Minor Dependent": "D", 
    "Ex-Spouse": "D", "Guardian": "D", "Court Appointed Guardian": "D", "Collateral Dependent": "D", 
    "Life Partner": "D", "Annuitant": "D", "Trustee": "D", "Other Relationship": "D", "Other Relative": "D"
}

# Function to format date to YYYYMMDD
def format_date(date):
    return date.strftime('%Y%m%d') if not pd.isna(date) else ""

# Load the preprocessed data
input_path = os.path.join('PrePreprocessed', 'prepped.xlsx')
final_df = pd.read_excel(input_path)

# Convert and format necessary columns
final_df['Relationship'] = final_df['Relationship'].map(relationship_to_code)
final_df['Birth_Date'] = pd.to_datetime(final_df['Birth_Date']).apply(format_date)
final_df['Date_Enrolled'] = pd.to_datetime(final_df['Date_Enrolled']).apply(format_date)
final_df['Disenroll_Date'] = pd.to_datetime(final_df['Disenroll_Date']).apply(format_date)

# Save the final preprocessed dataset
final_output_path = os.path.join('PrePreprocessed', 'finished.xlsx')
final_df.to_excel(final_output_path, index=False)

# Print summary of the first few rows
print(final_df.head())

print("\nFinal dataset preprocessing complete. 'finished.xlsx' saved in 'PrePreprocessed'.")