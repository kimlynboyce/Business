import streamlit as st
import json
import os
from datetime import datetime

# File to store data
DATA_FILE = "data.json"

# Load existing data or create empty dict
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = []

st.title("Supply Chain Tracker 🇹🇹")

# Sidebar for Input
st.sidebar.header("Add New Entry")
with st.sidebar.form("entry_form"):
    item_name = st.text_input("Item Name (e.g., Peppers)")
    category = st.selectbox("Category", ["Local Produce", "Imported Good"])
    price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=0)
    submit = st.form_submit_button("Save Entry")

if submit:
    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "item": item_name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    data.append(new_entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    st.success(f"Added {item_name}!")

# Display Data
st.header("Dashboard")
if data:
    st.table(data)
else:
    st.write("No data yet. Use the sidebar to add entries.")