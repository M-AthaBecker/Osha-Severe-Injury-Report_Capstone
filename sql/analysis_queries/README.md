
## 🏥 OSHA Severe Injury Report - SQL Analysis

This section documents the SQL analysis of the [OSHA Severe Injury Report](https://www.osha.gov/severeinjury) dataset to identify high-risk industries, geographic hotspots, injury patterns, and temporal trends in workplace severe injuries.

> **Objective:** Answer - Which industries, states, and injury types drive severe workplace injuries, and how have trends evolved over time?

### 📂 SQL Folder Structure

```text
sql/
├── 01_data_exploration.sql  # Initial profiling & data quality checks
├── 02_data_cleaning.sql     # Standardization & deduplication
├── 03_data_aggregation.sql  # Core business questions & KPIs
└── 04_data_joins.sql        # Enrichment with NAICS industry data
```

### 🔍 What's Inside Each File

#### 1. `01_data_exploration.sql` - Data Exploration
- Row counts, date range, and distinct value checks
- Distribution of `Injury Type`, `Body Part`, `Event Type`, `State`
- Identification of nulls, inconsistent state codes, and invalid NAICS codes
- Used: `COUNT(DISTINCT)`, `GROUP BY`, `ORDER BY`, `WHERE ... IS NULL`

#### 2. `02_data_cleaning.sql` - Data Cleaning
- Standardized `EventDate` to `DATE` format and removed future dates
- Trimmed and upper-cased `State`, `City`, `NAICS Code`
- Removed duplicate reports using `ROW_NUMBER() OVER (PARTITION BY EventDate, Employer, City)`
- Handled nulls in `Nature`, `Part of Body`, `Source` with `COALESCE()`
- Created clean staging view: `vw_osha_clean`

#### 3. `03_data_aggregation.sql` - Data Aggregation & Analysis
Key questions answered:
- **Top Industries:** Injuries by NAICS 2-digit and 4-digit sector
- **Top States:** Severe injuries by state (total & per quarter)
- **Injury Characteristics:** Most common nature of injury, body part, and event source
- **Trends Over Time:** Year-over-year and monthly seasonality using `DATE_TRUNC()` / `DATENAME(MONTH)`
- Techniques: CTEs, `CASE` statements, Window Functions `RANK()`, `SUM() OVER()`, conditional aggregation

Example:
```sql
-- Top 5 industries by severe injury count
WITH industry_counts AS (
  SELECT 
    n.sector_description,
    COUNT(*) AS injury_count,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
  FROM vw_osha_clean o
  LEFT JOIN naics_structure n ON o.naics_code = n.naics_code
  GROUP BY n.sector_description
)
SELECT sector_description, injury_count 
FROM industry_counts 
WHERE rnk <= 5;
```

#### 4. `04_data_joins.sql` - Data Joins & Enrichment
- Joined OSHA data with `NAICS Structure.xlsx` (6-digit NAICS to Sector Title mapping) to translate codes → readable industry names
- LEFT JOIN to preserve all injury records, INNER JOIN for validated analysis
- Verified join integrity: checked for unmatched NAICS codes

### 🛠️ Skills Demonstrated
- **SQL:** CTEs, Window Functions (`ROW_NUMBER, RANK`), Aggregations, `CASE`, `COALESCE`, Date Functions
- **Data Quality:** Deduplication, null handling, standardization, validation checks
- **Analytical Thinking:** Translating business questions into efficient queries, enrichment via lookup tables

### 📊 Key Findings (from queries)
1. **Manufacturing (31-33) and Construction (23)** consistently account for the highest share of severe injuries.
2. **Top states:** TX, CA, FL, PA, OH - correlated with workforce size and high-risk industries.
3. **Most common injuries:** Amputations and fractures, with `Fingers/Hands` as most affected body part, source often `Machinery`.
4. **Seasonality:** Q2-Q3 shows a slight uptick, potentially linked to increased construction and temp labor activity.

### 🔗 Data Source
- OSHA Severe Injury Reports (2015-Present) - [osha.gov](https://www.osha.gov/severeinjury)
- NAICS Industry Structure Reference Table

---
*All queries written in standard ANSI SQL (Compatible with SQL Server / PostgreSQL).*

