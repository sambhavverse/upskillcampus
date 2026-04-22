import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.title("🚀 Live Sales Dashboard")

# Load data
df = pd.read_csv("sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar filter
st.sidebar.header("Filter")
category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

df = df[df["Category"].isin(category)]

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", df["Sales"].sum())
col2.metric("Total Profit", df["Profit"].sum())
col3.metric("Average Sales", round(df["Sales"].mean(), 2))

# Bar Chart
st.subheader("Sales by Category")
fig1 = px.bar(df, x="Category", y="Sales", color="Category")
st.plotly_chart(fig1)

# Line Chart
st.subheader("Sales Trend")
fig2 = px.line(df, x="Date", y="Sales", markers=True)
st.plotly_chart(fig2)

# Pie Chart
st.subheader("Sales Distribution")
fig3 = px.pie(df, names="Category", values="Sales")
st.plotly_chart(fig3)

# Data Table
st.subheader("Data Table")
st.dataframe(df)