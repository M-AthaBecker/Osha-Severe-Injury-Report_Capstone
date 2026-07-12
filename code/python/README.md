# 🐍 Python Analysis — OSHA Severe Injury Report
### Exploratory Data Analysis, Visualizations & Forecasting

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-lightblue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.x-teal)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

---

## 📋 Overview

This Jupyter Notebook performs exploratory data analysis, statistical analysis, visualizations, and forecasting on the OSHA Severe Injury Report dataset containing **105,317 records** spanning January 2015 through October 2025.

---

## 📦 Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, manipulation, and grouping |
| `numpy` | Numerical calculations and linear trend forecasting |
| `matplotlib` | Chart creation and formatting |
| `seaborn` | Chart styling and heatmap generation |

---

## 📁 Input Files

| File | Description |
|---|---|
| `severe_injuries_clean_v2.csv` | Cleaned OSHA severe injury dataset with industry names, weekday column, and NAICS hierarchy columns |

> **Note:** The processed CSV already contains `Direct Parent Title` and `NAICS Industry Title` columns from the hierarchical XLOOKUP performed in Excel. No separate NAICS join is required in Python.

---

## 🔧 Data Cleaning Steps

| Step | Description |
|---|---|
| Date Conversion | `Event Date` converted from Excel serial number format to datetime using `pd.to_datetime()` |
| Zip Code | Converted to text and zero-padded to 5 digits using `str.zfill(5)` |
| Amputation | Filled nulls with 0 and converted from float to integer |
| Loss of Eye | Filled nulls with 0 and converted from float to integer |
| Employer Names | Stripped whitespace using `str.strip()`, converted to title case using `str.title()`, normalized double spaces using `str.replace()` |
| Industry Titles | Removed trailing `T` formatting artifacts from `Direct Parent Title` and `NAICS Industry Title` using `str.rstrip('T')` |
| Year Column | Extracted from `Event Date` using `dt.year` for time series analysis |
| YearMonth Column | Extracted using `dt.to_period('M')` for monthly trend analysis |

---

## 📊 Charts Produced

### 1. Outcomes Distribution — Pie Charts
**File:** `outcomes_distribution.png`  
Three side-by-side pie charts showing Yes vs No percentages for Hospitalized, Amputation, and Loss of Eye outcomes.

**Key Finding:** 81.63% of incidents resulted in hospitalization, 26.39% in amputation, and only 0.03% in loss of eye.

---

### 2. Top 15 Injury Types — Horizontal Bar Chart
**File:** `injuries_by_nature.png`  
Horizontal bar chart showing the top 15 injury types by NatureTitle sorted by incident count.

**Key Finding:** Fractures (34,598) and Amputations (23,449) dominate all other injury types by a significant margin.

---

### 3. Top 10 States — Horizontal Bar Chart
**File:** `top10_states.png`  
Horizontal bar chart showing the top 10 states by total severe injury incident count.

**Key Finding:** Texas leads with 17,378 incidents — nearly 50% more than second-place Florida at 11,630.

---

### 4. Correlation Heatmap
**File:** `correlation_heatmap.png`  
Color-coded heatmap showing correlation between Hospitalized, Amputation, and Loss of Eye.

**Key Finding:** Strong negative correlation of -0.79 between Hospitalized and Amputation confirms these are largely mutually exclusive outcomes.

---

### 5. Incidents Over Time — Line Chart
**File:** `incidents_over_time.png`  
Line chart showing yearly incident counts from 2015 to 2025 with COVID-19 reference line.

**Key Finding:** Peak of 11,156 incidents in 2018, sharp COVID drop in 2020, no full recovery to pre-pandemic levels.

---

### 6. Injuries by Day of Week — Bar Chart
**File:** `injuries_by_day.png`  
Bar chart showing incident counts by day of week with weekdays and weekends in different colors.

**Key Finding:** Tuesday (19,660) and Wednesday (19,718) are the peak injury days. Weekends are significantly lower.

---

