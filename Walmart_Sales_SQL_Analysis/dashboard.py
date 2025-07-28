import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Walmart Sales Dashboard", layout="wide")

st.title(" Walmart Sales Data Dashboard")

# Load CSVs for file
sales_by_store = pd.read_csv("output_total_sales_by_store.csv")
monthly_sales = pd.read_csv("output_monthly_sales.csv")

# ---- Sidebar ----
st.sidebar.header("📂 Filters")

top_n = st.sidebar.slider("Select Top N Stores", min_value=5, max_value=20, value=10)

# ---- Section 1: Top Stores ----
st.subheader(f"🏬 Top {top_n} Stores by Total Sales")
top_stores = sales_by_store.head(top_n)

fig1, ax1 = plt.subplots()
ax1.bar(top_stores["Store"].astype(str), top_stores["Total_Sales"], color='skyblue')
ax1.set_xlabel("Store")
ax1.set_ylabel("Total Sales")
ax1.set_title(f"Top {top_n} Stores")
st.pyplot(fig1)

# ---- Section 2: Monthly Sales Trend ----
st.subheader(" Monthly Sales Trend")

fig2, ax2 = plt.subplots()
ax2.plot(monthly_sales["Month"], monthly_sales["Monthly_Sales"], marker='o', color='orange')
ax2.set_xlabel("Month")
ax2.set_ylabel("Monthly Sales")
ax2.set_title("Sales Trend Over Time")
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---- Download Options ----
st.subheader("⬇️ Download Processed Data")

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label="📥 Download Top Stores CSV",
        data=sales_by_store.to_csv(index=False),
        file_name='top_stores.csv',
        mime='text/csv'
    )

with col2:
    st.download_button(
        label="📥 Download Monthly Sales CSV",
        data=monthly_sales.to_csv(index=False),
        file_name='monthly_sales.csv',
        mime='text/csv'
    )

st.success("✅ Dashboard loaded successfully!")
