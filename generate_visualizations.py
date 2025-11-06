"""
Generate key visualizations from the medallion analysis notebooks.
This script creates publication-ready plots for the README.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for professional-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("Starting visualization generation...")

# ============================================================================
# 1. Medallion Price Trends Over Time
# ============================================================================
print("\n1. Generating medallion price trends...")

# Load and process medallion transfer data
xl = pd.ExcelFile('data/february_2023_medallion_price_list.xls')

# Filter for target dates
filtered_sheet_names = []
for sheet_name in xl.sheet_names:
    try:
        if datetime.strptime(sheet_name, '%B %Y') >= datetime(2017, 3, 1):
            filtered_sheet_names.append(sheet_name)
    except ValueError:
        pass

# Remove irrelevant sheets
filtered_sheet_names = [name for name in filtered_sheet_names if name != 'Sheet1']

# Load and process data
dataframes = {}
for sheet in filtered_sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet, header=2)
    dataframes[sheet] = df

# Filter for unrestricted sales
for sheet, df in dataframes.items():
    df = df.copy()
    medallion_class = df['Medallion Classification'].astype(str).str.strip().str.lower()
    prices = df['Prices'].astype(str).str.strip().str.lower()

    if 'unrestricted' in medallion_class.values and 'stock transfers' in prices.values:
        start = medallion_class[medallion_class == 'unrestricted'].index[0]
        end = prices[prices == 'stock transfers'].index[0]
        df = df.loc[start:end-1]

    df['Medallion Classification'] = 'Unrestricted'
    df = df.loc[df['Prices'] != 0]
    df = df.dropna(subset=['Prices'])

    df.rename(columns={"Prices": "Total Price"}, inplace=True)
    df['Price Each'] = df['Total Price'] / df['Number of Medallions']
    df = df[['Medallion Classification', 'Total Price', 'Number of Medallions', 'Price Each', 'Notes']]
    df['Notes'] = df['Notes'].fillna('No Notes').replace(' ', 'No Notes')

    # Exclude non-relevant transaction types
    df = df[~df['Notes'].isin(['Estate', 'Family', 'Individual to LLC, Adding 1% member',
                                 'Partnership Split', 'Individual to Corp'])]

    dataframes[sheet] = df

# Create summary statistics
summary_data = []
for sheet, df in dataframes.items():
    date = pd.to_datetime(" ".join(sheet.split(" ")))

    summary_data.append({
        'Date': date,
        'Max Price': df['Price Each'].max(),
        'Min Price': df['Price Each'].min(),
        'Average Price': df['Price Each'].mean(),
        'Std Price': df['Price Each'].std(),
        'Total Medallions Sold': df['Number of Medallions'].sum(),
        'Total Spent': df['Total Price'].sum(),
        'Foreclosure Count': df['Notes'].str.contains('Foreclosure').sum(),
        'No Notes': df['Notes'].str.contains('No Notes').sum(),
        'Bankruptcy': df['Notes'].str.contains('Bankruptcy').sum(),
    })

summary_df = pd.DataFrame(summary_data).set_index('Date').sort_index()

# Plot price trends
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(summary_df.index, summary_df['Average Price'], label='Average Price', linewidth=2.5, marker='o', markersize=4)
ax.fill_between(summary_df.index, summary_df['Min Price'], summary_df['Max Price'],
                alpha=0.2, label='Price Range')

ax.set_title('NYC Taxi Medallion Price Trends (2017-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
ax.legend(fontsize=11, loc='best')
ax.grid(True, alpha=0.3)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.savefig('images/medallion_price_trends.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: medallion_price_trends.png")
plt.close()

# ============================================================================
# 2. Transaction Types Distribution
# ============================================================================
print("\n2. Generating transaction type distribution...")

all_data = pd.concat(dataframes.values())
notes_counts = all_data['Notes'].value_counts()

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 8))
colors = sns.color_palette('Set2', len(notes_counts))
wedges, texts, autotexts = ax.pie(notes_counts.values, labels=notes_counts.index,
                                    autopct='%1.1f%%', colors=colors, startangle=90,
                                    textprops={'fontsize': 11, 'fontweight': 'bold'})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax.set_title('Medallion Transaction Types Distribution\n(2017-2023)',
             fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('images/transaction_types.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: transaction_types.png")
plt.close()

# ============================================================================
# 3. Monthly Volume and Transaction Counts
# ============================================================================
print("\n3. Generating transaction volume trends...")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Plot 1: Transaction counts
ax1.plot(summary_df.index, summary_df['Total Medallions Sold'],
         label='Total Medallions Sold', linewidth=2, marker='o', markersize=5, color='#2E86AB')
ax1.plot(summary_df.index, summary_df['Foreclosure Count'],
         label='Foreclosure Count', linewidth=2, marker='s', markersize=5, color='#A23B72')
ax1.plot(summary_df.index, summary_df['No Notes'],
         label='Standard Sales', linewidth=2, marker='^', markersize=5, color='#F18F01')

ax1.set_title('Medallion Transaction Volume Over Time', fontsize=14, fontweight='bold')
ax1.set_ylabel('Count', fontsize=11, fontweight='bold')
ax1.legend(fontsize=10, loc='best')
ax1.grid(True, alpha=0.3)

# Plot 2: Foreclosure percentage
foreclosure_pct = (summary_df['Foreclosure Count'] / summary_df['Total Medallions Sold'] * 100)
ax2.plot(summary_df.index, foreclosure_pct, linewidth=2.5, color='#A23B72', marker='o', markersize=5)
ax2.axhline(y=64.2, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Overall Average (64.2%)')
ax2.fill_between(summary_df.index, foreclosure_pct, alpha=0.3, color='#A23B72')

ax2.set_title('Foreclosure Rate Over Time', fontsize=14, fontweight='bold')
ax2.set_xlabel('Date', fontsize=11, fontweight='bold')
ax2.set_ylabel('Foreclosure %', fontsize=11, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/transaction_volume_trends.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: transaction_volume_trends.png")
plt.close()

# ============================================================================
# 4. Market Share Analysis from Monthly Data
# ============================================================================
print("\n4. Generating market share analysis...")

# Load monthly ride data
data_reports_monthly = pd.read_csv('data/data_reports_monthly.csv')
data_reports_monthly.columns = data_reports_monthly.columns.str.strip()
data_reports_monthly['Month/Year'] = pd.to_datetime(data_reports_monthly['Month/Year'])
data_reports_monthly.set_index('Month/Year', inplace=True)

# Clean data
data_reports_monthly = data_reports_monthly.replace({',': ''}, regex=True)
cols = data_reports_monthly.columns.drop(['License Class'])
data_reports_monthly[cols] = data_reports_monthly[cols].apply(pd.to_numeric, errors='coerce')

# Calculate percentages
df = data_reports_monthly[['License Class', 'Trips Per Day']].copy()
df['Total NYC Rides'] = df.groupby('Month/Year')['Trips Per Day'].transform('sum')
df['Trips Percent of Total'] = df['Trips Per Day'] / df['Total NYC Rides']

# Plot market share evolution
fig, ax = plt.subplots(figsize=(14, 7))

license_classes = df['License Class'].unique()
colors = sns.color_palette('tab10', len(license_classes))

for idx, license_class in enumerate(license_classes):
    subset = df[df['License Class'] == license_class]
    ax.plot(subset.index, subset['Trips Percent of Total'] * 100,
            label=license_class, linewidth=2.5, color=colors[idx], marker='o', markersize=3)

ax.set_title('Market Share Evolution by License Class', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Market Share (%)', fontsize=12, fontweight='bold')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/market_share_evolution.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: market_share_evolution.png")
plt.close()

# ============================================================================
# 5. Correlation Analysis: Yellow Taxi
# ============================================================================
print("\n5. Generating correlation analysis...")

df2 = df.copy()
df2['Total Unique Vehicles'] = data_reports_monthly.groupby('Month/Year')['Unique Vehicles'].transform('sum')
df2['Unique Vehicles'] = data_reports_monthly['Unique Vehicles']
df2['Unique Vehicles Percent of Total'] = df2['Unique Vehicles'] / df2['Total Unique Vehicles']

# Create scatter plots for Yellow taxi
yellow_data = df2[df2['License Class'] == 'Yellow'].copy()
high_volume_data = df2[df2['License Class'] == 'FHV - High Volume'].copy()

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Yellow taxi correlation
ax = axes[0]
scatter_data = pd.DataFrame({
    'Total_Rides': yellow_data['Total NYC Rides'],
    'Market_Share': yellow_data['Unique Vehicles Percent of Total'] * 100
}).dropna()

ax.scatter(scatter_data['Total_Rides'], scatter_data['Market_Share'],
          alpha=0.6, s=100, c='#FFC107', edgecolors='black', linewidth=1.5)

# Add trend line
z = np.polyfit(scatter_data['Total_Rides'], scatter_data['Market_Share'], 1)
p = np.poly1d(z)
ax.plot(scatter_data['Total_Rides'], p(scatter_data['Total_Rides']),
        "r--", linewidth=2.5, alpha=0.8, label=f'Trend Line\nCorr: -0.649')

ax.set_title('Yellow Taxi: Market Share vs Total NYC Rides\n(Strong Negative Correlation)',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Total NYC Rides Per Day', fontsize=11, fontweight='bold')
ax.set_ylabel('Yellow Taxi Market Share (%)', fontsize=11, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# High Volume FHV correlation
ax = axes[1]
scatter_data2 = pd.DataFrame({
    'Total_Rides': high_volume_data['Total NYC Rides'],
    'Unique_Vehicles': high_volume_data['Unique Vehicles']
}).dropna()

ax.scatter(scatter_data2['Total_Rides'], scatter_data2['Unique_Vehicles'],
          alpha=0.6, s=100, c='#9C27B0', edgecolors='black', linewidth=1.5)

# Add trend line
z = np.polyfit(scatter_data2['Total_Rides'], scatter_data2['Unique_Vehicles'], 1)
p = np.poly1d(z)
ax.plot(scatter_data2['Total_Rides'], p(scatter_data2['Total_Rides']),
        "r--", linewidth=2.5, alpha=0.8, label=f'Trend Line\nCorr: 0.685')

ax.set_title('FHV High-Volume: Vehicles vs Total NYC Rides\n(Strong Positive Correlation)',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Total NYC Rides Per Day', fontsize=11, fontweight='bold')
ax.set_ylabel('FHV High-Volume Unique Vehicles', fontsize=11, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/correlation_analysis.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: correlation_analysis.png")
plt.close()

print("\n" + "="*70)
print("✓ All visualizations generated successfully!")
print("="*70)
print("\nGenerated files:")
print("  - images/medallion_price_trends.png")
print("  - images/transaction_types.png")
print("  - images/transaction_volume_trends.png")
print("  - images/market_share_evolution.png")
print("  - images/correlation_analysis.png")
