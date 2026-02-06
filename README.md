# 🐍 Sales Predictor

A professional Python-based project that forecasts retail sales using historical data and machine learning.  
This project demonstrates **data cleaning, feature engineering, visualization, and predictive modeling** to support business decision-making.

---

## 🔍 Project Overview

The goal of this project is to:

- Analyze historical retail sales data  
- Build ML models to predict future sales trends  
- Identify patterns in sales behavior  
- Support data-driven business planning  

This repository serves as a **portfolio example** of practical Python-based data analysis and forecasting.

---

## ✨ Key Features

- Data cleaning and preprocessing with **Pandas**  
- Feature engineering for better predictions  
- Sales trend prediction using **Scikit-learn**  
- Visualizations with **Matplotlib**  
- Modular Python scripts for easy extension  
- Expandable model design for future improvements  

---

## 🛠 Tools & Technologies

- **Python 3.14+**  
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
│   ├── raw/                # Original datasets
│   │   └── sales_data.csv
│   └── processed/          # Cleaned/processed datasets
│       └── cleaned_sales_data.csv
│
├── graphs/                 # All generated plots
│   ├── sales_over_time.png
│   ├── sales_histogram.png
│   └── sales_cumulative.png
│
├── src/
│   ├── data_cleaning.py    # Script for cleaning and preprocessing
│   ├── sales_prediction.py # Script for building and evaluating ML model
│   └── plot_all.py         # Script for generating all plots
│
├── README.md
└── requirements.txt

---

## 📊 Sample Sales Data (Clickable)

You can click the link below to open the cleaned CSV file directly in GitHub:

[**Cleaned Sales Data (CSV)**](data/processed/cleaned_sales_data.csv)

Here is a preview of the dataset:

| Date       | Sales |
|------------|-------|
| 2025-01-01 | 100   |
| 2025-01-02 | 115   |
| 2025-01-03 | 108   |

---

## 📊 Example Output Graphs (Clickable)

After running the prediction scripts, the following graphs are saved in `graphs/`:

### 1️⃣ Sales Over Time
[View Sales Over Time](graphs/sales_over_time.png)  
![Sales Over Time](graphs/sales_over_time.png)

### 2️⃣ Sales Distribution
[View Sales Distribution](graphs/sales_histogram.png)  
![Sales Distribution](graphs/sales_histogram.png)

### 3️⃣ Cumulative Sales
[View Cumulative Sales](graphs/sales_cumulative.png)  
![Cumulative Sales](graphs/sales_cumulative.png)

---

## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/AkilSelot/Sales-Predictor.git
cd Sales-Predictor
Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
Install required packages:

pip install -r requirements.txt
Run Python scripts:

Data Cleaning: cleans raw sales data and saves it to data/processed/

python src\data_cleaning.py
Sales Prediction: trains ML model, outputs predicted sales, and saves graphs

python src\sales_prediction.py
Generate All Plots: creates multiple example plots (sales over time, histogram, cumulative)

python src\plot_all.py
💡 Notes
Replace the CSV dataset with your own sales data for testing.

The Python scripts are modular — you can easily improve the model or add new features.

Example graphs are saved in graphs/ folder as PNG files.

ML model can be replaced with other algorithms if needed.

👤 Author
Akil Selot
