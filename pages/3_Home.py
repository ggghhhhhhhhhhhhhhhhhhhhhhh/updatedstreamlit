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

    session = SessionLocal()
    
lost_items=session.query(LostItems.all())
