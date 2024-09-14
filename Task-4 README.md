# Tour and Travel Customer Churn Prediction
## Project Overview:
The Tour & Travel Customer Churn Prediction project is aimed at helping a travel company predict customer churn using machine learning techniques. The dataset contains various indicators such as age, frequent flyer status, annual income class, services opted frequency, social media account synchronization, and hotel bookings. By predicting customer churn, the company can optimize its resources and improve retention strategies.

## Dataset Features:
- Age: Customer's age
- Frequent Flyer Status: Whether the customer is a frequent flyer
- Annual Income Class: Income classification of the customer
- Services Opted Frequency: Frequency of services used by the customer
- Social Media Synchronization: If the customer has synchronized a social media account
- Hotel Bookings: Number of hotel bookings by the customer
- Target: Binary variable indicating churn (1 = churned, 0 = not churned)
## Goals:
- Predict customer churn using the provided dataset.
- Perform exploratory data analysis (EDA) to gain insights into customer behavior and the factors influencing churn.
- Build a predictive model using machine learning algorithms, specifically a Random Forest Classifier, to help the company save resources and improve decision-making.
## Installation:
To run this project, you'll need to install the following Python libraries:
##### pip install pandas numpy matplotlib seaborn scikit-learn
## Usage:
### 1. Load the dataset:
- Place your dataset file (Customertravel.csv) in the project directory.

### 2. Basic Data Exploration:
- Get an overview of the data with .info() and .describe().
- Check for missing values and visualize key distributions such as target churn distribution and age.
  ### 3. Preprocessing:
- Handle missing values by filling numerical columns with the median and categorical columns with the mode.
- Convert categorical columns to numerical using LabelEncoder.
- Split the dataset into training and testing sets.
### 4. Modeling:
- Use a Random Forest Classifier to train the model on the processed data.
- Evaluate the model’s performance using accuracy score, classification report, and confusion matrix.
### 5.  Feature Importance:
- Visualize the most important features affecting churn prediction using a feature importance plot.
## Model Evaluation:
- Accuracy: Achieved ~85% accuracy in predicting customer churn.
- Confusion Matrix: Shows how well the model classifies churned vs. non-churned customers.
- Feature Importance: Identifies key factors influencing customer churn, helping in business decision-making.
##  Results:
## Distribution of target:
![Figure_1](https://github.com/user-attachments/assets/af79eab3-f552-4d29-ace0-305bd34c90bf)
## Age Distribution:
![Figure_2](https://github.com/user-attachments/assets/b444d418-a955-430b-801b-9a07e52c5e38)
## Correlation Heatmap:
![Figure_3](https://github.com/user-attachments/assets/5fe42053-0b0d-46e1-b2b7-a6a5c0ccc30a)
## confusion Matrix:
![Figure_4](https://github.com/user-attachments/assets/9eb72478-1f4b-4448-9301-653aa0cafacc)
## Feature Importance:
![Figure5](https://github.com/user-attachments/assets/4c8e9273-fafa-411f-be75-481633c78f9b)



