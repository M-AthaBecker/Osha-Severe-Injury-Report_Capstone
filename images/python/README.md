# 🐍 Python Visualizations — OSHA Severe Injury Report

This folder contains all chart images generated from the Python/Jupyter Notebook analysis of the OSHA Severe Injury Report dataset (105,317 records | January 2015 – October 2025).

---

## 📊 Chart Index

| File | Chart Type | Description | Key Finding |
|---|---|---|---|
| `outcomes_distribution.png` | Pie Charts (3) | Yes vs No outcome breakdown for Hospitalized, Amputation, and Loss of Eye | 81.63% hospitalized, 26.39% amputation, 0.03% loss of eye |
| `injuries_by_nature.png` | Horizontal Bar | Top 15 injury types by NatureTitle | Fractures lead at 34,598 — nearly 50% more than Amputations at 23,449 |
| `top10_states.png` | Horizontal Bar | Top 10 states by total incident count | Texas leads with 17,378 — nearly 50% more than Florida |
| `correlation_heatmap.png` | Heatmap | Correlation matrix between all three outcome variables | Strong negative correlation of -0.79 between Hospitalized and Amputation |
| `incidents_over_time.png` | Line Chart | Yearly incident counts 2015–2025 with COVID-19 reference line | Peak in 2018 at 11,156 — sharp COVID drop in 2020 — no full recovery |
| `injuries_by_day.png` | Bar Chart | Incident counts by day of week | Tuesday (19,660) and Wednesday (19,718) are peak injury days |
| `top20_industries.png` | Stacked Bar | Top 20 NAICS industries by hospitalizations | General Medical leads — construction trades dominate the list |
| `top20_parent_industries.png` | Stacked Bar | Top 20 broad industry categories by hospitalizations | Construction records nearly 3x more incidents than second place |
| `forecast.png` | Line Chart | Historical monthly incidents with linear trend and 6-month forecast | Monthly incidents projected to stabilize at 700-800 through early 2026 |
| `outliers_boxplot.png` | Box Plots (3) | Outlier detection for all three outcome variables | 20,668 hospitalization outliers representing multi-employee incidents |
| `skewness_distribution.png` | Histograms (3) | Distribution and skewness of numeric outcome columns | Loss of Eye has extreme skewness of 54.83 reflecting its 0.03% occurrence rate |

---

## 🛠️ Generated With

| Library | Version |
|---|---|
| `matplotlib` | 3.x |
| `seaborn` | 0.x |
| `pandas` | 2.x |
| `numpy` | 1.x |

All charts saved at **150 DPI** using `plt.savefig()` with `seaborn white` style — no grid lines.

---

## 📂 Related

- Full Python analysis → see `/python/` folder
- Interactive Tableau dashboards → [Tableau Public](https://public.tableau.com/app/profile/m.athaBecker)
- Portfolio webpage → [GitHub Pages](https://M-AthaBecker.github.io/Osha-Severe-Injury-Report_Capstone)
