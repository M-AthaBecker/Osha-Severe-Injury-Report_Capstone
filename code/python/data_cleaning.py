"""
OSHA Severe Injury Report – Data Cleaning Script
Author: Mary Becker
Description: Cleaning steps for OSHA severe injury dataset.
"""
------------------------------------------------------------------------------------------------------
## Importing needed libararies to complete analysis 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("All libraries loaded successfully!")
------------------------------------------------------------------------------------------------------
## Loading Dataset 
df = pd.read_csv("data/Severe_Injury_Report_Cleaned.csv")
------------------------------------------------------------------------------------------------------
## Correcting Data types: 
# Changing event date from object to date 
df['Event Date'] = pd.to_datetime(df['Event Date'])

# Maintaining the leading zeros on zip code changing from integar to string
df['Zip'] = df['Zip'].astype(str).str.zfill(5)

# Changing Amputation and Loss of Eye from float to integar and filling blanks with 0
df['Amputation'] = df['Amputation'].fillna(0).astype(int)
df['Loss Of Eye'] = df['Loss Of Eye'].fillna(0).astype(int)

#Confirming the changes 

print("Confirming the data type updates:")
print(df.dtypes)
print()
print("Data type updates confirmed!")
------------------------------------------------------------------------------------------------------
## Employer Name Standardization
# The total number of unique employer names before cleaning
print(f"Unique employer names before cleaning: {df['Employer'].nunique():,}")
print()

# Removing leading and trailing spaces
df['Employer'] = df['Employer'].str.strip()

# Updating name to Proper capitalization
df['Employer'] = df['Employer'].str.title()

# Removing extra spaces between words 
df['Employer'] = df['Employer'].str.replace(r'\s+', ' ', regex=True)

# Common suffixes standardization
suffix_map = {
    r'\bLlc\b': 'LLC',
    r'\bInc\b': 'Inc.',
    r'\bCorp\b': 'Corp.',
    r'\bLlp\b': 'LLP',
    r'\bDba\b': 'DBA',
    r'\bL\.L\.C\.\b': 'LLC',
}

for pattern, replacement in suffix_map.items():
    df['Employer'] = df['Employer'].str.replace(
        pattern, replacement, regex=True
    )

# Replacing empty cells with unknown
df['Employer'] = df['Employer'].fillna('Unknown')

# The total number of unique employer names after cleaning
print(f"Unique employer names after cleaning: {df['Employer'].nunique():,}")
print()
print("Sample cleaned employer names:")
print(df['Employer'].head(10).to_string())
------------------------------------------------------------------------------------------------------
# Confirming Direct Parent Title and NAICS Industry Title does not need a T at the end of the name 
print("Before cleaning:")
print(df['Direct Parent Title'].unique()[:10])
print()
print(df['NAICS Industry Title'].unique()[:10])
print()
------------------------------------------------------------------------------------------------------
# Cleaning the trailing T and Spaces 
# Removing trailing Ts and spacess from the Direct Parent Title 
df['Direct Parent Title'] = df['Direct Parent Title'].str.rstrip('T').str.strip()

# Removing spaces and trailing Ts from NAICS Industry Title 
df['NAICS Industry Title'] = df['NAICS Industry Title'].str.strip().str.rstrip('T').str.strip()

------------------------------------------------------------------------------------------------------
# verifying data cleaning
print("After cleaning:")
print(df['Direct Parent Title'].unique()[:10])
print()
print(df['NAICS Industry Title'].unique()[:10])
print()
print("Cleaning complete!")

------------------------------------------------------------------------------------------------------
#Export cleaned dataset
df.to_csv("Severe_Injury_Report_Cleaned.csv", index=False)
print("Processed dataframe saved successfully!")
print(f"Total records saved: {len(df):,}")
print(f"Total columns saved: {len(df.columns)}")
print()
print("Columns included:")
for col in df.columns:
    print(f"  - {col}")
