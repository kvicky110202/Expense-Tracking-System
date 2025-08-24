import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"

def analytics_by_month():
    response = requests.get(f"{API_URL}/monthly_expenses/")
    monthly_summary = response.json()

    # Create a DataFrame with multiple rows
    df = pd.DataFrame(monthly_summary)

    # Rename columns for clarity
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    # Sort by 'Month Number' in descending order
    df_sorted = df.sort_values(by="Month Number", ascending=False)

    # Set 'Month Number' as the index
    df_sorted.set_index("Month Number", inplace=True)

    # Display the title
    st.title("Expense Breakdown By Months")

    # Display the bar chart
    st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], width=0, height=0, use_container_width=True)

    # Format the 'Total' column to two decimal places
    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    # Display the table
    st.table(df_sorted)

