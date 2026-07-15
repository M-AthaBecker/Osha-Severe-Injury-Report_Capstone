# 📈 Tableau Analysis — OSHA Severe Injury Report

![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau)
![Dashboards](https://img.shields.io/badge/Dashboards-3-blue)
![Worksheets](https://img.shields.io/badge/Worksheets-12-green)
![Records](https://img.shields.io/badge/Records-105%2C317-orange)

---

## 🔗 View Live Dashboards

> **All three interactive dashboards are published on Tableau Public:**

### 👉 [View on Tableau Public](https://public.tableau.com/app/profile/m.athaBecker)

---

## 📋 Overview

Three interactive Tableau dashboards were built to present the OSHA Severe Injury Report analysis in a visual and explorable format. All dashboards include **Year filters** allowing users to explore how patterns changed from 2015 through 2025.

---

## 📁 Data Source

| File | Description |
|---|---|
| `severe_injuries_processed_v2.csv` | Fully cleaned and enriched dataset exported from Python — includes industry names, Direct Parent Title, NAICS Industry Title, Weekday column, and all cleaned fields |

> **Note:** No joins were required in Tableau. All industry name lookups and data cleaning were completed prior to loading into Tableau. A calculated field `Direct Parent Title Clean` was created in Tableau to remove trailing T formatting artifacts from industry category names.

---

## 🧹 Data Cleaning in Tableau

One additional cleaning step was performed directly in Tableau after connecting the data source.

**Issue:** The `Direct Parent Title` column contained trailing `T` characters on several industry names — for example `Machinery ManufacturingT` and `Chemical ManufacturingT` — carried over from the original NAICS reference table formatting.

**Solution:** A calculated field was created:

```
IF RIGHT([Direct Parent Title], 1) = "T"
THEN LEFT([Direct Parent Title], LEN([Direct Parent Title]) - 1)
ELSE [Direct Parent Title]
END
```

This field `Direct Parent Title Clean` was used in place of the original column throughout all worksheets and dashboards.

---

## 📊 Worksheets

| # | Worksheet | Chart Type | Key Finding |
|---|---|---|---|
| 1 | OSHA Severe Injury Outcomes by State | Horizontal Bar | Texas leads all states at 17,378 incidents |
| 2 | Severe Injury Outcomes by Direct Parent Title | Horizontal Bar | Construction dominates at nearly 3x second place |
| 3 | Monthly Reports Over Time | Line Chart | COVID-19 dip clearly visible — peak 2018, drop 2020 |
| 4 | Forecasted Reports | Line Chart | Monthly incidents projected to stabilize 700-800 |
| 5 | Reports by Day of Week | Bar Chart | Tuesday and Wednesday are peak injury days |
| 6 | Severe Injury Report by Broad Category | Packed Bubbles | Construction bubble dominates all other categories |
| 7 | Hospitalized Pie | Pie Chart | 81.63% hospitalized vs 18.37% not hospitalized |
| 8 | Amputation Pie | Pie Chart | 26.39% amputation vs 73.61% no amputation |
| 9 | Loss of Eye Pie | Pie Chart | 0.03% loss of eye vs 99.97% no loss of eye |
| 10 | Top 20 Injuries by Nature Title | Horizontal Bar | Fractures lead at 34,598 — Amputations second at 23,449 |
| 11 | Top 20 Injuries by Body Part | Horizontal Bar | Fingertips lead at 10,402 — fingers dominate top 3 |
| 12 | Total Reports KPI | Text Card | 105,318 total severe injury reports |

---

## 🖥️ Dashboards

---

### Dashboard 1 — Injury Overview

**Purpose:** Provide a high-level summary of total incident volume and outcome distributions alongside the most common injury types and affected body parts.

| Worksheet Included | Description |
|---|---|
| Total Reports KPI | Bold number card showing 105,318 total records |
| Hospitalized Pie | Yes vs No outcome breakdown |
| Amputation Pie | Yes vs No outcome breakdown |
| Loss of Eye Pie | Yes vs No outcome breakdown |
| Top 20 Injuries by Nature Title | Horizontal bar chart |
| Top 20 Injuries by Body Part | Horizontal bar chart |

**Filters:** Year filter applies interactively across all visualizations

**Key Story:** Fractures are the most common injury type at 34,598 incidents and fingertips are the most commonly injured body part at 10,402 — both strongly associated with construction and manufacturing environments.

---

### Dashboard 2 — Time Analysis

**Purpose:** Explore how severe workplace injuries trended over time and which days carry the highest risk.

| Worksheet Included | Description |
|---|---|
| Monthly Reports Over Time | Line chart with COVID-19 reference line and trend line |
| Forecasted Reports | Exponential smoothing projection through 2027 |
| Reports by Day of Week | Bar chart with weekday vs weekend color contrast |

**Filters:** Year filter applies interactively across all three charts

**Key Story:** Injuries peaked in 2018 at 11,156 annual incidents, dropped sharply in 2020 due to COVID-19, and have not returned to pre-pandemic levels. The forecast projects stabilization around 700-800 monthly incidents through 2027.

---

### Dashboard 3 — Industry Analysis

**Purpose:** Identify which industries and geographic areas carry the highest severe injury burden.

| Worksheet Included | Description |
|---|---|
| OSHA Severe Injury Outcomes by State | Horizontal bar with Hospitalized, Amputation, Loss of Eye, and Total Outcomes |
| Severe Injury Outcomes by Direct Parent Title | Broad industry breakdown across all four outcome measures |
| Severe Injury Report by Broad Category | Packed bubble chart colored by industry category |

**Filters:** Year filter and Direct Parent Title Clean filter apply interactively across all charts

**Key Story:** Construction is the dominant industry across all metrics — recording nearly 3x more incidents than the second-ranked category. Texas leads all states by a significant margin.

---

## 🎨 Design Decisions

| Decision | Rationale |
|---|---|
| Consistent color scheme | Blue tones for primary bars, orange/gold for secondary measures, green for positive outcomes — colorblind accessible |
| Year filter on all dashboards | Allows stakeholders to explore year-specific patterns without building separate views |
| Separate dashboards by theme | Reduces clutter — injury overview, time trends, and industry analysis each get dedicated space |
| Packed bubble chart | Visually communicates the dominance of Construction at a glance — size difference is immediately apparent |
| COVID-19 reference line | Provides critical context for the 2020 decline without requiring explanation |

---

## ♿ Accessibility Considerations

- Color choices avoid red-green combinations that are difficult for colorblind viewers
- All charts include data labels so values are readable without relying on color alone
- Chart titles and axis labels are included on every worksheet
- Tooltips provide additional detail on hover for all data points

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
