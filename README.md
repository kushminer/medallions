# NYC Taxi Medallion Market Analysis

A comprehensive data analysis project examining NYC taxi medallion pricing, transaction patterns, and ride-sharing market dynamics from 2017-2023.

## Overview

This project analyzes the NYC taxi medallion market through two key lenses:
1. **Medallion Transfer Pricing**: Historical transaction data revealing market trends, foreclosure patterns, and pricing dynamics
2. **Operational Metrics**: Ride statistics, revenue patterns, and competitive analysis across different license classes (Yellow, Green, FHV)

## Key Findings

### Medallion Market Dynamics
- Analyzed 2,800+ medallion transactions from March 2017 to February 2023
- 64% of transactions were foreclosures, indicating significant market distress
- Tracked price volatility and identified key market trends
- Filtered analysis to focus on unrestricted medallion sales for accurate market valuation

### Ride-Sharing Competition Analysis
- Strong negative correlation (-0.649) between total NYC rides and Yellow taxi market share
- High-Volume FHV services show strong positive correlation (0.685) with total ride growth
- Yellow taxi unique vehicles represent declining percentage of total market as ride volume increases

### Operational Insights
- Yellow taxi: 0.814 correlation between vehicle availability and daily trip volume
- FHV services demonstrate varying levels of supply elasticity
- Market share shifts observable across different license classes over time

## Project Structure

```
medallions/
├── notebooks/
│   ├── 01_medallion_transfers.ipynb          # Medallion pricing & transaction analysis
│   ├── 02_monthly_visualizations.ipynb       # Comprehensive market visualizations
│   ├── 03_rides_per_class.ipynb             # License class comparison
│   ├── 04_percent_of_total.ipynb            # Market share analysis
│   ├── 05_time_series_modeling.ipynb        # Predictive modeling
│   └── 06_time_series_notes.ipynb           # Modeling documentation
├── data/
│   └── README.md                             # Data sources and descriptions
├── requirements.txt
└── README.md
```

## Data Sources

This analysis uses publicly available data from:
- **NYC Taxi & Limousine Commission (TLC)**: Monthly operational reports by license class
- **Medallion Transfer Data**: Historical transaction records including pricing and sale conditions

*Note: Data files are not included in this repository due to size constraints. See `data/README.md` for download instructions.*

## Methodology

### Data Processing
- Cleaned and standardized transaction data across 70+ monthly sheets
- Filtered for unrestricted medallion sales, excluding family transfers, partnerships, and estate sales
- Removed zero-price transactions (corporate restructuring, LLC conversions)
- Calculated per-medallion pricing for multi-medallion transactions

### Statistical Analysis
- Regression analysis (OLS) to quantify relationships between variables
- Correlation analysis to identify market dynamics
- Time series visualization to track trends
- Cross-license class comparative analysis

## Key Visualizations

The notebooks include:
- Time series plots of medallion pricing trends
- Transaction volume and type distribution over time
- Multi-class ride volume comparisons
- Market share evolution across license classes
- Correlation scatter plots for key relationships
- Price volatility and standard deviation analysis

## Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **NumPy**: Numerical computing
- **Statsmodels**: Statistical modeling and regression analysis
- **Jupyter Notebook**: Interactive analysis environment

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/medallions.git
cd medallions

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

## Usage

1. Obtain the required datasets (see `data/README.md`)
2. Place data files in the `data/` directory
3. Open notebooks in sequential order (01-06)
4. Run cells to reproduce analysis

## Analysis Highlights

### Transaction Type Distribution
- Foreclosures: 64.2%
- Standard Sales: 29.0%
- Estate Sales: 4.1%
- Bankruptcy: 2.2%

### Market Correlations
- **Yellow Taxi**: High correlation (0.814) between vehicle supply and trip demand
- **FHV High-Volume**: Strong growth correlation (0.685) with total market expansion
- **Yellow Market Share**: Significant negative correlation (-0.649) with total ride growth

## Future Work

- Predictive modeling for medallion valuations
- Integration of additional market factors (gas prices, regulatory changes)
- Analysis of COVID-19 pandemic impact on medallion values
- Deeper investigation into inactive medallion impact on market dynamics

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Data analysis and visualization by [Your Name]

## Acknowledgments

- NYC Taxi & Limousine Commission for public data access
- The open-source Python data science community

---

*This project was created as part of a data science portfolio to demonstrate skills in data cleaning, statistical analysis, visualization, and insight generation from real-world datasets.*
