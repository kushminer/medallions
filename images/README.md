# Visualization Images

This directory contains exported visualizations from the analysis notebooks.

## Generating Visualizations

To generate visualization images from the notebooks, ensure you have:

1. **Data files**: Downloaded and placed in the `data/` directory (see [`data/README.md`](../data/README.md))
2. **Dependencies**: All Python packages installed (`pip install -r requirements.txt`)

Then run:

```bash
python generate_visualizations.py
```

## Expected Outputs

When the script completes successfully, this directory will contain:

| File | Description | Source |
|------|-------------|--------|
| `medallion_price_trends.png` | Time series of average medallion prices with min/max range | Notebook 01 |
| `transaction_types.png` | Pie chart showing distribution of transaction types | Notebook 01 |
| `transaction_volume_trends.png` | Monthly transaction counts and foreclosure rates | Notebook 01 |
| `market_share_evolution.png` | Multi-line plot of market share by license class | Notebook 02 |
| `correlation_analysis.png` | Scatter plots showing key correlations | Notebook 02 |

## Image Specifications

- **Format**: PNG
- **Resolution**: 300 DPI (publication quality)
- **Dimensions**: Variable (optimized for each visualization)
- **Color Scheme**: Professional color palette suitable for presentations

## Usage

These images can be:
- Embedded in presentations
- Included in reports
- Shared on social media
- Used in the README (when data is available)

## Note

Images are not committed to the repository by default (excluded in `.gitignore`). Generate them locally as needed.
