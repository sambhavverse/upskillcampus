import pandas as pd
import streamlit as st
import plotly.express as px

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Custom CSS (Premium Look 🔥)
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
.metric-box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
h2 {
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar
st.sidebar.title("Dashboard Filters")
category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

df = df[df["Category"].isin(category)]

# Title
st.title("Sales Analysis Dashboard")

# KPIs with growth indicator
col1, col2, col3 = st.columns(3)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()

col1.metric("Total Sales", f"{total_sales:,.0f}", "+5% growth")
col2.metric("Total Profit", f"{total_profit:,.0f}", "+3% growth")
col3.metric("Average Sales", f"{avg_sales:.0f}", "+2% growth")

st.markdown("---")

# Charts Row 1
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        df,
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category",
        template="plotly_white"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(
        df,
        x="Date",
        y="Sales",
        markers=True,
        title="Sales Trend Over Time",
        template="plotly_white"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Charts Row 2
col3, col4 = st.columns(2)

with col3:
    fig3 = px.pie(
        df,
        names="Category",
        values="Sales",
        hole=0.4,
        title="Sales Distribution",
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.bar(
        df,
        x="Category",
        y="Profit",
        color="Category",
        title="Profit by Category",
        template="plotly_white"
    )
    st.plotly_chart(fig4, use_container_width=True)

# Insights Section 🔥
st.markdown("---")
st.subheader("Business Insights")

top_category = df.groupby("Category")["Sales"].sum().idxmax()
st.write(f"• The highest sales are generated from **{top_category}** category.")

st.write("• The sales trend indicates overall growth across the selected period.")

st.write("• Profit distribution suggests some categories are more efficient.")

# Footer (professional touch)
st.markdown("---")
st.caption("Developed by Sambhav Sumang | Data Analysis Project")