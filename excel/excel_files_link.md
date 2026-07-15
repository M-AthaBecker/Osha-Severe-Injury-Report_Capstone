# 📊 Excel Analysis — OSHA Severe Injury Report Capstone

![Excel](https://img.shields.io/badge/Microsoft-Excel-217346?logo=microsoft-excel)
![OneDrive](https://img.shields.io/badge/Files%20Hosted-OneDrive-0078D4?logo=microsoft-onedrive)
![Records](https://img.shields.io/badge/Records-105%2C317-orange)

---

## 📁 File Access

> **Note:** Excel workbooks are hosted externally on OneDrive due to GitHub file size limitations.

### 🔗 [Access Excel Files on OneDrive](https://1drv.ms/f/c/1562BD349AF6D1BE/IgC7JsIZXjoiQ5PdADut5pCrAXLGcTuc46TtWsBtHT1PYOg?e=BThBYg)

---

## 📂 Files Included

| File | Description |
|---|---|
| **Raw Dataset** | Original OSHA Severe Injury Report CSV as downloaded from osha.gov — no modifications |
| **Data Cleaning Workbook** | Excel workbook with all data cleaning steps applied including duplicate removal, date conversion, employer standardization, zip code restoration, state formatting, and hierarchical XLOOKUP for NAICS industry names |
| **Analysis Workbook** | Excel workbook containing all pivot tables, charts, statistical summary, and year over year analysis |
| **Tableau-Ready Dataset** | Final cleaned and enriched CSV used as the data source for Tableau Public dashboards |

---

## 🔧 Data Cleaning Performed in Excel

| Column | Issue Found | Action Taken |
|---|---|---|
| ID | 1 duplicate record found | Removed — final dataset is 105,317 records |
| Event Date | Stored as text not a date | Converted using Text to Columns — MDY format |
| Employer | Blank values, inconsistent capitalization, extra spaces | Trimmed spaces, applied PROPER case, noted as dataset limitation |
| State | Inconsistent capitalization, some full state names | Trimmed spaces, converted to UPPER case |
| Zip | Missing leading zeros — stored as number | Restored using TEXT formula — zero-padded to 5 digits |
| City | 17 blank records | Retained — valid injury data in remaining fields |
| Primary NAICS | Varied digit lengths | Used hierarchical XLOOKUP for industry name matching |
| NAICS Industry Title | Trailing T formatting artifacts | Removed using Excel formula |
| Direct Parent Title | Trailing T formatting artifacts | Removed using Excel formula |

---

## 🔍 NAICS Hierarchical XLOOKUP

One of the most significant Excel tasks was building a hierarchical XLOOKUP formula to match NAICS industry codes to human-readable industry names. The formula attempts matches at four levels of specificity:

```excel
=IFERROR(
    XLOOKUP(TEXT([@[Primary NAICS]],"000000"),TEXT(NAICS_Codes[2022 NAICS Code],"000000"),NAICS_Codes[National Industry title]),
    IFERROR(
        XLOOKUP(LEFT(TEXT([@[Primary NAICS]],"000000"),4),TEXT(NAICS_Codes[2022 NAICS Code],"000000"),NAICS_Codes[National Industry title]),
        IFERROR(
            XLOOKUP(LEFT(TEXT([@[Primary NAICS]],"000000"),3),TEXT(NAICS_Codes[2022 NAICS Code],"000000"),NAICS_Codes[National Industry title]),
            IFERROR(
                XLOOKUP(LEFT(TEXT([@[Primary NAICS]],"000000"),2),TEXT(NAICS_Codes[2022 NAICS Code],"000000"),NAICS_Codes[National Industry title]),
                "Unknown"
            )
        )
    )
)
```

**Result:** Reduced unmatched industry records from 10,794 to just **32** out of 105,317 — a **99.97% match rate.**

---

## 📊 Analysis Performed in Excel

| Analysis | Description |
|---|---|
| Statistical Summary | Total, % Yes, % No for Hospitalized, Amputation, and Loss of Eye |
| Correlation Analysis | CORREL formula between Hospitalized and Amputation — returned -0.79 |
| Top 20 Industries | PivotTable filtered to top 20 by hospitalizations with stacked bar chart |
| Year Over Year Trend | PivotTable grouped by year with line chart — top 5 industries |
| Day of Week Analysis | CHOOSE/WEEKDAY helper column with bar chart |
| Forecasting | FORECAST.ETS function projecting monthly incidents |
| Geographic Analysis | Top 3 and top 10 states by incident count |
| NAICS Industry Lookup | Hierarchical XLOOKUP returning industry names and parent categories |

---

## 📈 Charts Produced in Excel

| Chart | Type | Key Finding |
|---|---|---|
| Top 20 Industries by Hospitalizations | Stacked Bar | General Medical leads, construction trades dominate |
| Year Over Year Trend — Top 5 Industries | Line Chart | COVID-19 dip clearly visible in 2020 |
| Severe Workplace Injuries by Day of Week | Bar Chart | Tuesday and Wednesday peak |
| Forecasted Injuries | Line Chart | Stabilizing around 700-800 per month |

---

## 📋 Statistical Summary

| Metric | Hospitalized | Amputation | Loss of Eye |
|---|---|---|---|
| Total Records | 105,317 | 105,310 | 105,312 |
| Total Yes | 85,971 | 27,788 | 35 |
| Total No | 19,346 | 77,522 | 105,277 |
| % Yes | 81.63% | 26.39% | 0.03% |
| % No | 18.37% | 73.61% | 99.97% |

> **Note:** Minor discrepancies in total record counts across columns reflect a small number of blank values in Amputation and Loss of Eye fields — retained as valid data gaps.

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
