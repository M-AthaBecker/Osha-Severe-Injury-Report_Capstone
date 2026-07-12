"""
OSHA Severe Injury Report – Visualizations
Author: Mary Becker
Description: Python visualizations for OSHA severe injury data using Matplotlib and Seaborn.
"""
-----------------------------------------------------------------------------------------------
## Importing needed libararies to complete analysis 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraries loaded successfully!")
-----------------------------------------------------------------------------------------------
## Visualizations 
# establishing the visualization style
sns.set_style('white')
plt.rcParams['figure.figsize'] = (12,6)
plt.rcParams['font.size'] = 12

print('Visualization style ready to go!')
-----------------------------------------------------------------------------------------------
## Pie chart for severe injury outcome
fig, axes = plt.subplots(1,3, figsize=(18,6))

# Data for each pie chart
outcomes = {
    'Hospitalized' : [df['Hospitalized'].sum(), len(df) - df['Hospitalized'].sum()],
    'Amputation' : [df['Amputation'].sum(), len(df) - df['Amputation'].sum()],
    'Loss Of Eye' : [df['Loss Of Eye'].sum(), len(df) - df['Loss Of Eye'].sum()]
}

colors = [['mediumvioletred', 'thistle'],
          ['dodgerblue', 'lightskyblue'],
          ['darkorange', 'moccasin']]

for idx, (outcome, values) in enumerate(outcomes.items()):
   
    axes[idx].pie(
        values,
        labels=['Yes','No'],
        autopct='%1.2f%%',
        colors=colors[idx],
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}
    )
    axes[idx].set_title(f'{outcome}', fontsize=14, fontweight='bold', pad=15)

# Naming chart 
fig.suptitle(
    'Severe Workplace Injury Outcomes\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold',
    y=1.02
)

plt.tight_layout()
plt.show() 
-----------------------------------------------------------------------------------------------
## Bar chart on injuries by nature title 
# finding the top 15 nature titles 
naturetitle_counts = df['Nature Title'].value_counts().head(15).reset_index()
naturetitle_counts.columns = ['Nature Title', 'Count']

# creating the horizontal chart 
plt.figure(figsize=(14, 8))

plt.barh(
    naturetitle_counts['Nature Title'],
    naturetitle_counts['Count'],
    color='coral',
    edgecolor='white'
)

# placing data labels
for index, value in enumerate(naturetitle_counts['Count']):
    plt.text(
        value + 100,
        index,
        f'{value:,}',
        va='center',
        fontsize=10
    )

# Naming the chart, x and y axis 
plt.title(
    'Top 15 Injury Types (Nature Title)\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Injury Type', fontsize=12)
plt.gca().invert_yaxis()
plt.xlim(0, naturetitle_counts['Count'].max() * 1.15)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Top 10 States by number of reports 
# finding top 10 states by reports 
state_counts = df['State'].value_counts().head(10).reset_index()
state_counts.columns = ['State', 'Count']

# Create horizontal bar chart
plt.figure(figsize=(14, 8))

plt.barh(
    state_counts['State'],
    state_counts['Count'],
    color='silver',
    edgecolor='white'
)

# placing data labels 
for index, value in enumerate(state_counts['Count']):
    plt.text(
        value + 50,
        index,
        f'{value:,}',
        va='center',
        fontsize=10
    )

# Naming the chart and the x and y axis 
plt.title(
    'Top 10 States by Severe Workplace Injuries\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.gca().invert_yaxis()
plt.xlim(0, state_counts['Count'].max() * 1.15)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Heatmap 
# Desired columns
corr_data = df[['Hospitalized', 'Amputation', 'Loss Of Eye']].corr()

# Create heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_data,
    annot=True,           
    fmt='.2f',           
    cmap='coolwarm',      
    center=0,             
    linewidths=1,         
    linecolor='white',    
    square=True,          
    annot_kws={'size': 14, 'weight': 'bold'}  
)

# Naming the chart 
plt.title(
    'Correlation Matrix — Injury Outcomes\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold',
    pad=15
)

plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Reports over time 
# Finding year for each report 
df['Year'] = df['Event Date'].dt.year

# Counting number of reports each year
yearly_counts = df.groupby('Year').size().reset_index(name='Count')

# Creating the chart
plt.figure(figsize=(14, 6))

plt.plot(
    yearly_counts['Year'],
    yearly_counts['Count'],
    color='darkblue',
    linewidth=2.5,
    marker='o',          
    markersize=8,
    markerfacecolor='cyan',
    markeredgecolor='white',
    markeredgewidth=1.5
)

# Adding data labels
for x, y in zip(yearly_counts['Year'], yearly_counts['Count']):
    plt.text(
        x, y + 100,
        f'{y:,}',
        ha='center',
        fontsize=9
    )

