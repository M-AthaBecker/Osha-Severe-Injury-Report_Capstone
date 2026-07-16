# 🦺 OSHA Severe Workplace Injury Analysis
### Data Analytics Capstone Project | FullStack Academy | 2026

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20SQL%20%7C%20Python%20%7C%20Tableau-blue)
![Records](https://img.shields.io/badge/Records-105%2C317-orange)
![Date Range](https://img.shields.io/badge/Date%20Range-Jan%202015%20–%20Oct%202025-lightgrey)

---

## 📋 Project Overview

This capstone project analyzes **105,317 OSHA Severe Workplace Injury Reports** spanning January 2015 through October 2025. The dataset was sourced directly from the [OSHA Severe Injury Report Dashboard](https://www.osha.gov/severe-injury-reports) and enriched with NAICS industry classification data from the U.S. Census Bureau.

Under **29 CFR 1904.39**, employers are required to report three types of severe workplace injuries to OSHA within 24 hours:
- 🏥 **In-patient Hospitalization**
- ✂️ **Amputation**
- 👁️ **Loss of an Eye**

---

## 🎯 Research Questions

1. Which industries have the highest rates of severe workplace injuries?
2. How has the frequency of severe injuries changed over time from 2015 to 2025?
3. Which injury types and body parts are most commonly affected?
4. Is there a relationship between hospitalization and amputation outcomes?
5. Are there patterns in when severe injuries occur — by day of week or time of year?
6. What does the forecast suggest about future severe workplace injury trends?

---

## 🔑 Key Findings

| Finding | Detail |
|---|---|
| 🏗️ **Construction Dominates** | Nearly 3x more severe injuries than the second-ranked broad industry |
| 🦴 **Fractures Most Common** | 34,598 fracture incidents — significantly outpacing all other injury types |
| 🏥 **High Hospitalization Rate** | 81.63% of all severe injuries resulted in hospitalization |
| 🤠 **Texas Leads All States** | 17,378 incidents — nearly 50% more than second-place Florida |
| 😷 **COVID-19 Impact** | Sharp 20%+ decline in 2020 — injuries have not returned to pre-pandemic levels |
| 📅 **Mid-Week Peak** | Tuesday and Wednesday consistently show the highest injury counts |
| 🖐️ **Fingers Most Affected** | Fingertips were the most commonly injured body part at 10,402 incidents |
| 🔗 **Strong Negative Correlation** | r = -0.79 between hospitalization and amputation confirms distinct injury mechanisms |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Microsoft Excel** | Data cleaning, statistical summary, pivot tables, hierarchical XLOOKUP for NAICS lookup |
| **MySQL / DBeaver** | Database schema, data exploration queries, 4-level hierarchical LEFT JOIN with COALESCE |
| **Python / Jupyter Notebook** | EDA, statistical analysis, skewness, outlier detection, 11 visualizations, forecasting |
| **Tableau Public** | 3 interactive dashboards with year and industry filters |

---

## 📊 Visualizations

### Python Charts
| Chart | Description |
|---|---|
| `outcomes_distribution.png` | Pie charts showing Yes vs No for Hospitalized, Amputation, Loss of Eye |
| `injuries_by_nature.png` | Top 15 injury types by NatureTitle |
| `top10_states.png` | Top 10 states by incident count |
| `correlation_heatmap.png` | Correlation matrix — Hospitalized vs Amputation vs Loss of Eye |
| `incidents_over_time.png` | Year over year trend with COVID-19 reference line |
| `injuries_by_day.png` | Incidents by day of week — weekday vs weekend contrast |
| `top20_industries.png` | Top 20 industries by hospitalizations — stacked bar |
| `top20_parent_industries.png` | Top 20 broad industry categories — stacked bar |
| `forecast.png` | Actual vs forecasted monthly incidents through April 2026 |
| `outliers_boxplot.png` | Box plots for outlier detection across all three outcome variables |
| `skewness_distribution.png` | Distribution histograms with skewness values |

### Tableau Dashboards
| Dashboard | Contents |
|---|---|
| **Dashboard 1 — Injury Overview** | KPI card, outcome pie charts, top 20 nature title and body part bar charts |
| **Dashboard 2 — Time Analysis** | Monthly trend, forecast, and day of week — all filterable by year |
| **Dashboard 3 — Industry Analysis** | Outcomes by state, by broad industry, and bubble chart |

---

## 📁 Repository Structure

```
Osha-Severe-Injury-Report_Capstone/
├── index.html                      ← Portfolio webpage (GitHub Pages)
├── README.md                       ← This file
├── documentation/                  ← Written report and PowerPoint presentation
│   └── README.md
├── excel/                          ← Excel analysis files hosted on OneDrive
│   └── README.md
├── sql_analysis_queries/           ← All SQL query files (.sql)
│   ├── data_cleaning.sql
│   ├── data_exploration.sql
│   ├── data_aggregation.sql
│   ├── data_join.sql
│   └── README.md
├── tableau/                        ← Tableau dashboard documentation
│   └── README.md
├── images/python/                  ← Python chart images
│   └── README.md
├── outcomes_distribution.png
├── injuries_by_nature.png
├── top10_states.png
├── correlation_heatmap.png
├── incidents_over_time.png
├── injuries_by_day.png
├── top20_industries.png
├── top20_parent_industries.png
├── forecast.png
├── outliers_boxplot.png
└── skewness_distribution.png
```

---

## 📈 Statistical Summary

| Metric | Hospitalized | Amputation | Loss of Eye |
|---|---|---|---|
| Total Yes | 85,971 | 27,788 | 35 |
| Total No | 19,346 | 77,529 | 105,282 |
| % Yes | 81.63% | 26.39% | 0.03% |
| Skewness | -1.24 | +1.08 | +54.83 |
| Outliers | 20,668 | 0 | 35 |

---

## 💡 Recommendations

1. **Root Cause Analysis** — High-risk industries should investigate the specific conditions driving elevated injury rates
2. **Targeted Safety Training** — Construction should focus on fracture/fall prevention; Manufacturing on amputation prevention
3. **Mid-Week Safety Focus** — Schedule additional safety checks on Tuesday, Wednesday, and Thursday
4. **Sustain Post-COVID Gains** — Identify and preserve practices that contributed to lower post-pandemic injury rates
5. **State-Level Focus** — Texas, Florida, Pennsylvania, and Ohio should be prioritized for OSHA outreach

---

## ⚠️ Limitations

- Dataset relies on employer-submitted reports — underreporting is possible
- 2.52% of records could not be matched to an industry name via NAICS lookup
- 2025 data only covers January through October — not directly comparable to full prior years
- Correlation findings identify patterns but do not establish causation

---

## 📚 Data Sources

- **Primary Dataset:** [OSHA Severe Injury Report Dashboard](https://www.osha.gov/severe-injury-reports)
- **Industry Reference:** [2022 NAICS Structure](https://www.census.gov/naics/?48967)
- **Regulatory Reference:** 29 CFR 1904.39 — OSHA Severe Injury Reporting Requirements

---

## 👩‍💼 About

**Mary Becker**  
FullStack Academy Data Analytics Certificate | 2026  
Master of Arts in Human Resource Management — Saint Mary's University of Minnesota  
SHRM Member | MVHRA Member  

[![GitHub](https://img.shields.io/badge/GitHub-M--AthaBecker-black?logo=github)](https://github.com/M-AthaBecker)
[![Tableau](https://img.shields.io/badge/Tableau-Public-blue?logo=tableau)](https://public.tableau.com/app/profile/mary.becker/viz/OshaSevereInjuryReportv1/Overview#1)
