import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem

engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
else:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False

st.title(f"Home - Lost Items ({st.session_state.current_user})")

session = SessionLocal()
lost_items = session.query(LostItem).all()

if lost_items:
    table_data = [{"Owner Name": item.owner_name,
                   "Description": item.item_desc,
                   "Last Seen Location": item.last_seen_location,
                   "Status": item.status} for item in lost_items]
    
import pandas as pd

df_table_data=pd.DataFrame(table
