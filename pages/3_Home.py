import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

# Restrict access if not logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
    st.markdown("[Go to Login Page](./1_Login)")
else:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False  # Reset login state
        st.experimental_rerun()

    st.title("Home - Lost Items")

    session = SessionLocal()
    lost_items = session.query(LostItem).all()

    if lost_items:
        table_data = []
        for item in lost_items:
            table_data.append({
                "Owner Name": item.owner_name,
                "Item Description": item.item_desc,
                "Last Seen Location": item.last_seen_location,
                "Status": item.status,
                "Action": f"Mark as Found [{item.id}]" if item.status == "Lost" else "Resolved"
            })

        # Display table with headers using Streamlit's dataframe rendering.
        import pandas as pd