# Add vertical line for COVID
plt.axvline(x=2020, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
plt.text(2020.1, yearly_counts['Count'].max() * 0.95, 
         'COVID-19', color='red', fontsize=10)

# Naming chart and x and y axis
plt.title(
    'Severe Workplace Injuries Over Time\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.xticks(yearly_counts['Year'], rotation=45)
plt.ylim(0, yearly_counts['Count'].max() * 1.15)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Injuries by day of week 
# Counting the weekdays 
day_counts = df.groupby('Weekday').size().reset_index(name='Count')

# placing days in correct calendar order
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday']
day_counts['Weekday'] = pd.Categorical(
    day_counts['Weekday'], 
    categories=day_order, 
    ordered=True
)
day_counts = day_counts.sort_values('Weekday')

# creating the bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(
    day_counts['Weekday'],
    day_counts['Count'],
    color=['brown', 'green', 'green', 'green', 
           'green', 'green', 'brown'],
    edgecolor='white'
)

# formatting the data labels 
for bar, value in zip(bars, day_counts['Count']):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 100,
        f'{value:,}',
        ha='center',
        fontsize=10
    )

# placing the name of the chart and on the x and y axis 
plt.title(
    'Severe Workplace Injuries by Day of Week\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.ylim(0, day_counts['Count'].max() * 1.15)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## top 20 industries by hospitalizations 
# Removing unknown industries
df_known = df[df['NAICS Industry Title'] != 'Unknown']

# Finding top 20 industries by hospitalizations
industry_counts = df_known.groupby('NAICS Industry Title').agg(
    Hospitalizations=('Hospitalized', 'sum'),
    Amputations=('Amputation', 'sum'),
    LossOfEye=('Loss Of Eye', 'sum')
).reset_index()

# Sorting results to get only top 20
industry_counts = industry_counts.sort_values(
    'Hospitalizations', ascending=False
).head(20)

# Creating the horizontal stacked bar chart
plt.figure(figsize=(16, 10))

plt.barh(industry_counts['NAICS Industry Title'], 
         industry_counts['Hospitalizations'],
         color='teal', label='Hospitalizations')

plt.barh(industry_counts['NAICS Industry Title'],
         industry_counts['Amputations'],
         left=industry_counts['Hospitalizations'],
         color='gold', label='Amputations')

plt.barh(industry_counts['NAICS Industry Title'],
         industry_counts['LossOfEye'],
         left=industry_counts['Hospitalizations'] + industry_counts['Amputations'],
         color='black', label='Loss of Eye')

# Naming the chart and axes
plt.title(
    'Top 20 Industries by Severe Workplace Injury Outcomes\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Industry', fontsize=12)
plt.gca().invert_yaxis()
plt.legend(loc='lower right', fontsize=11)
plt.xlim(0, industry_counts['Hospitalizations'].max() * 1.5)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Top 20 broad industry categories 
# removing the unknown
df_known2 = df[df['Direct Parent Title'] != 'Unknown']

# finding top 20 industries by hospitalizations
parent_counts = df_known2.groupby('Direct Parent Title').agg(
    Hospitalizations=('Hospitalized', 'sum'),
    Amputations=('Amputation', 'sum'),
    LossOfEye=('Loss Of Eye', 'sum')
).reset_index()

# sorting results to get only top 20
parent_counts = parent_counts.sort_values(
    'Hospitalizations', ascending=False
).head(20)

# creating the horizontal stacked bar chart
plt.figure(figsize=(16, 10))

plt.barh(parent_counts['Direct Parent Title'],
         parent_counts['Hospitalizations'],
         color='steelblue', label='Hospitalizations')

plt.barh(parent_counts['Direct Parent Title'],
         parent_counts['Amputations'],
         left=parent_counts['Hospitalizations'],
         color='darkorange', label='Amputations')

plt.barh(parent_counts['Direct Parent Title'],
         parent_counts['LossOfEye'],
         left=parent_counts['Hospitalizations'] + parent_counts['Amputations'],
         color='darkgreen', label='Loss of Eye')

# naming the chart and axes
plt.title(
    'Top 20 Broad Industry Categories by Severe Workplace Injury Outcomes\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Industry Category', fontsize=12)
plt.gca().invert_yaxis()
plt.legend(loc='lower right', fontsize=11)
plt.xlim(0, parent_counts['Hospitalizations'].max() * 1.5)
plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Forecasting 
import numpy as np

# grouping data by month
df['YearMonth'] = df['Event Date'].dt.to_period('M')
monthly = df.groupby('YearMonth').size().reset_index(name='Count')
monthly['YearMonth'] = monthly['YearMonth'].dt.to_timestamp()

# creating a time index for forecasting 
monthly['TimeIndex'] = np.arange(len(monthly))

# doing the trend
z = np.polyfit(monthly['TimeIndex'], monthly['Count'], 1)
p = np.poly1d(z)

# completing forecast for 6 months ahead
future_indices = np.arange(len(monthly), len(monthly) + 6)
future_dates = pd.date_range(
    start=monthly['YearMonth'].iloc[-1],
    periods=7,
    freq='MS'
)[1:]
forecast_values = p(future_indices)

# creating the chart 
plt.figure(figsize=(16, 6))

# Plot actual data
plt.plot(
    monthly['YearMonth'],
    monthly['Count'],
    color='darkblue',
    linewidth=2,
    label='Actual Reports',
    marker='o',
    markersize=4
)

# placement of the trend line
plt.plot(
    monthly['YearMonth'],
    p(monthly['TimeIndex']),
    color='darkorange',
    linewidth=2,
    linestyle='--',
    label='Trend Line'
)

# plotting the forecast 
plt.plot(
    future_dates,
    forecast_values,
    color='darkgreen',
    linewidth=2,
    linestyle='--',
    marker='o',
    markersize=6,
    label='Forecast'
)

# shading the forecasted region
plt.axvspan(
    future_dates[0],
    future_dates[-1],
    alpha=0.1,
    color='darkgreen',
    label='Forecast Period'
)

# separation of the actual versus forecasted 
plt.axvline(
    x=monthly['YearMonth'].iloc[-1],
    color='red',
    linestyle='--',
    linewidth=1.5,
    alpha=0.7
)
plt.text(
    monthly['YearMonth'].iloc[-1],
    monthly['Count'].max() * 1.05,
    'Forecast Start',
    color='red',
    fontsize=9
)

# naming the chart and the x and y axis
plt.title(
    'Severe Workplace Injuries — Actual vs Forecast\nJanuary 2015 - April 2026',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Reports', fontsize=12)
plt.legend(loc='lower left', fontsize=10)
plt.tight_layout()
plt.show()


print("Forecasted Monthly Reports:")
for date, value in zip(future_dates, forecast_values):
    print(f"{date.strftime('%B %Y')}: {int(value):,}")
-----------------------------------------------------------------------------------------------
## Identifying outliers 
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# titles
outcomes = ['Hospitalized', 'Amputation', 'Loss Of Eye']
colors = ['navy', 'cornflowerblue', 'mediumpurple']

for idx, (outcome, color) in enumerate(zip(outcomes, colors)):
    axes[idx].boxplot(
        df[outcome].dropna(),
        patch_artist=True,
        boxprops=dict(facecolor=color, alpha=0.7),
        medianprops=dict(color='white', linewidth=2),
        whiskerprops=dict(color=color, linewidth=1.5),
        capprops=dict(color=color, linewidth=1.5),
        flierprops=dict(
            marker='o',
            markerfacecolor=color,
            markersize=4,
            alpha=0.5
        )
    )
    axes[idx].set_title(outcome, fontsize=14, fontweight='bold')
    axes[idx].set_ylabel('Count per Report', fontsize=11)
    
    # returning outliers
    Q1 = df[outcome].quantile(0.25)
    Q3 = df[outcome].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[outcome] < Q1 - 1.5 * IQR) | 
                  (df[outcome] > Q3 + 1.5 * IQR)]
    print(f"{outcome}:")
    print(f"  Q1: {Q1} | Q3: {Q3} | IQR: {IQR}")
    print(f"  Outlier count: {len(outliers):,}")
    print()

