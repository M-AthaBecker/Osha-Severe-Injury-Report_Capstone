
# 🗄️ SQL Analysis Queries — OSHA Severe Injury Report

![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?logo=mysql)
![DBeaver](https://img.shields.io/badge/DBeaver-Community-382923)
![Schema](https://img.shields.io/badge/Schema-osha__severe__injuries-blue)
![Records](https://img.shields.io/badge/Records-105%2C317-orange)

---

## 📋 Overview

This folder contains all SQL queries used to explore, clean, aggregate, and analyze the OSHA Severe Injury Report dataset in MySQL using DBeaver. The queries are organized into four files corresponding to the four phases of the SQL analysis.

---

## 📁 Query Files

| File | Phase | Description |
|---|---|---|
| `data_cleaning.sql` | Data Cleaning | Schema creation, table setup, data type corrections, date conversion, employer standardization |
| `data_exploration.sql` | Data Exploration | Record counts, date range verification, unique value checks, outcome summaries |
| `data_aggregation.sql` | Data Aggregation | Grouping by state, industry, event type, body part, day of week, and jurisdiction |
| `data_join.sql` | Data Join | Hierarchical LEFT JOIN with COALESCE for NAICS industry name matching |

---

## 🔧 Data Cleaning Queries

**File:** `data_cleaning.sql`

| Query | Purpose |
|---|---|
| `CREATE SCHEMA` | Creates the `osha_severe_injuries` schema |
| `CREATE TABLE sir_data` | Creates the main table with all 25 columns — all set to TEXT to prevent import errors |
| `ALTER TABLE` | Converts columns back to correct data types after import |
| `STR_TO_DATE()` | Converts EventDate from text to proper DATE format |
| `TRIM()` + `COALESCE()` | Removes leading and trailing spaces and replaces blank employer names with Unknown |
| `CASE` statement | Standardizes major employer name variations — Walmart, UPS, FedEx, Home Depot, USPS etc. |
| `DESCRIBE` | Verifies column data types after all alterations |

---

## 🔍 Data Exploration Queries

**File:** `data_exploration.sql`

| Query | Purpose | Key Result |
|---|---|---|
| `COUNT(*)` | Total number of records | 105,317 |
| `MIN / MAX EventDate` | Confirms date range | January 2015 – October 2025 |
| `COUNT DISTINCT Employer` | Unique employer count | 67,507 after standardization |
| `COUNT DISTINCT State` | Unique state count | 56 — all 50 states + DC + 5 territories |
| `SUM / COUNT` on outcomes | Total and % for each outcome | 81.63% hospitalized, 26.39% amputation, 0.03% loss of eye |
| `TOP 10 Employers` | Most frequently reported employers | Identifies highest incident employers |
| `NatureTitle counts` | Injuries by type | Fractures lead at 34,598 |
| `PartOfBodyTitle counts` | Injuries by body part | Fingertips lead at 10,402 |

---

## 📊 Data Aggregation Queries

**File:** `data_aggregation.sql`

| Query | Purpose | Key Result |
|---|---|---|
| `GROUP BY State` | Incidents by state | Texas leads with 17,378 |
| `GROUP BY EventTitle` | Incidents by event type | Shows most common causes of injury |
| `GROUP BY PartOfBodyTitle` | Incidents by body part | Fingertips most affected |
| `GROUP BY FederalState` | Federal vs State jurisdiction split | Shows OSHA oversight distribution |
| `DAYNAME(EventDate)` | Incidents by day of week | Tuesday and Wednesday peak |
| `DATE_FORMAT` monthly | Monthly incident trend | COVID-19 dip visible in 2020 |
| `QUARTER(EventDate)` | Incidents by quarter | Q2 and Q3 highest |
| `GROUP BY PrimaryNAICS` | Top 10 industries by code | Pre-join industry analysis |

---

## 🔗 Data Join Queries

**File:** `data_join.sql`

The highlight of the SQL analysis — a four-level hierarchical LEFT JOIN using COALESCE to match NAICS industry codes to human-readable industry names.

### Join Strategy

```sql
SELECT
    lj.id,
    lj.employer,
    lj.city,
    lj.state,
    lj.primarynaics,
    coalesce(
        n6.`2022NaicsTitle`,  -- Try exact 6-digit match first
        n4.`2022NaicsTitle`,  -- Fall back to 4 digits
        n3.`2022NaicsTitle`,  -- Fall back to 3 digits
        n2.`2022NaicsTitle`,  -- Fall back to 2 digits
        'unknown industry'    -- Default if no match found
    ) as industryname
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6
    on lj.primarynaics = n6.`2022NaicsCode`
left join osha_severe_injuries.naics n4
    on left(lj.primarynaics, 4) = n4.`2022NaicsCode`
left join osha_severe_injuries.naics n3
    on left(lj.primarynaics, 3) = n3.`2022NaicsCode`
left join osha_severe_injuries.naics n2
    on left(lj.primarynaics, 2) = n2.`2022NaicsCode`
limit 20;
```

### Why LEFT JOIN?

| Join Type | Reason Not Used |
|---|---|
| `INNER JOIN` | Would drop all records without an exact NAICS match — significant data loss |
| `RIGHT JOIN` | Would prioritize NAICS table records over injury records — opposite of desired outcome |
| `INTERSECT` | Only returns exact matches — same problem as INNER JOIN |
| `LEFT JOIN` ✅ | Keeps ALL injury records regardless of match — correct choice |

### COALESCE Hierarchy

The NAICS table is joined four times with different aliases — each representing a different digit-level match attempt:

| Alias | Match Strategy | Example |
|---|---|---|
| `n6` | Exact 6-digit match | `111110` → `Soybean Farming` |
| `n4` | First 4 digits | `1111` → `Oilseed and Grain Farming` |
| `n3` | First 3 digits | `111` → `Crop Production` |
| `n2` | First 2 digits | `11` → `Agriculture, Forestry, Fishing and Hunting` |

COALESCE reads across these four "phantom columns" left to right and returns the first non-null value — falling back to `unknown industry` only if all four levels fail to find a match.

### Match Status Validation

```sql
select
    case
        when coalesce(n6.`2022NaicsTitle`, n4.`2022NaicsTitle`,
                      n3.`2022NaicsTitle`, n2.`2022NaicsTitle`) is null
        then 'unknown industry'
        else 'matched'
    end as match_status,
    count(*) as total
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6
    on lj.primarynaics = n6.`2022NaicsCode`
left join osha_severe_injuries.naics n4
    on left(lj.primarynaics, 4) = n4.`2022NaicsCode`
left join osha_severe_injuries.naics n3
    on left(lj.primarynaics, 3) = n3.`2022NaicsCode`
left join osha_severe_injuries.naics n2
    on left(lj.primarynaics, 2) = n2.`2022NaicsCode`
group by match_status;
```

**Result:** 102,662 matched | 2,655 unknown | **97.48% match rate**

---

## 🏗️ Database Setup

```sql
-- Schema and table
CREATE SCHEMA osha_severe_injuries;
USE osha_severe_injuries;

-- Two tables used
-- 1. severe_injuries  → 105,317 OSHA incident records
-- 2. naics            → 2,125 NAICS industry reference records
```

---

## ▶️ How to Run

1. Open **DBeaver** and connect to your MySQL instance
2. Open a new SQL Editor — **Ctrl + ]**
3. Make sure `osha_severe_injuries` is selected as the active database
4. Open the desired `.sql` file
5. Run individual queries with **Ctrl + Enter**
6. Run the full script with **Ctrl + Alt + Enter**

> **Tip:** Run queries in this order for best results:
> 1. `data_cleaning.sql` — sets up schema and imports data
> 2. `data_exploration.sql` — verify data loaded correctly
> 3. `data_aggregation.sql` — run analytical queries
> 4. `data_join.sql` — run NAICS join queries last

---

## 📚 Data Sources

- **Primary Dataset:** [OSHA Severe Injury Report Dashboard](https://www.osha.gov/severe-injury-reports)
- **NAICS Reference:** [2022 NAICS Structure](https://www.census.gov/naics/?48967)
- **Regulatory Reference:** 29 CFR 1904.39

---

## 👩‍💼 Author

**Mary Becker**  
FullStack Academy Data Analytics Certificate | 2026  
Master of Arts in Human Resource Management — Saint Mary's University of Minnesota  
SHRM Member | MVHRA Member

[![GitHub](https://img.shields.io/badge/GitHub-M--AthaBecker-black?logo=github)](https://github.com/M-AthaBecker)
[![Tableau](https://img.shields.io/badge/Tableau-Public-blue?logo=tableau)](https://public.tableau.com/app/profile/m.athaBecker)
