# 📊 Sales Analytics ETL Pipeline

An end-to-end Data Engineering project that extracts, transforms, and loads retail sales data into a relational database and provides interactive business insights through a Streamlit dashboard.

---

## 🚀 Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) workflow using Python, Pandas, SQLite, and Streamlit.

The pipeline ingests raw retail sales data, performs data quality checks and transformations, stores the processed data in a database, and visualizes key business metrics through an interactive analytics dashboard.

---

## 🏗️ Architecture

```text
Sample Superstore Dataset
            │
            ▼
      ETL Pipeline
   (Python + Pandas)
            │
            ▼
 Data Cleaning & Validation
            │
            ▼
  Feature Engineering Layer
            │
            ▼
     SQLite Database
            │
            ▼
   Streamlit Dashboard
            │
            ▼
 Interactive Business Insights
```

---

## ✨ Features

### Data Engineering

* Data Extraction from CSV files
* Duplicate Record Detection & Removal
* Null Value Validation
* Data Quality Checks
* Feature Engineering
* Automated ETL Workflow
* SQLite Data Storage
* ETL Logging

### Analytics

* Sales Performance Analysis
* Profitability Analysis
* Category-Level Insights
* Region-Level Insights
* Segment-Level Insights
* State-Wise Sales Rankings

### Dashboard

* Interactive KPI Cards
* Dynamic Filtering
* Plotly Visualizations
* CSV Export Functionality
* Responsive Layout

---

## 📈 Dashboard Metrics

The dashboard provides:

* Total Sales
* Total Profit
* Total Orders
* Average Discount

Additional Insights:

* Category Wise Sales
* Region Wise Profit
* Top 10 States by Sales
* Segment Distribution
* Category Distribution

---

## ⚙️ ETL Transformations

The ETL process performs:

### Data Cleaning

* Duplicate Removal
* Null Value Handling
* Data Validation

### Feature Engineering

Generated Columns:

| Column              | Description                                          |
| ------------------- | ---------------------------------------------------- |
| Revenue_per_Item    | Revenue generated per unit sold                      |
| Profit_Margin       | Profit percentage per transaction                    |
| Discount_Percentage | Discount value converted to percentage               |
| Sales_Category      | Low / Medium / High / Very High sales classification |

---

## 🛠️ Tech Stack

### Programming

* Python

### Data Processing

* Pandas

### Database

* SQLite
* SQLAlchemy

### Visualization

* Streamlit
* Plotly

### Data Engineering Concepts

* ETL Pipelines
* Data Validation
* Data Cleaning
* Feature Engineering
* Data Analytics

---

## 📂 Project Structure

```text
sales-data-etl/
│
├── data/
│   └── SampleSuperstore.csv
│
├── database/
│   └── sales.db
│
├── dashboard/
│   └── app.py
│
├── etl/
│   └── etl_pipeline.py
│
├── logs/
│   └── etl.log
│
├── requirements.txt
│
└── README.md
```

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd sales-data-etl
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python etl/etl_pipeline.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Sample Workflow

```text
Raw Sales Dataset
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
SQLite Storage
        │
        ▼
Interactive Dashboard
```

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Data Engineering Fundamentals
* ETL Pipeline Development
* Database Integration
* Data Quality Management
* Analytics Dashboard Development
* SQL-Based Data Storage
* Business Intelligence Reporting

---

## 👨‍💻 Author

Pulkit Barola

Aspiring Data Engineer | Cloud & DevOps Enthusiast | AWS Practitioner
