import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# File name
DB_FILE = "market_data.json"

# Initialize data
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

st.title("Market Tracker")

# 1. Simple Form
with st.form("entry", clear_on_submit=True):
    item = st.text_input("Item Name")
    category = st.selectbox("Category", ["Local", "Imported"])
    price = st.number_input("Price", min_value=0.0)
    submitted = st.form_submit_button("Save Item")

    if submitted and item:
        with open(DB_FILE, "r+") as f:
            data = json.load(f)
            data.append({
                "Date": str(datetime.now().date()),
                "Item": item,
                "Category": category,
                "Price": price
            })
            f.seek(0)
            json.dump(data, f, indent=4)
        st.success(f"Added {item}!")

# 2. Display Table
with open(DB_FILE, "r") as f:
    df = pd.DataFrame(json.load(f))

if not df.empty:
    st.table(df)
