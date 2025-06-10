# Car Sales Prediction using Support Vector Regression (SVR)

This machine learning project predicts car sales using the Support Vector Regression (SVR) algorithm. The entire workflow is built using object-oriented programming (OOP) principles in Python for modularity and scalability.

# Table of Contents

- [Car Sales Prediction using Support Vector Regression (SVR)](#car-sales-prediction-using-support-vector-regression-svr)
- [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Description](#description)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Getting Started](#getting-started)
    - [Option 1: Run the Jupyter Notebook](#option-1-run-the-jupyter-notebook)
    - [Option 2: Run the Python Script](#option-2-run-the-python-script)
  - [How It Works](#how-it-works)
  - [Input \& Output](#input--output)
  - [Example Output](#example-output)


## Project Structure

```
oop project/
├── Car_sales_data.csv           # Cleaned dataset used for training
├── car_sales_model_svm.pkl      # Trained SVR model file (serialized using pickle)
├── project.ipynb                # Jupyter Notebook containing all development and results
├── project.py                   # Python script for the same workflow as the notebook
├── scaler.pkl                   # Pre-fitted StandardScaler object used during preprocessing
```

## Description

This project explores car sales prediction using historical data. It includes data exploration, preprocessing, model training, and evaluation. The final trained model and preprocessing scaler are saved for deployment.

## Features

* Clean and modular code using custom classes: `DataLoader`, `Preprocessor`, etc.
* Visualizations using `matplotlib` and `seaborn`
* Data scaling using `StandardScaler`
* SVR-based regression model
* Model evaluation with RMSE and R² metrics
* Saved model and scaler for future inference

## Technologies Used

* Python
* Jupyter Notebook
* pandas, numpy
* matplotlib, seaborn
* scikit-learn
* pickle

## Installation

To install all required packages, run the following commands one by one:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install scikit-learn
pip install jupyter
pip install pickle
```

## Getting Started

You can either use the notebook or the Python script:

### Option 1: Run the Jupyter Notebook

```bash
jupyter notebook project.ipynb
```

### Option 2: Run the Python Script

```bash
python project.py
```

## How It Works

1. **Data Loading:** Load CSV data using a custom function.
2. **Preprocessing:** Handle missing values, encode features, and scale numeric columns.
3. **Model Training:** Use SVR to train a regression model.
4. **Evaluation:** Evaluate performance using RMSE and R² score.
5. **Persistence:** Save the trained model and scaler using pickle.

## Input & Output

* **Input:** `Car_sales_data.csv` with relevant sales features
* **Output:**

  * Trained model: `car_sales_model_svm.pkl`
  * Scaler: `scaler.pkl`
  * Evaluation metrics printed in the console or notebook

## Example Output

After running, you’ll see:

* Head and tail of the data
* Descriptive statistics
* Evaluation scores like RMSE and R²

