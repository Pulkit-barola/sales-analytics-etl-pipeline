import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

db_path = os.path.join(
    BASE_DIR,
    "database",
    "sales.db"
)

engine = create_engine(
    f"sqlite:///{db_path}"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_sql(
    "SELECT * FROM sales",
    engine
)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.title("🔍 Filters")

region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

segment = st.sidebar.selectbox(
    "Segment",
    ["All"] + sorted(df["Segment"].unique().tolist())
)

if region != "All":
    df = df[df["Region"] == region]

if category != "All":
    df = df[df["Category"] == category]

if segment != "All":
    df = df[df["Segment"] == segment]

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
avg_discount = df["Discount"].mean() * 100

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 Sales Analytics Dashboard")
st.markdown("Interactive Data Engineering Analytics Dashboard")

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "💰 Total Sales",
    f"${total_sales:,.2f}"
)

c2.metric(
    "📈 Total Profit",
    f"${total_profit:,.2f}"
)

c3.metric(
    "🛒 Total Orders",
    total_orders
)

c4.metric(
    "🏷️ Avg Discount",
    f"{avg_discount:.2f}%"
)

st.divider()

# --------------------------------------------------
# DOWNLOAD BUTTON
# --------------------------------------------------

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.divider()

# --------------------------------------------------
# CHART ROW 1
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📦 Category Wise Sales")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Category Wise Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("🌎 Region Wise Profit")

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

    fig = px.bar(
        region_profit,
        x="Region",
        y="Profit",
        color="Region",
        title="Region Wise Profit"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# CHART ROW 2
# --------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    st.subheader("👥 Segment Distribution")

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        segment_sales,
        names="Segment",
        values="Sales",
        hole=0.4,
        title="Segment Wise Sales Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col4:

    st.subheader("📊 Category Distribution")

    category_dist = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_dist,
        names="Category",
        values="Sales",
        hole=0.4,
        title="Sales Distribution by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# TOP 10 STATES
# --------------------------------------------------

st.subheader("🏆 Top 10 States by Sales")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig = px.bar(
    top_states,
    x="State",
    y="Sales",
    color="Sales",
    title="Top 10 States by Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)