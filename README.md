# 📊 Sales Analytics ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.12-blue)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)]()
[![SQLite](https://img.shields.io/badge/SQLite-Database-green)]()
[![ETL](https://img.shields.io/badge/Data%20Engineering-ETL-orange)]()

## 🚀 Live Demo

🌐 Live Application: https://sales-analytics-etl-pipeline-1.onrender.com/

---

# 📌 Project Overview

Sales Analytics ETL Pipeline is an end-to-end Data Engineering project that extracts raw retail sales data, performs data cleaning and transformation, stores processed data in SQLite, and visualizes business insights through an interactive Streamlit dashboard.

The project demonstrates real-world ETL concepts, data quality checks, database integration, and analytics reporting.

---

# 🏗️ Architecture

```text
Sample Superstore Dataset
           │
           ▼
      Extract Data
           │
           ▼
    Data Validation
           │
           ▼
   Data Cleaning &
   Transformation
           │
           ▼
     SQLite Database
           │
           ▼
 Streamlit Dashboard
           │
           ▼
 Business Insights
```

---

# ✨ Key Features

### ETL Pipeline

- Extract data from CSV dataset
- Perform data quality checks
- Remove duplicate records
- Handle missing values
- Feature engineering
- Load transformed data into SQLite database
- ETL execution logging

### Analytics Dashboard

- Interactive KPI cards
- Sales Analysis
- Profit Analysis
- Region Wise Performance
- Category Wise Sales
- Segment Distribution
- Top States Analysis
- Dynamic Filters
- CSV Export Functionality

---

# 📈 Dashboard Metrics

The dashboard provides:

- Total Sales
- Total Profit
- Total Orders
- Average Discount

Business Insights:

- Category Wise Sales
- Region Wise Profit
- Segment Distribution
- Sales Distribution by Category
- Top 10 States by Sales

---

# ⚙️ ETL Transformations

### Data Cleaning

- Duplicate Detection
- Duplicate Removal
- Null Value Validation
- Data Quality Checks

### Feature Engineering

Generated Columns:

| Column | Description |
|----------|-------------|
| Revenue_per_Item | Revenue generated per product |
| Profit_Margin | Profit percentage per transaction |
| Discount_Percentage | Discount converted into percentage |
| Sales_Category | Sales classification (Low, Medium, High, Very High) |

---

# 🛠️ Tech Stack

### Programming

- Python

### Data Processing

- Pandas

### Database

- SQLite
- SQLAlchemy

### Dashboard

- Streamlit
- Plotly

### Concepts

- ETL Pipeline
- Data Cleaning
- Data Validation
- Data Transformation
- Feature Engineering
- Business Analytics

---

# 📂 Project Structure

```text
sales-analytics-etl-pipeline
│
├── dashboard
│   └── app.py
│
├── data
│   └── SampleSuperstore.csv
│
├── database
│   └── sales.db
│
├── etl
│   └── etl_pipeline.py
│
├── logs
│   └── etl.log
│
├── requirements.txt
│
└── README.md
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Pulkit-barola/sales-analytics-etl-pipeline.git
```

Move into project directory:

```bash
cd sales-analytics-etl-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ETL Pipeline:

```bash
python etl/etl_pipeline.py
```

Launch Dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 📊 Business Insights Generated

The dashboard helps answer:

- Which product category generates the highest revenue?
- Which region contributes the most profit?
- Which states drive maximum sales?
- Which customer segment contributes most to revenue?
- How do discounts impact profitability?

---

# 🎯 Skills Demonstrated

- Data Engineering Fundamentals
- ETL Pipeline Development
- Data Cleaning & Validation
- SQL & Database Management
- Analytics Dashboard Development
- Business Intelligence Reporting
- Python Data Processing

---

# 📷 Project Screenshots

Add dashboard screenshots here:

### Dashboard Overview

![Dashboard Screenshot](images/dashboard.png)

### Sales Analytics

![Analytics Screenshot](images/analytics.png)

---

# 👨‍💻 Author

**Pulkit Barola**

Aspiring Data Engineer | Cloud & Data Enthusiast

GitHub: https://github.com/Pulkit-barola

---

# ⭐ Future Enhancements

- AWS S3 Integration
- Automated ETL Scheduling
- PostgreSQL Migration
- Real-Time Data Pipeline
- Data Warehouse Integration
