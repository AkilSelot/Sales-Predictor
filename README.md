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

Sales-Predictor


│


├── data


│   ├── raw


│   │   └── sales_data.csv


│   └── processed


│       └── cleaned_sales_data.csv


│


├── graphs


│   ├── sales_over_time.png


│   ├── sales_distribution.png


│   └── cumulative_sales.png


│


├── src


│   ├── data_cleaning.py   


│   ├── sales_prediction.py


│   └── plot_sales.py       


│


├── README.md


└── requirements.txt



---

## 📊 Sample Sales Data (Click to View)

The cleaned sales data is available here. Click the link to open the CSV file in GitHub:

[🔹 Open Cleaned Sales Data](data/processed/cleaned_sales_data.csv)

---

## 📈 Example Output Graphs (Click to View)

After running the prediction scripts, the following graphs are saved in `graphs/`. Click to open each graph:

1️⃣ **Sales Over Time**  
[🔹 View Sales Over Time Graph](graphs/sales_over_time.png)

2️⃣ **Sales Distribution**  
[🔹 View Sales Distribution Graph](graphs/sales_histogram.png)

3️⃣ **Cumulative Sales**  
[🔹 View Cumulative Sales Graph](graphs/sales_cumulative.png)

> **Note:** Nothing is previewed on the README; users need to click to view each file.

---

## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/AkilSelot/Sales-Predictor.git
cd Sales-Predictor
Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
Install required packages:

pip install -r requirements.txt
Run Python scripts:

Data Cleaning: cleans raw sales data and saves it to data/processed/

python src/data_cleaning.py
Sales Prediction: trains ML model and outputs predicted sales, saving graphs to graphs/

python src/sales_prediction.py
💡 Notes
Replace the CSV dataset with your own sales data for testing.

Python scripts are modular — you can easily improve the model or add new features.

ML model can be replaced with other algorithms as needed.

Example graphs are saved in graphs/ folder as PNG files.

👤 Author
Akil Selot
Data Analyst
