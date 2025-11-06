<div align="center">

# 🚕 NYC Taxi Medallion Market Analysis

### A comprehensive data science project analyzing taxi medallion economics and ride-sharing market dynamics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Data Science](https://img.shields.io/badge/Data-Science-green.svg)](https://github.com/topics/data-science)

**Period Analyzed:** March 2017 - February 2023 | **Transactions:** 2,800+ | **Data Points:** 100,000+

[View Notebooks](notebooks/) • [Data Sources](data/README.md) • [Contributing](CONTRIBUTING.md)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Findings](#-key-findings)
- [Project Structure](#-project-structure)
- [Notebooks Guide](#-notebooks-guide)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Methodology](#-methodology)
- [Analysis Highlights](#-analysis-highlights)
- [Future Work](#-future-work)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes the NYC taxi medallion market through two key lenses:

1. **Medallion Transfer Pricing**: Historical transaction data revealing market trends, foreclosure patterns, and pricing dynamics
2. **Operational Metrics**: Ride statistics, revenue patterns, and competitive analysis across different license classes (Yellow, Green, FHV)

### Business Context

NYC taxi medallions were once valued at over $1 million but have experienced dramatic price decline due to ride-sharing competition. This analysis quantifies market distress, identifies competitive dynamics, and explores the relationship between overall market growth and traditional taxi operations.

## 🔍 Key Findings

### 💰 Medallion Market Dynamics

<table>
<tr>
<td width="50%">

**Market Distress Indicators**
- 📊 **2,800+** transactions analyzed
- 🏚️ **64%** were foreclosures
- 📉 Significant price volatility observed
- 🎯 Focus on unrestricted sales for accuracy

</td>
<td width="50%">

**Transaction Breakdown**
- Foreclosures: **64.2%**
- Standard Sales: **29.0%**
- Estate Sales: **4.1%**
- Bankruptcy: **2.2%**

</td>
</tr>
</table>

### 📈 Ride-Sharing Competition Analysis

> **Critical Finding**: As total NYC rides increase, Yellow taxi market share decreases

| License Class | Correlation with Total Market | Interpretation |
|--------------|------------------------------|----------------|
| **Yellow Taxi** | **-0.649** | Strong negative - losing market share as market grows |
| **FHV High-Volume** | **+0.685** | Strong positive - capturing market growth |
| **Yellow Supply/Demand** | **+0.814** | High correlation between vehicles available and trips |

### 💡 Strategic Insights

- 🚖 **Yellow taxis** demonstrate declining market position despite overall ride growth
- 🚗 **High-Volume FHV** services (Uber/Lyft) capture the majority of market expansion
- 📊 Traditional taxi operations show **supply elasticity** - fewer vehicles as market share declines
- ⚠️ Medallion values reflect structural market shift, not temporary disruption

## 📁 Project Structure

```
medallions/
├── 📓 notebooks/
│   ├── 01_medallion_transfers.ipynb          # Medallion pricing & transaction analysis
│   ├── 02_monthly_visualizations.ipynb       # Comprehensive market visualizations
│   ├── 03_rides_per_class.ipynb             # License class comparison
│   ├── 04_percent_of_total.ipynb            # Market share analysis
│   ├── 05_time_series_modeling.ipynb        # Predictive modeling
│   └── 06_time_series_notes.ipynb           # Modeling documentation
│
├── 📊 data/
│   └── README.md                             # Data sources and descriptions
│
├── 🛠️ generate_visualizations.py            # Script to export key plots
├── 📋 requirements.txt                       # Python dependencies
├── 📄 LICENSE                                # MIT License
├── 🤝 CONTRIBUTING.md                        # Contribution guidelines
└── 📖 README.md                              # This file
```

## 📓 Notebooks Guide

Each notebook is designed to be run sequentially and explores a specific aspect of the analysis:

| Notebook | Focus Area | Key Outputs | Time to Run |
|----------|-----------|-------------|-------------|
| **01_medallion_transfers** | Transaction analysis | Price trends, foreclosure rates | ~3 min |
| **02_monthly_visualizations** | Visual exploration | Multi-class comparisons, correlations | ~5 min |
| **03_rides_per_class** | License class breakdown | Individual class statistics | ~2 min |
| **04_percent_of_total** | Market share analysis | Percentage trends over time | ~2 min |
| **05_time_series_modeling** | Predictive modeling | Forecasting models, predictions | ~10 min |
| **06_time_series_notes** | Model documentation | Methodology notes, assumptions | ~1 min |

**Total Analysis Time:** ~25 minutes (with data loaded)

## 📊 Data Sources

This analysis uses publicly available data from:

- 🏛️ **NYC Taxi & Limousine Commission (TLC)**
  - Monthly operational reports by license class
  - Aggregated trip statistics (2015-2023)
  - Vehicle and driver count data

- 📄 **Medallion Transfer Records**
  - Historical transaction data (2017-2023)
  - Pricing, sale conditions, and medallion classifications
  - 70+ monthly sheets consolidated and processed

> **Note:** Data files are not included in this repository due to size constraints. See [`data/README.md`](data/README.md) for download instructions.

## 🔬 Methodology

### Data Processing Pipeline

```
Raw Data → Cleaning → Filtering → Transformation → Analysis → Visualization
```

**1. Data Cleaning**
- ✅ Standardized 70+ monthly Excel sheets into unified format
- ✅ Removed duplicate and malformed entries
- ✅ Handled missing values and data type conversions

**2. Filtering Criteria**
- 🎯 Focus on **unrestricted medallion sales** only
- ❌ Excluded: Family transfers, partnerships, estate sales
- ❌ Removed: Zero-price transactions (corporate restructuring)
- ✅ Calculated: Per-medallion pricing for multi-medallion sales

**3. Statistical Methods**
- 📈 **Regression Analysis (OLS)**: Quantified variable relationships
- 🔗 **Correlation Analysis**: Identified market dynamics (Pearson's r)
- 📉 **Time Series Analysis**: Tracked trends and seasonality
- 🔀 **Comparative Analysis**: Cross-license class performance

## 📈 Key Visualizations

The notebooks generate comprehensive visualizations including:

- 📊 **Price Trend Analysis**: Time series plots with confidence intervals
- 🥧 **Transaction Distribution**: Pie charts showing sale type breakdowns
- 📉 **Market Share Evolution**: Multi-line plots tracking competitive dynamics
- 🎯 **Correlation Matrices**: Scatter plots with regression lines
- 📦 **Box Plots**: Price volatility and statistical distributions
- 🗺️ **Heatmaps**: Temporal patterns and seasonal variations

## 🛠️ Technologies Used

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="50"/>
<br><strong>Python 3.8+</strong>
<br>Core language
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="50"/>
<br><strong>Pandas</strong>
<br>Data manipulation
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="50"/>
<br><strong>NumPy</strong>
<br>Numerical computing
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" width="50"/>
<br><strong>Jupyter</strong>
<br>Interactive analysis
</td>
</tr>
</table>

**Additional Libraries:**
- 📊 **Matplotlib & Seaborn**: Data visualization and statistical graphics
- 📈 **Statsmodels**: Statistical modeling, regression, and time series
- 🔢 **SciPy**: Scientific computing and statistical tests
- 📑 **OpenPyXL & xlrd**: Excel file processing

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/medallions.git
cd medallions

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

## 💻 Usage

### Quick Start

1. **Obtain Data**: Download required datasets following instructions in [`data/README.md`](data/README.md)
2. **Setup Environment**: Place data files in `data/` directory
3. **Run Analysis**: Open notebooks sequentially (01-06) in Jupyter
4. **Generate Visualizations** (Optional):
   ```bash
   python generate_visualizations.py
   ```

### Example Workflow

```python
# Example: Loading and exploring medallion data
import pandas as pd
xl = pd.ExcelFile('data/february_2023_medallion_price_list.xls')
df = pd.read_excel(xl, sheet_name='February 2023', header=2)
print(f"Total transactions: {len(df)}")
```

## 📊 Analysis Highlights

### Market Impact Metrics

<table>
<tr>
<td width="33%" align="center">
<h3>🏚️ 64.2%</h3>
<strong>Foreclosure Rate</strong>
<br>Indicating severe market distress
</td>
<td width="33%" align="center">
<h3>📉 -0.649</h3>
<strong>Yellow Taxi Correlation</strong>
<br>Negative correlation with market growth
</td>
<td width="33%" align="center">
<h3>📈 +0.685</h3>
<strong>High-Volume FHV Correlation</strong>
<br>Strong positive market capture
</td>
</tr>
</table>

### Transaction Distribution

| Category | Percentage | Count | Significance |
|----------|-----------|-------|--------------|
| 🏚️ **Foreclosures** | 64.2% | 1,827 | Primary indicator of market collapse |
| 💼 **Standard Sales** | 29.0% | 826 | Regular market transactions |
| 👨‍👩‍👧 **Estate Sales** | 4.1% | 116 | Inheritance-related transfers |
| 💸 **Bankruptcy** | 2.2% | 63 | Financial distress indicators |

## 🔮 Future Work

### Planned Enhancements

- [ ] **Advanced Predictive Modeling**
  - ARIMA/SARIMA models for price forecasting
  - Machine learning approaches (Random Forest, XGBoost)
  - Confidence intervals and prediction accuracy metrics

- [ ] **External Factor Integration**
  - Gas price correlation analysis
  - Regulatory change impact assessment
  - COVID-19 pandemic detailed analysis

- [ ] **Interactive Dashboards**
  - Plotly/Dash web interface
  - Real-time data updates
  - User-customizable views

- [ ] **Expanded Market Analysis**
  - Inactive medallion impact quantification
  - Driver income analysis
  - Comparative analysis with other major cities

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Quick Contribution Guide:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

## 👤 Author

**Data Science Portfolio Project**

Connect with me:
- 📧 Email: [your.email@example.com](mailto:your.email@example.com)
- 💼 LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- 🏛️ **NYC Taxi & Limousone Commission** for providing open data access
- 📊 **Python Data Science Community** for excellent open-source tools
- 🎓 **Data Science Best Practices** from Kaggle and academic research
- 💡 **Inspiration** from urban economics and transportation research

## 📚 References & Resources

- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [NYC Open Data Portal](https://opendata.cityofnewyork.us/)
- [Medallion Transfer Reports](https://www.nyc.gov/site/tlc/about/aggregated-reports.page)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ and Python | © 2025

*This project demonstrates skills in data cleaning, statistical analysis, visualization, and insight generation from real-world datasets for portfolio purposes.*

</div>
