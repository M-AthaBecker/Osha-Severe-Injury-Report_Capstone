"""
OSHA Severe Injury Report – Data Exploration
Author: Mary Becker
Description: Initial exploration of the OSHA severe injury dataset.
"""

## Checking dataset import 
print(df.shape)
print(df.head())

## Data Overview 
print("Dataset Dimensions:")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")
print()

## Column names and data types 
print("Column Names and Data Types:")
print(df.dtypes)
print()

## first 5 rows
print("First 5 Rows:")
df.head()

## Checking for missing values 
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)

# Creating a summary table
missing_summary = pd.DataFrame({
    'Missing Count': missing,
    'Missing %': missing_pct
})

# returning columns with missing values
missing_summary = missing_summary[missing_summary['Missing Count'] > 0]
missing_summary = missing_summary.sort_values('Missing %', ascending=False)

print("Missing Values Summary:")
print(missing_summary)
print()
print(f"Total columns with missing values: {len(missing_summary)}")

## Missing value handling 
print("Missing Value Handling:")
print()
print("Latitude - 0.07% - No action taken.  70 records is not a significant impact on the analysis.")
print()
print("Lontitude - 0.07% - No action taken.  70 records is not a significant impact on the analysis.")
print()
print("City - 0.02% - No action taken.  17 records is not a significant impact on the analysis.")
print()
print("Primary NAICS - 0.00% - No action taken.  2 records is not a significant impact on the analysis.") 
print()
print("No columns were dropped. The missing values do not have an impact on the overall analysis.")
print("The missing data does not represent data integrity concerns.") 

## Descriptive Statistics
# Summary Statistics for Numerical Columns
print("Summary Statistics for Numerical Columns:")
print()
print(df[['Hospitalized', 'Amputation', 'Loss Of Eye']].describe().round(2))
print()

# Total counts for each outcome
print("Outcome Totals:")
print(f"Total Hospitalized:  {df['Hospitalized'].sum():,}")
print(f"Total Amputations:   {df['Amputation'].sum():,}")
print(f"Total Loss of Eye:   {df['Loss Of Eye'].sum():,}")
print()

# Percentage of each outcome
total = len(df)
print("Outcome Percentages:")
print(f"% Hospitalized:  {df['Hospitalized'].sum() / total * 100:.2f}%")
print(f"% Amputation:    {df['Amputation'].sum() / total * 100:.2f}%")
print(f"% Loss of Eye:   {df['Loss Of Eye'].sum() / total * 100:.2f}%")
print()

# Unique value counts for categorical columns
print("Unique Value Counts for Categorical Columns:")
cat_cols = ['State', 'Primary NAICS', 'Part of Body Title', 
            'Employer','Nature Title','Event Title']
for col in cat_cols:
    print(f"{col}: {df[col].nunique():,} unique values")

## Checking unique state values 
state_vals = df['State'].unique()

print("All unique state values:")
print(state_vals)

## Single Value Check 
print("Columns with only one unique value:")
single_value = []
for col in df.columns:
    if df[col].nunique() == 1:
        single_value.append(col)
        print(f"  - {col}: {df[col].unique()[0]}")

if len(single_value) == 0:
    print("  None found - all columns have more than one unique value.  Dataset seems to be a reliable source.")

print()


# unique value counts for all columns
print("Unique value counts for all columns:")
for col in df.columns:
    print(f"  {col}: {df[col].nunique():,} unique values")
