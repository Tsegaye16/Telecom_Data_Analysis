# Enhancing Telecom Business Insights through Comprehensive Data Analysis and Machine Learning Techniques for Optimal Investment Decisions

## Executive Summary

In the highly competitive telecom sector, understanding customer behavior and engagement is crucial for making informed investment decisions. This project involves a comprehensive analysis of telecom data for TellCo, a mobile service provider in the Republic of Pefkakia. Leveraging advanced data analysis and machine learning techniques, the project aims to identify opportunities for growth, optimize service offerings, and support strategic investment decisions.

## Project Overview

The objective of this project is to analyze the data provided by TellCo to identify opportunities for growth and to assess whether TellCo is a worthy investment. The analysis is divided into four primary tasks:

1. **User Overview Analysis**: Understanding customer behavior and usage patterns.
2. **User Engagement Analysis**: Evaluating user engagement metrics and clustering users based on engagement.
3. **Experience Analysis**: Analyzing user experience metrics, including network performance and device characteristics.
4. **Satisfaction Analysis**: Combining engagement and experience metrics to compute satisfaction scores and predict customer satisfaction.

## Dataset Description

- **Data Source**: xDR records from TellCo.
- **Attributes**: Includes user activity data on various applications (e.g., Social Media, Google, Email, YouTube, Netflix, Gaming) and network performance metrics (e.g., TCP retransmission, RTT, Throughput).
- **Schema**: Detailed description of attributes and SQL schema.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Tsegaye16/Telecom_Data_Analysis
   cd Telecom_Data_Analysis
   ```

``

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - Import the provided SQL schema into your PostgreSQL database.
   - Configure the connection settings in your project configuration files.

## Tasks and Methodologies

### Task 1 - User Overview Analysis

- **Business Overview**: Understanding user behavior is crucial for any business aiming to enhance its offerings and tailor solutions to customer needs. This analysis provides insights into customer device preferences and usage patterns, which can drive targeted marketing strategies and product improvements.

- **Objective**: Conduct a comprehensive User Overview Analysis to identify the most popular handsets, manufacturers, and their usage patterns.
- **Sub-tasks**:

  - Identify Top 10 Handsets: Determine the top 10 handsets used by customers.
  - Identify Top 3 Manufacturers: Identify the top 3 handset manufacturers.
  - Analyze Top Handsets by Manufacturer: For each of the top 3 manufacturers, identify the top 5 handsets.
  - Interpretation and Recommendations: Provide insights and recommendations based on the analysis to inform marketing strategies.

- **Additional Analysis**:
  - Aggregate user data on xDR (data sessions) including:
    - Number of sessions
    - Session duration
    - Total download (DL) and upload (UL) data
    - Data volume per application
  - Perform Exploratory Data Analysis (EDA) to uncover insights and handle missing values and outliers.
    - Describe variables and data types
    - Segment users into deciles based on total session duration and compute total data per decile
    - Conduct univariate and bivariate analyses
    - Perform correlation analysis
    - Execute Principal Component Analysis (PCA) for dimensionality reduction and interpret results

## Contact

For any questions or further information, please contact [Tsegaye Abewa](mailto:abewatsegaye16@gmail.com).
