# filename: enhance_and_process_data.py
import pandas as pd
import os

# Path to the first_fill.xlsx data
first_fill_path = os.path.join('FirstOutput', 'first_fill.xlsx')

# Load the entire sheet to verify columns
first_fill_df_initial = pd.read_excel(first_fill_path)
print("Columns in first_fill.xlsx: ", first_fill_df_initial.columns.tolist())

# Load only available necessary columns
available_columns = [
    'Record Type', 'Group Number', 'Division', 'Insured I.D.', 'Member Number', 
    'Subscriber_ID', 'Person Code', 'Relationship', 'Last Name', 'First Name', 
    'Date of Birth', 'Gender', 'Address 1', 'Address 2', 'Zip Code', 
    'SSN', 'Effective Date', 'Term Date', 'Medical Group', 'City', 'State', 
    'Reserved Xref Member Number', 'Reserved Xref Family Position'
]  # Modify this list based on actual columns present

# Reload data with available columns
first_fill_df = pd.read_excel(first_fill_path, usecols=available_columns)

# Path to Subscribers.csv data
subscribers_path = os.path.join('HackMIT2024', 'inputs', 'MemberData', 'Subscribers.csv')
subscribers_df = pd.read_csv(subscribers_path, usecols=[
    'Subscriber_ID', 'Address', 'Address2', 'Zip_Code'
])

# Merge address information
complete_df = first_fill_df.merge(subscribers_df, on='Subscriber_ID', how='left', suffixes=('', '_sub'))

# Fill missing address information
for index, row in complete_df.iterrows():
    if pd.isna(row['Address 1']):
        complete_df.at[index, 'Address 1'] = row['Address']
    if pd.isna(row['Address 2']):
        complete_df.at[index, 'Address 2'] = row['Address2']
    if pd.isna(row['Zip Code']):
        complete_df.at[index, 'Zip Code'] = row['Zip_Code']

# Handle new entries for unmatched Subscriber_IDs
new_entries = subscribers_df[~subscribers_df['Subscriber_ID'].isin(first_fill_df['Subscriber_ID'])]
new_entries_df = new_entries.rename(columns={
    'Address': 'Address 1',
    'Address2': 'Address 2',
    'Zip_Code': 'Zip Code'
})

new_entries_df['Record Type'] = 23
required_columns = [col for col in first_fill_df.columns]
new_entries_df = new_entries_df.reindex(columns=required_columns, fill_value='')

complete_final_df = pd.concat([complete_df, new_entries_df], ignore_index=True)

# Save the new dataset
output_path = os.path.join('SecondOutput', 'second_fill.xlsx')
os.makedirs('SecondOutput', exist_ok=True)
complete_final_df.to_excel(output_path, index=False)

# Verification
print("First few rows of the final dataset:\n", complete_final_df.head())