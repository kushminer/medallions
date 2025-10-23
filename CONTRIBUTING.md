# Contributing to NYC Medallion Market Analysis

Thank you for your interest in contributing to this project! This document provides guidelines for contributions.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the Issues section
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the issue/suggestion
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Your environment (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

1. Explain the enhancement and its benefits
2. Provide examples of how it would be used
3. Consider if it fits the project scope

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear, descriptive messages
6. Push to your fork
7. Open a Pull Request with:
   - Description of changes
   - Rationale for the changes
   - Any relevant issue numbers

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep notebook cells organized and well-documented

### Notebook Standards

- Clear markdown cells explaining each analysis section
- Remove unnecessary outputs before committing (except key visualizations)
- Ensure notebooks run sequentially from top to bottom
- Include cell execution numbers

### Adding New Analysis

If adding new analytical notebooks:

1. Follow the naming convention: `##_descriptive_name.ipynb`
2. Include a markdown cell at the top explaining the analysis goal
3. Document key findings in markdown cells
4. Update the main README.md with your findings

### Data Handling

- Never commit raw data files to the repository
- Update `data/README.md` if new data sources are added
- Document any data transformations clearly

## Testing

Before submitting:

1. Ensure all notebooks run without errors
2. Verify visualizations render correctly
3. Check that file paths work for other users
4. Test installation instructions on a clean environment

## Documentation

- Update README.md if adding features
- Document new dependencies in requirements.txt
- Add docstrings to any Python functions
- Keep data source documentation current

## Questions?

Feel free to open an issue for any questions about contributing!

## Code of Conduct

- Be respectful and constructive
- Focus on the content, not the person
- Welcome newcomers and help them learn
- Assume good intentions

Thank you for contributing to this project!