### 7. Top 20 Industries — Stacked Bar Chart
**File:** `top20_industries.png`  
Horizontal stacked bar chart showing top 20 NAICS Industry Titles by hospitalizations with amputation and loss of eye stacked.

**Key Finding:** General Medical and Surgical Hospitals leads at 2,348 hospitalizations. Construction trades dominate the list.

---

### 8. Top 20 Broad Industry Categories — Stacked Bar Chart
**File:** `top20_parent_industries.png`  
Horizontal stacked bar chart showing top 20 Direct Parent Title categories by hospitalizations.

**Key Finding:** Construction records nearly 3x more incidents than the second-ranked category.

---

### 9. Forecast — Actual vs Projected
**File:** `forecast.png`  
Line chart showing historical monthly incident counts with a linear trend line and 6-month forecast.

**Key Finding:** Monthly incidents projected to stabilize between 700-800 through early 2026 with no return to pre-COVID levels.

---

### 10. Outlier Detection — Box Plots
**File:** `outliers_boxplot.png`  
Three side-by-side box plots showing outlier distribution for Hospitalized, Amputation, and Loss of Eye.

**Key Finding:** Hospitalized has 20,668 outlier records representing multi-employee incidents. Loss of Eye has 35 outliers consistent with its 0.03% rate.

---

### 11. Skewness Distribution — Histograms
**File:** `skewness_distribution.png`  
Three histograms showing the distribution and skewness of each numeric outcome column.

**Key Finding:** Hospitalized is highly negatively skewed (-1.24), Amputation is positively skewed (+1.08), and Loss of Eye is extremely skewed (+54.83).

---

## 📈 Statistical Summary

| Metric | Hospitalized | Amputation | Loss of Eye |
|---|---|---|---|
| Total Records | 105,317 | 105,317 | 105,317 |
| Total Yes | 85,971 | 27,788 | 35 |
| Total No | 19,346 | 77,529 | 105,282 |
| % Yes | 81.63% | 26.39% | 0.03% |
| Skewness | -1.24 | +1.08 | +54.83 |
| Outliers | 20,668 | 0 | 35 |

---

## 🔍 EDA Checklist

| Check | Result |
|---|---|
| Dataset dimensions | 105,317 rows × 25 columns |
| Single value columns | None found — all columns have 2+ unique values |
| Missing values | 8 columns with missing values — all retained with documentation |
| Duplicate records | 1 duplicate removed in Excel prior to Python analysis |
| Date range | January 2015 – October 2025 confirmed |
| Unique states | 56 — all 50 states + DC + 5 US territories confirmed valid |
| Unique employers | 66,519 after standardization |
| Unique industries | 1,000 NAICS industry titles matched |

---

## 📝 Notes

- All charts saved as `.png` files at 150 DPI using `plt.savefig()`
- Chart style set to `seaborn white` — no grid lines
- The `Weekday` column was pre-calculated in Excel and loaded directly — no `dt.day_name()` extraction needed
- The `Direct Parent Title` and `NAICS Industry Title` columns were pre-joined in Excel via hierarchical XLOOKUP — no Python join required
- Processed dataframe saved as `severe_injuries_processed_v2.csv` at end of notebook for use in Tableau

---

## ▶️ How to Run

1. Open **Jupyter Notebook** via Anaconda Navigator
2. Navigate to your Capstone folder
3. Open `OSHA_Capstone_Analysis.ipynb`
4. Go to **Kernel → Restart & Run All**
5. All charts will regenerate and save automatically

> **Quick Reload Option:** If the kernel resets, load the processed CSV directly:
> ```python
> df = pd.read_csv(r'C:\Users\maryb\Downloads\Capstone\severe_injuries_processed_v2.csv')
> ```
> This skips all cleaning steps and loads the pre-processed data in seconds.

---

## 📚 Data Source

- **Primary Dataset:** [OSHA Severe Injury Report Dashboard](https://www.osha.gov/severe-injury-reports)
- **Regulatory Reference:** 29 CFR 1904.39