# naming chart
fig.suptitle(
    'Outliers - Severe Workplace Injury Outcomes\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold',
    y=1.02
)

plt.tight_layout()
plt.show()
-----------------------------------------------------------------------------------------------
## Skewness check
# skewness of numeric columns
numeric_cols = ['Hospitalized', 'Amputation', 'Loss Of Eye']

print("Numberic columns skewness:")
print()
for col in numeric_cols:
    skew = df[col].skew()
    if skew > 1:
        direction = "Highly Positively Skewed (tail on right)"
    elif skew > 0.5:
        direction = "Moderately Positively Skewed"
    elif skew < -1:
        direction = "Highly Negatively Skewed (tail on left)"
    elif skew < -0.5:
        direction = "Moderately Negatively Skewed"
    else:
        direction = "Approximately Symmetric"
    
    print(f"{col}:")
    print(f"  Skewness: {skew:.4f}")
    print(f"  Direction: {direction}")
    print()

# visualization
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for idx, col in enumerate(numeric_cols):
    axes[idx].hist(
        df[col].dropna(),
        bins=20,
        color=['navy', 'cornflowerblue', 'mediumpurple'][idx],
        edgecolor='white'
    )
    axes[idx].set_title(f'{col}\nSkewness: {df[col].skew():.4f}', 
                        fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Value', fontsize=10)
    axes[idx].set_ylabel('Frequency', fontsize=10)

fig.suptitle(
    'Distribution of Numeric Columns\nJanuary 2015 - October 2025',
    fontsize=16,
    fontweight='bold',
    y=1.02
)

plt.tight_layout()
plt.show()

