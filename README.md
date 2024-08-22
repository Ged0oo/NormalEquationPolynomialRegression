# Normal Equation Linear Regression

## Overview
# This Python script implements linear regression using the Normal Equation method. 
# The script reads data from a CSV file (MarketData.csv), computes the parameters (theta values) 
# using the normal equation, and then predicts sales based on input features.

## Files
# MarketData.csv: The dataset containing the features (youtube, facebook, newspaper) 
# and the target variable (sales).
# normal_equation.py: The Python script implementing the normal equation for linear regression.

## Script Explanation
# The script loads the dataset and drops the sales column from the feature set.
# It adds a column of ones to the feature matrix to account for the intercept term.
# The normal equation is used to calculate the parameters (theta values) that minimize the cost function.
# The script then predicts sales values for different combinations of youtube, facebook, and newspaper ad spends.

## Output
# The theta values (parameters) are printed to the console.
# Predicted sales values are printed for three different input sets.
