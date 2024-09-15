# filename: preprocess_members.py
import pandas as pd
import os

# Dictionary for relationship conversion
relationship_dict = {
    1: "Insured", 2: "Spouse", 3: "Father or Mother", 4: "Grandfather or Grandmother", 5: "Grandson or Granddaughter", 
    6: "Uncle or Aunt", 7: "Nephew or Niece", 8: "Cousin", 9: "Adopted Child", 10: "Foster Child", 
    11: "Son-in-law or Daughter-in-law", 12: "Brother-in-law or Sister-in-law", 13: "Mother-in-law or Father-in-law", 
    14: "Brother or Sister", 15: "Ward", 16: "Stepparent", 17: "Stepson or Stepdaughter", 18: "Sponsored Dependent", 
    19: "Child", 20: "Dependent of a Minor Dependent", 21: "Ex-Spouse", 22: "Guardian", 
    23: "Court Appointed Guardian", 24: "Collateral Dependent", 25: "Life Partner", 26: "Annuitant", 
    27: "Trustee", 28: "Other Relationship", 29: "Other Relative"
}

# Load data from the excel file
file_path = os.path.join('HackMIT2024', 'inputs', 'MemberData', 'Members.xlsx')
members_df = pd.read_excel(file_path)

# Columns to be retained
columns = [
    'Subscriber_ID', 'Member_Seq', 'Last_Name', 'First_Name', 'Relationship', 'Birth_Date', 
    'Date_Enrolled', 'Disenroll_Date', 'Sex', 'Adult_Child', 'Other_Insurance', 'Adult_Dependent', 
    'Notes', 'Entry_Date', 'Entry_User', 'Update_Date', 'Update_User', 'Alternate_ID', 'VIP_Flag',
    'Pend_Flag', 'Pend_Ex_Code', 'Other_Name', 'Pre_Exist', 'Pre_Exist_End', 'Pre_Exist_Ex_Code', 
    'Student', 'Date_Of_Death', 'Marital_Status', 'Ethnicity_Code', 'Middle_Name', 'Name_Suffix', 
    'Salutation', 'SSN', 'Unique_ID', 'Access_Code', 'Student_End', 'Adult_Dependent_End', 
    'Height', 'Weight', 'Continue_Coverage', 'Continue_Coverage_Ex_Code', 'Continue_Coverage_End_Date',
    'Credible_Coverage', 'Coverage_Type', 'Use_Member_Plan_Year', 'Plan_Year_Frequency', 
    'Plan_Year_Frequency_Type', 'Creditable_Coverage_Start', 'Creditable_Coverage_End', 
    'Initial_Volume_Salary_Pct', 'Initial_Volume', 'Smoker'
]
members_df = members_df[columns]

# Convert Relationship column using the dictionary
members_df['Relationship'] = members_df['Relationship'].map(relationship_dict)

# Save the preprocessed dataset
output_path = os.path.join('PrePreprocessed', 'prepped.xlsx')
members_df.to_excel(output_path, index=False)

print("Initial dataset preprocessing complete. 'prepped.xlsx' saved in 'PrePreprocessed'.")