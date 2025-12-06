# OCS Study Abroad Data Visualization Dashboard

## 📊 Overview

This repository contains comprehensive data visualizations for DePauw University's Off-Campus Study (OCS) program. The analysis covers **9,104 student participation records** spanning from **1999 to 2028**, analyzing patterns across **673 programs** in **74 countries** for **73 different majors**.

## 🎯 Visualizations Included

The dashboard provides insights into four key areas:

### 1. **Top 20 Most Popular Programs**
- Analysis across 5, 10, 15, and 20-year periods
- Interactive horizontal bar charts showing participation trends
- Time periods analyzed:
  - Last 5 years (2020-2025)
  - Last 10 years (2015-2025)
  - Last 15 years (2010-2025)
  - Last 20 years (2005-2025)

### 2. **Top 20 Most Popular Countries**
- Geographic distribution of study abroad destinations
- Comparative analysis across different time periods
- Identifies emerging and declining destination trends

### 3. **Top Destinations by Major**
- Shows preferred study abroad countries for top 10 majors
- Separate visualizations for each time period (5, 10, 15, 20 years)
- Helps understand academic program preferences

### 4. **Participation Trends by Semester**
- Historical trends showing participation patterns
- Breakdown by semester type (Fall, Spring, Winter Term, etc.)
- Overall participation trend over time

## 🚀 Quick Start

### Viewing the Dashboard

1. **Open the main dashboard:**
   ```bash
   open visualizations/index.html
   ```
   Or simply double-click `visualizations/index.html` in your file browser

2. **The dashboard provides:**
   - Summary statistics
   - Quick navigation to all visualizations
   - Interactive charts (zoom, pan, hover for details)

### File Structure

```
OCS-Study/
├── OCS_Working2.xlsx                    # Original dataset
├── create_visualizations.py             # Visualization generator script
├── README.md                            # This file
└── visualizations/
    ├── index.html                       # Main dashboard (START HERE)
    ├── programs_by_period.html          # Top 20 programs analysis
    ├── countries_by_period.html         # Top 20 countries analysis
    ├── major_destinations_5_years.html  # Major destinations (5 years)
    ├── major_destinations_10_years.html # Major destinations (10 years)
    ├── major_destinations_15_years.html # Major destinations (15 years)
    ├── major_destinations_20_years.html # Major destinations (20 years)
    ├── semester_trends.html             # Semester participation trends
    ├── overall_participation_trend.html # Overall trend over time
    └── summary_statistics.txt           # Statistical summary
```

## 📈 Key Findings

### Top Programs (All Time)
1. IES - 137 participants
2. Chamber Symphony Tour - 125 participants
3. Servicio - 118 participants
4. Life After Mandela - 97 participants
5. CIEE - 86 participants

### Top Destinations (All Time)
1. England - 306 participants
2. United States - 222 participants
3. Spain - 197 participants
4. Italy - 144 participants
5. Scotland - 136 participants

### Top Majors Participating in Study Abroad
1. Communication - 1,158 participants
2. English - 999 participants
3. Economics - 873 participants
4. Psychology - 494 participants
5. Political Science - 477 participants

### Participation by Time Period
- **Last 5 years (2020-2025):** 2,614 participants
- **Last 10 years (2015-2025):** 4,765 participants
- **Last 15 years (2010-2025):** 5,436 participants
- **Last 20 years (2005-2025):** 6,301 participants

## 🔧 Regenerating Visualizations

If you need to regenerate the visualizations with updated data:

1. **Ensure Python dependencies are installed:**
   ```bash
   pip install pandas openpyxl matplotlib seaborn plotly
   ```

2. **Run the visualization script:**
   ```bash
   python3 create_visualizations.py
   ```

3. **Output will be generated in the `visualizations/` directory**

## 📊 Visualization Features

All interactive visualizations include:
- **Zoom & Pan:** Click and drag to zoom into specific areas
- **Hover Details:** Hover over data points for detailed information
- **Download:** Save visualizations as PNG files (camera icon)
- **Reset Axes:** Double-click to reset view
- **Toggle Items:** Click legend items to show/hide data series

## 💡 Use Cases

These visualizations can be used for:
- **Strategic Planning:** Identify trending programs and destinations
- **Student Advising:** Help students choose programs based on major
- **Marketing & Recruitment:** Understand program popularity trends
- **Resource Allocation:** Allocate resources to popular programs/destinations
- **Historical Analysis:** Track participation trends over time
- **Academic Integration:** Understand which majors participate most

## 📝 Data Notes

- **Dataset Size:** 9,104 records
- **Date Range:** 1999-2028
- **Programs:** 673 unique programs
- **Countries:** 74 unique countries
- **Majors:** 73 unique majors
- **Null Values:** Some records have missing data in PROGRAM, LOCATION, or COUNTRY fields

## 🤝 Contributing

To update or enhance the visualizations:

1. Modify `create_visualizations.py`
2. Run the script to regenerate visualizations
3. Commit changes to the repository

## 📧 Questions or Issues?

For questions about the data or visualizations, please contact the DePauw University Office of Off-Campus Study.

---
**Data Source:** OCS_Working2.xlsx
**Visualization Tool:** Plotly

