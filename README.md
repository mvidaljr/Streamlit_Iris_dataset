# Iris Dataset Visualization with Streamlit

## Project Overview

This project focuses on building an interactive web application using Streamlit to visualize and explore the Iris dataset. The application provides users with intuitive visualizations and insights into the famous Iris dataset, which is widely used for pattern recognition and classification tasks.

## Dataset

- **Source:** The Iris dataset, containing 150 samples of iris flowers, with three classes (setosa, versicolor, virginica) based on four features: sepal length, sepal width, petal length, and petal width.

## Tools & Libraries Used

- **Web Application:**
  - `Streamlit` for creating the interactive web interface.
- **Data Manipulation:**
  - `Pandas` for handling and processing the dataset.
- **Data Visualization:**
  - `Matplotlib` and `Seaborn` for generating plots and visualizations.

## Methodology

### Application Features:

- **Data Exploration:**
  - Displayed summary statistics and data tables for the Iris dataset.
  
- **Interactive Visualizations:**
  - Enabled users to select features and plot different types of charts (scatter plots, histograms, pair plots) to explore the relationships between variables.
  - Provided options to filter data by species for more detailed analysis.

### Example Usage:

```bash
streamlit run app.py
```

### Streamlit App Structure:

- **Sidebar:**
  - Options for users to select features, species, and chart types.
  
- **Main Panel:**
  - Displayed dynamic visualizations and insights based on user inputs.

## Results

The Streamlit app provides an easy-to-use platform for visualizing the Iris dataset. Users can explore the relationships between features and species interactively, making the data analysis process more engaging and informative.

## Conclusion

This project successfully demonstrates how Streamlit can be used to create a dynamic and interactive data visualization application. The Iris dataset serves as an excellent example of how to use these tools for educational and analytical purposes.

## Future Work

- Extend the application to include predictive modeling based on user-selected features.
- Add support for additional datasets to broaden the scope of the app.
- Deploy the application for public access and real-time usage.
