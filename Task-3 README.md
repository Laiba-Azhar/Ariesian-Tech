# Cereal Data Analysis:

This project performs a detailed analysis of a dataset containing information on various cereals, including their nutritional values and ratings. If you're a cereal lover, you might want to avoid looking at this data— it may just change your perception of some of your favorite cereals!

## Dataset Overview:

The dataset contains the following attributes for each cereal:

- **Name**: The name of the cereal.
- **Manufacturer**: The cereal's manufacturer, represented by a single letter.
- **Type**: The type of cereal (C = cold, H = hot).
- **Calories**: The number of calories per serving.
- **Protein**: The amount of protein in grams.
- **Fat**: The amount of fat in grams.
- **Sodium**: Sodium content in milligrams.
- **Fiber**: Fiber content in grams.
- **Carbohydrates**: Carbohydrate content in grams.
- **Sugars**: Sugar content in grams.
- **Potassium**: Potassium content in milligrams.
- **Vitamins**: Percentage of daily vitamins provided by the cereal.
- **Shelf**: The shelf location in the grocery store (1, 2, or 3).
- **Weight**: The weight of one serving in ounces.
- **Cups**: Number of cups per serving.
- **Rating**: Consumer rating of the cereal.

## Project Objectives:

The main objectives of this project are to:

1. **Perform Descriptive Analysis**: Summarize basic statistics for key nutritional data points like calories, protein, fat, sugars, etc.
2. **Identify Correlations**: Explore relationships between nutritional values, such as the correlation between sugar content and consumer rating.
3. **Visualize Data**: Use data visualization to represent trends, distributions, and comparisons (e.g., top-rated cereals, calories vs sugar).
4. **Find the Healthiest Cereals**: Identify cereals with the best balance of nutrients (e.g., low sugar, high fiber, low calories).
5. **Analyze Manufacturer Trends**: Examine which manufacturers dominate the cereal market and their average product ratings.

## Installation:

To run the analysis, you'll need to install the following Python libraries:
pip install pandas matplotlib seaborn
## Usage:
After installing the necessary dependencies, you can run the analysis as follows:
##### Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

###### Load the dataset
df = pd.read_csv('cereal.csv')

##### Perform data analysis (e.g., descriptive statistics)
print(df.describe())
## Analysis:
#### 1. Descriptive Statistics
- Summary of key nutritional values: calories, sugars, fiber, and protein.
#### 2. Correlations
- Calories vs Sugars: Exploring their relationship.
- Fiber vs Rating: Does more fiber result in higher ratings?
#### 3. Top-Rated & Healthiest Cereals
- Identifying cereals with the best ratings.
- Highlighting low-sugar, high-fiber, and low-calorie options.
#### 4. Manufacturer Insights
- Which manufacturers have the best ratings and healthiest products?
## Outputs:
## Sugar,Sodium and Calorie Distribution Graph:
![Figure_1](https://github.com/user-attachments/assets/d05e3ff3-93d2-47f4-8c00-da44088db93b)
## Correlational Matrix of Nutritional Factors:
![Figure_2](https://github.com/user-attachments/assets/9915deb0-940f-4487-b8e3-8c6e3bd676d1)
## Sugar Content Vs Consumer Rating:
![Figure_3](https://github.com/user-attachments/assets/cb74162e-0b4b-4f0b-bfb7-f34e1f44bbdb)
## Average Sugar Content by Manufacturer:
![Figure_4](https://github.com/user-attachments/assets/f0c486c0-1f81-48e4-9fc2-eb171f8b1fd2)






