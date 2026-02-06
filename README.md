# 🐍 Sales Predictor

A professional Python-based project that forecasts retail sales using historical data and machine learning.  

This repository showcases a Python ML workflow for sales prediction, with cleaned datasets, modular scripts, and interactive graphs.

---

## 🔍 Project Overview

The goal of this project is to analyze retail sales data to:

- Predict future sales trends  
- Identify patterns in sales behavior  
- Evaluate model performance  
- Support data-driven business planning  

This project serves as a portfolio example of Python-based **data analysis, ML modeling, and visualization**.

---

## ✨ Key Features

- Data cleaning and preprocessing with Pandas  
- Feature engineering for improved predictions  
- Sales trend prediction using Scikit-learn  
- Interactive visualizations with Matplotlib  
- Modular Python scripts for easy extension  
- Cleaned datasets and saved graphs for clickable previews  

---

## 🔴 Live Python Output

The predicted sales graph is saved in the repository and clickable on GitHub:

👉 [View Sales Graph](graphs/sales_plot.png)  

[![Open Sales Graph](graphs/sales_plot.png)](graphs/sales_plot.png)  

**Note:** The image opens a static version. For live graphs, run the Python script locally (see instructions below).

---

## 📈 Sample Sales Data

Here is a snippet of the processed dataset:

| Date       | Sales |
|------------|-------|
| 2025-01-01 | 100   |
| 2025-01-02 | 115   |
| 2025-01-03 | 108   |

---

## 📥 Download Dataset

You can view the datasets directly in GitHub or download them:

- **Processed data:** [cleaned_sales_data.csv](data/processed/cleaned_sales_data.csv)  
- **Raw data:** [sales_data.csv](data/raw/sales_data.csv)  

> **Tip:** Keep the files in `/data/processed/` and `/data/raw/` folders in your repo.

---

## 🛠 Tools & Technologies

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- CSV datasets  

---

## 📁 Repository Structure

Sales-Predictor/
│
├── data/
│ ├── raw/ # Original datasets
│ │ └── sales_data.csv
│ └── processed/ # Cleaned/processed datasets
│ └── cleaned_sales_data.csv
│
├── src/
│ ├── data_cleaning.py # Script for cleaning and preprocessing
│ └── sales_prediction.py # Script for building and evaluating ML model
│
├── graphs/
│ └── sales_plot.png # Predicted vs actual sales graph
│
├── README.md
└── requirements.txt


---

## 🚀 Getting Started

1. Open **CMD** and navigate to the project folder:

```cmd
cd C:\Users\selot\Desktop\GitHub-Portfolio\Sales-Predictor
Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
Install required packages:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
🐍 Run Python Scripts
Data Cleaning – cleans raw sales data:

python src\data_cleaning.py
Sales Prediction – trains ML model and saves graph:

python src\sales_prediction.py
Open graphs/sales_plot.png to see predicted vs actual sales.

💡 Notes
Replace the CSV dataset with your own sales data for testing

Scripts are modular — easy to extend and improve

ML model can be replaced with other regression algorithms for experimentation

👤 Author
Akil Selot
Python & Data Analytics Portfolio

