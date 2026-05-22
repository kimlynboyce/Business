import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = "data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = []

st.title("Supply Chain Tracker 🇹🇹")

# Add a tabs layout
tab1, tab2 = st.tabs(["Single Entry", "Bulk Entry"])

with tab1:
    with st.form("single_form"):
        item_name = st.text_input("Item Name")
        price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
        submit = st.form_submit_button("Save")
        if submit:
            data.append({"date": str(datetime.now().date()), "item": item_name, "price": price})
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
            st.success("Saved!")

with tab2:
    st.write("Paste format: Item, Price (one per line)")
    bulk_input = st.text_area("Bulk Data")
    if st.button("Process Bulk"):
        for line in bulk_input.split('\n'):
            if ',' in line:
                item, price = line.split(',')
                data.append({"date": str(datetime.now().date()), "item": item.strip(), "price": float(price)})
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        st.success("Bulk entries added!")

st.header("Your Data")
st.table(data)
