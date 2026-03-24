import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

if "sales" not in df.columns:
	if {"units", "unit_price"}.issubset(df.columns):
		df["sales"] = df["units"] * df["unit_price"]
	else:
		st.error("CSV must contain either 'sales' or both 'units' and 'unit_price'.")
		st.stop()

st.set_page_config(layout="wide")

st.title("📊 Sales Analytics Dashboard")

# 🔹 KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", df["sales"].sum())
col2.metric("Avg Sales", round(df["sales"].mean(), 2))
col3.metric("Transactions", len(df))

# 🔹 Low Sales Alert
st.subheader("⚠️ Low Sales Alerts (<100)")
low_sales = df[df["sales"] < 100]
st.dataframe(low_sales)

# 🔹 Top Stores
if "store_id" in df.columns:
	st.subheader("🏬 Top Performing Stores")
	top_stores = df.groupby("store_id")["sales"].sum().sort_values(ascending=False)
	st.bar_chart(top_stores)
elif "region" in df.columns:
	st.subheader("🌍 Top Performing Regions")
	top_stores = df.groupby("region")["sales"].sum().sort_values(ascending=False)
	st.bar_chart(top_stores)
else:
	st.subheader("🏬 Top Performing Stores")
	st.info("No 'store_id' or 'region' column found for this section.")
	top_stores = pd.Series(dtype="float64")

# 🔹 Product Performance
st.subheader("🏆 Product Performance")
product_perf = df.groupby("product")["sales"].sum().sort_values(ascending=False)
st.bar_chart(product_perf)

# 🔹 Time Trend
st.subheader("📈 Sales Trend Over Time")
trend = df.groupby("date")["sales"].sum()
st.line_chart(trend)

# 🔹 Insight Section (IMPORTANT)
st.subheader("🧠 Key Insights")

top_product = product_perf.idxmax()
worst_store = top_stores.idxmin() if not top_stores.empty else "N/A"

st.write(f"🏆 Top Product: {top_product}")
st.write(f"⚠️ Lowest Performing Store: {worst_store}")
st.write(f"📉 Low Sales Count: {len(low_sales)}")

st.markdown("---")
st.caption("Built using Python, Pandas, and Streamlit")