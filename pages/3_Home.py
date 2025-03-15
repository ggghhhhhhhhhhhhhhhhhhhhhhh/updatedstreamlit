import streamlit as st
import pandas as pd
from models import LostItem
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

os.makedirs('instance', exist_ok=True)
engine = create_engine('sqlite:///instance/recoverease.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
else:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False

    st.title(f"Home - Lost Items ({st.session_state.current_user})")
    
    session=SessionLocal()
    
    items=session.query(LostItem).all()
    
    if items:
        df=pd.DataFrame([{
            "Owner Name":item.owner_name,
            "Description":item.item_desc,
            "Last Seen Location":item.last_seen_location,
            "Status":item.status} for item in items])
        
        st.dataframe(df_table_data)
    
session.close()
