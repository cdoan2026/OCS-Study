import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for matplotlib
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Read the data
print("Loading data...")
df = pd.read_excel('OCS_Working2.xlsx', sheet_name='all (3)')

# Data preprocessing
print("Processing data...")
df['YEAR'] = pd.to_datetime(df['EXP_GRAD_DATE'], errors='coerce').dt.year

# Current year based on the most recent complete data
# Using 2025 as reference (can adjust based on actual needs)
current_year = 2025

# Define time periods
periods = {
    '5 years': current_year - 5,
    '10 years': current_year - 10,
    '15 years': current_year - 15,
    '20 years': current_year - 20
}

print(f"\nAnalysis periods:")
for period, start_year in periods.items():
    print(f"  {period}: {start_year} - {current_year}")

# Create output directory for visualizations
import os
os.makedirs('visualizations', exist_ok=True)

# ============================================================================
# 1. TOP 20 PROGRAMS FOR DIFFERENT TIME PERIODS
# ============================================================================
print("\n" + "="*80)
print("Creating Program Visualizations...")
print("="*80)

# Filter out null programs
df_programs = df[df['PROGRAM'].notna()].copy()

# Create subplot figure for programs
fig_programs = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        f'Top 20 Programs (Last 5 Years: {periods["5 years"]}-{current_year})',
        f'Top 20 Programs (Last 10 Years: {periods["10 years"]}-{current_year})',
        f'Top 20 Programs (Last 15 Years: {periods["15 years"]}-{current_year})',
        f'Top 20 Programs (Last 20 Years: {periods["20 years"]}-{current_year})'
    ),
    specs=[[{"type": "bar"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "bar"}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
row_col_pairs = [(1, 1), (1, 2), (2, 1), (2, 2)]

for idx, (period_name, start_year) in enumerate(periods.items()):
    # Filter data for this period
    period_data = df_programs[df_programs['YEAR'] >= start_year]

    # Get top 20 programs
    top_programs = period_data['PROGRAM'].value_counts().head(20)

    row, col = row_col_pairs[idx]

    fig_programs.add_trace(
        go.Bar(
            y=top_programs.index[::-1],  # Reverse for better visualization
            x=top_programs.values[::-1],
            orientation='h',
            marker=dict(color=colors[idx]),
            text=top_programs.values[::-1],
            textposition='auto',
            name=period_name,
            showlegend=False
        ),
        row=row, col=col
    )

fig_programs.update_layout(
    title_text="Top 20 Most Popular Programs by Time Period",
    title_font_size=20,
    height=1000,
    showlegend=False
)

fig_programs.update_xaxes(title_text="Number of Participants")
fig_programs.update_yaxes(title_text="Program")

fig_programs.write_html('visualizations/programs_by_period.html')
print("✓ Created: visualizations/programs_by_period.html")

# ============================================================================
# 2. TOP 20 COUNTRIES FOR DIFFERENT TIME PERIODS
# ============================================================================
print("\n" + "="*80)
print("Creating Country Visualizations...")
print("="*80)

# Filter out null countries
df_countries = df[df['COUNTRY'].notna()].copy()

# Create subplot figure for countries
fig_countries = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        f'Top 20 Countries (Last 5 Years: {periods["5 years"]}-{current_year})',
        f'Top 20 Countries (Last 10 Years: {periods["10 years"]}-{current_year})',
        f'Top 20 Countries (Last 15 Years: {periods["15 years"]}-{current_year})',
        f'Top 20 Countries (Last 20 Years: {periods["20 years"]}-{current_year})'
    ),
    specs=[[{"type": "bar"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "bar"}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)

for idx, (period_name, start_year) in enumerate(periods.items()):
    # Filter data for this period
    period_data = df_countries[df_countries['YEAR'] >= start_year]

    # Get top 20 countries
    top_countries = period_data['COUNTRY'].value_counts().head(20)

    row, col = row_col_pairs[idx]

    fig_countries.add_trace(
        go.Bar(
            y=top_countries.index[::-1],
            x=top_countries.values[::-1],
            orientation='h',
            marker=dict(color=colors[idx]),
            text=top_countries.values[::-1],
            textposition='auto',
            name=period_name,
            showlegend=False
        ),
        row=row, col=col
    )

fig_countries.update_layout(
    title_text="Top 20 Most Popular Countries by Time Period",
    title_font_size=20,
    height=1000,
    showlegend=False
)

fig_countries.update_xaxes(title_text="Number of Participants")
fig_countries.update_yaxes(title_text="Country")

fig_countries.write_html('visualizations/countries_by_period.html')
print("✓ Created: visualizations/countries_by_period.html")

# ============================================================================
# 3. TOP DESTINATIONS FOR MAJORS
# ============================================================================
print("\n" + "="*80)
print("Creating Major Destinations Visualizations...")
print("="*80)

# Get top 10 majors overall
df_majors = df[df['MAJOR'].notna() & df['COUNTRY'].notna()].copy()
top_majors = df_majors['MAJOR'].value_counts().head(10).index.tolist()

# Create visualizations for each time period
for period_name, start_year in periods.items():
    period_data = df_majors[df_majors['YEAR'] >= start_year]

    # Create a matrix of major vs country
    major_dest_data = []

    for major in top_majors:
        major_data = period_data[period_data['MAJOR'] == major]
        top_dest = major_data['COUNTRY'].value_counts().head(5)

        for country, count in top_dest.items():
            major_dest_data.append({
                'Major': major,
                'Country': country,
                'Count': count
            })

    if major_dest_data:
        df_major_dest = pd.DataFrame(major_dest_data)

        # Create grouped bar chart
        fig = px.bar(
            df_major_dest,
            x='Major',
            y='Count',
            color='Country',
            title=f'Top Destinations by Major ({period_name}: {start_year}-{current_year})',
            barmode='group',
            height=600
        )

        fig.update_layout(
            xaxis_tickangle=-45,
            xaxis_title="Major",
            yaxis_title="Number of Participants",
            legend_title="Country"
        )

        filename = f'visualizations/major_destinations_{period_name.replace(" ", "_")}.html'
        fig.write_html(filename)
        print(f"✓ Created: {filename}")

# ============================================================================
# 4. TRENDS IN PARTICIPATION BY SEMESTER
# ============================================================================
print("\n" + "="*80)
print("Creating Semester Participation Trends...")
print("="*80)

# Parse semester information
def parse_semester(sem_text):
    """Extract year and semester type from SEMESTER_TEXT"""
    if pd.isna(sem_text):
        return None, None

    # Handle different formats
    parts = str(sem_text).split()
    if len(parts) >= 2:
        semester_type = parts[0]  # Fall, Spring, Winter Term, etc.
        year_part = parts[-1]  # Last part should be year

        # Extract year
        if '-' in year_part:
            year = int(year_part.split('-')[0])
        else:
            year = int(year_part) if year_part.isdigit() else None

        return semester_type, year

    return None, None

df['SEMESTER_TYPE'], df['SEMESTER_YEAR'] = zip(*df['SEMESTER_TEXT'].apply(parse_semester))

# Filter valid data
df_semester = df[df['SEMESTER_YEAR'].notna()].copy()
df_semester = df_semester[df_semester['SEMESTER_YEAR'] >= 1990]  # Filter reasonable years

# Group by semester and year
semester_counts = df_semester.groupby(['SEMESTER_YEAR', 'SEMESTER_TYPE']).size().reset_index(name='Count')

# Create line plot for trends
fig_trends = go.Figure()

# Get unique semester types
semester_types = semester_counts['SEMESTER_TYPE'].unique()

for sem_type in semester_types:
    sem_data = semester_counts[semester_counts['SEMESTER_TYPE'] == sem_type]
    sem_data = sem_data.sort_values('SEMESTER_YEAR')

    fig_trends.add_trace(go.Scatter(
        x=sem_data['SEMESTER_YEAR'],
        y=sem_data['Count'],
        mode='lines+markers',
        name=sem_type,
        line=dict(width=2),
        marker=dict(size=6)
    ))

fig_trends.update_layout(
    title="Participation Trends by Semester Over Time",
    xaxis_title="Year",
    yaxis_title="Number of Participants",
    height=600,
    hovermode='x unified',
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="right",
        x=1
    )
)

fig_trends.write_html('visualizations/semester_trends.html')
print("✓ Created: visualizations/semester_trends.html")

# Overall participation trend
overall_trend = df_semester.groupby('SEMESTER_YEAR').size().reset_index(name='Count')
overall_trend = overall_trend.sort_values('SEMESTER_YEAR')

fig_overall = go.Figure()

fig_overall.add_trace(go.Scatter(
    x=overall_trend['SEMESTER_YEAR'],
    y=overall_trend['Count'],
    mode='lines+markers',
    name='Total Participation',
    line=dict(color='#FF6B6B', width=3),
    marker=dict(size=8),
    fill='tozeroy',
    fillcolor='rgba(255, 107, 107, 0.2)'
))

fig_overall.update_layout(
    title="Overall Participation Trend by Year",
    xaxis_title="Year",
    yaxis_title="Number of Participants",
    height=600,
    hovermode='x'
)

fig_overall.write_html('visualizations/overall_participation_trend.html')
print("✓ Created: visualizations/overall_participation_trend.html")

# ============================================================================
# 5. COMBINED DASHBOARD
# ============================================================================
print("\n" + "="*80)
print("Creating Combined Dashboard...")
print("="*80)

# Create a comprehensive HTML dashboard
dashboard_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OCS Study Abroad Data Visualization Dashboard</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .nav {{
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .nav a {{
            text-decoration: none;
            color: #667eea;
            font-weight: bold;
            margin-right: 20px;
            padding: 8px 15px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}
        .nav a:hover {{
            background-color: #f0f0f0;
        }}
        .section {{
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        .section h3 {{
            color: #764ba2;
            margin-top: 25px;
        }}
        .viz-link {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 10px 10px 0;
            transition: transform 0.2s;
        }}
        .viz-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .stat-card h3 {{
            margin: 0;
            font-size: 2em;
            color: white;
        }}
        .stat-card p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        iframe {{
            width: 100%;
            height: 700px;
            border: none;
            border-radius: 5px;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 OCS Study Abroad Data Visualization Dashboard</h1>
        <p>DePauw University - Comprehensive Analysis</p>
        <p style="font-size: 0.9em; margin-top: 15px;">
            Analysis Period: {min(df['YEAR'].dropna())} - {max(df['YEAR'].dropna())} |
            Total Records: {len(df):,}
        </p>
    </div>

    <div class="nav">
        <a href="#programs">Programs</a>
        <a href="#countries">Countries</a>
        <a href="#majors">Majors & Destinations</a>
        <a href="#trends">Semester Trends</a>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <h3>{len(df):,}</h3>
            <p>Total Participants</p>
        </div>
        <div class="stat-card">
            <h3>{df['PROGRAM'].nunique()}</h3>
            <p>Unique Programs</p>
        </div>
        <div class="stat-card">
            <h3>{df['COUNTRY'].nunique()}</h3>
            <p>Countries</p>
        </div>
        <div class="stat-card">
            <h3>{df['MAJOR'].nunique()}</h3>
            <p>Majors</p>
        </div>
    </div>

    <div class="section" id="programs">
        <h2>📚 Top 20 Most Popular Programs</h2>
        <p>Analysis of the most popular study abroad programs across different time periods (5, 10, 15, and 20 years).</p>
        <a href="programs_by_period.html" class="viz-link" target="_blank">View Interactive Visualization →</a>
    </div>

    <div class="section" id="countries">
        <h2>🌍 Top 20 Most Popular Countries</h2>
        <p>Geographic distribution of study abroad destinations across different time periods.</p>
        <a href="countries_by_period.html" class="viz-link" target="_blank">View Interactive Visualization →</a>
    </div>

    <div class="section" id="majors">
        <h2>🎓 Top Destinations by Major</h2>
        <p>Analysis of preferred study abroad destinations for top majors at DePauw University.</p>
        <h3>By Time Period:</h3>
        <a href="major_destinations_5_years.html" class="viz-link" target="_blank">Last 5 Years</a>
        <a href="major_destinations_10_years.html" class="viz-link" target="_blank">Last 10 Years</a>
        <a href="major_destinations_15_years.html" class="viz-link" target="_blank">Last 15 Years</a>
        <a href="major_destinations_20_years.html" class="viz-link" target="_blank">Last 20 Years</a>
    </div>

    <div class="section" id="trends">
        <h2>📈 Participation Trends by Semester</h2>
        <p>Historical trends showing participation patterns across different semesters and years.</p>
        <a href="semester_trends.html" class="viz-link" target="_blank">View Semester-wise Trends →</a>
        <a href="overall_participation_trend.html" class="viz-link" target="_blank">View Overall Trend →</a>
    </div>

    <div class="section">
        <h2>📊 All Visualizations</h2>
        <p>Quick access to all interactive visualizations:</p>
        <ul style="line-height: 2;">
            <li><a href="programs_by_period.html" target="_blank">Top 20 Programs by Period</a></li>
            <li><a href="countries_by_period.html" target="_blank">Top 20 Countries by Period</a></li>
            <li><a href="major_destinations_5_years.html" target="_blank">Major Destinations (5 Years)</a></li>
            <li><a href="major_destinations_10_years.html" target="_blank">Major Destinations (10 Years)</a></li>
            <li><a href="major_destinations_15_years.html" target="_blank">Major Destinations (15 Years)</a></li>
            <li><a href="major_destinations_20_years.html" target="_blank">Major Destinations (20 Years)</a></li>
            <li><a href="semester_trends.html" target="_blank">Semester Participation Trends</a></li>
            <li><a href="overall_participation_trend.html" target="_blank">Overall Participation Trend</a></li>
        </ul>
    </div>

    <div class="footer">
        <p>Generated on {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}</p>
        <p>DePauw University - Office of Off-Campus Study</p>
    </div>
</body>
</html>
"""

with open('visualizations/index.html', 'w') as f:
    f.write(dashboard_html)

print("✓ Created: visualizations/index.html (Main Dashboard)")

# ============================================================================
# 6. CREATE SUMMARY STATISTICS
# ============================================================================
print("\n" + "="*80)
print("Generating Summary Statistics...")
print("="*80)

summary_stats = f"""
OCS STUDY ABROAD DATA - SUMMARY STATISTICS
============================================
Generated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}

DATASET OVERVIEW:
-----------------
Total Records: {len(df):,}
Date Range: {int(df['YEAR'].min())} - {int(df['YEAR'].max())}
Unique Programs: {df['PROGRAM'].nunique()}
Unique Countries: {df['COUNTRY'].nunique()}
Unique Majors: {df['MAJOR'].nunique()}

TOP 10 PROGRAMS (ALL TIME):
---------------------------
{df[df['PROGRAM'].notna()]['PROGRAM'].value_counts().head(10).to_string()}

TOP 10 COUNTRIES (ALL TIME):
----------------------------
{df[df['COUNTRY'].notna()]['COUNTRY'].value_counts().head(10).to_string()}

TOP 10 MAJORS (ALL TIME):
-------------------------
{df[df['MAJOR'].notna()]['MAJOR'].value_counts().head(10).to_string()}

PARTICIPATION BY TIME PERIOD:
-----------------------------
Last 5 years ({periods['5 years']}-{current_year}): {len(df[df['YEAR'] >= periods['5 years']]):,} participants
Last 10 years ({periods['10 years']}-{current_year}): {len(df[df['YEAR'] >= periods['10 years']]):,} participants
Last 15 years ({periods['15 years']}-{current_year}): {len(df[df['YEAR'] >= periods['15 years']]):,} participants
Last 20 years ({periods['20 years']}-{current_year}): {len(df[df['YEAR'] >= periods['20 years']]):,} participants
"""

with open('visualizations/summary_statistics.txt', 'w') as f:
    f.write(summary_stats)

print("✓ Created: visualizations/summary_statistics.txt")

print("\n" + "="*80)
print("✅ ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("="*80)
print("\nGenerated files in 'visualizations/' directory:")
print("  1. index.html - Main Dashboard (START HERE)")
print("  2. programs_by_period.html - Top 20 Programs")
print("  3. countries_by_period.html - Top 20 Countries")
print("  4. major_destinations_*.html - Major Destinations (4 files)")
print("  5. semester_trends.html - Semester Trends")
print("  6. overall_participation_trend.html - Overall Trend")
print("  7. summary_statistics.txt - Summary Statistics")
print("\nOpen 'visualizations/index.html' in your web browser to view the dashboard!")
print("="*80)
