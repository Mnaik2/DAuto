# filename: process_and_match_results.py
import pandas as pd
import os

# Load the data
results_path = os.path.join('HackMIT2024', 'results', 'Results_Not_Formated.xlsx')
finished_path = os.path.join('PrePreprocessed', 'finished.xlsx')

results_df = pd.read_excel(results_path)
finished_df = pd.read_excel(finished_path, usecols=[
    'Subscriber_ID', 'Sex', 'SSN', 'Birth_Date', 'Date_Enrolled', 'Disenroll_Date', 
    'Alternate_ID', 'Last_Name', 'First_Name'
])

# Step 1: Matching and Populating
# Ensure the merge occurs correctly and redefine matched_df
try:
    matched_df = results_df.merge(finished_df, left_on='Member Number', right_on='Alternate_ID', how='left', suffixes=('', '_f'))
except Exception as e:
    print("Error during merging process: ", e)

# Ensure valid columns exist
if 'matched_df' in locals():
    # Filling missing fields for valid columns
    fields_to_fill = {
        'Gender': 'Sex',  # Using the direct column from merged result
        'SSN': 'SSN_f',
        'Effective Date': 'Date_Enrolled',
        'Term Date': 'Disenroll_Date',
        'Last Name': 'Last_Name',
        'Date of Birth': 'Birth_Date'
    }

    for target, source in fields_to_fill.items():
        if source in matched_df.columns:
            matched_df[target] = matched_df[target].fillna(matched_df[source])
        else:
            print(f"Warning: Column {source} expected for filling {target} not found in matched DataFrame.")


    # Step 2: Adding New Entries for unmatched Alternate_ID
    new_entries = finished_df[~finished_df['Alternate_ID'].isin(matched_df['Member Number'])]
    new_entries_df = new_entries.rename(columns={
        'Alternate_ID': 'Member Number',
        'Sex': 'Gender',
        'Date_Enrolled': 'Effective Date',
        'Disenroll_Date': 'Term Date',
        'Last_Name': 'Last Name',
        'Birth_Date': 'Date of Birth'
    })

    required_columns = [column for column in results_df.columns]
    new_entries_df = new_entries_df.reindex(columns=required_columns, fill_value='')

    # Concatenate matched and new entries
    final_df = pd.concat([matched_df, new_entries_df], ignore_index=True)

    # Save the final dataset
    output_path = os.path.join('FirstOutput', 'first_fill.xlsx')
    os.makedirs('FirstOutput', exist_ok=True)
    final_df.to_excel(output_path, index=False)

    # Verify Final Output
    print("First few rows of the final dataset:\n", final_df.head())
else:
    print("The merging process did not result in a valid DataFrame.")