import streamlit as st
from models import FoundItem
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

os.makedirs('instance', exist_ok=True)
engine = create_engine('sqlite:///instance/recoverease.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

st.title("Report Found Item")

finder_name = st.text_input("Finder Name")
contact_info = st.text_input("Contact Info")

if st.button("Submit Report"):
    session = SessionLocal()
    new_item = FoundItem(
        finder_name=finder_name,
        contact_info=contact_info,
    )
    session.add(new_item)
    session.commit()
    session.close()
    st.success(f"Found item reported successfully by {finder_name}!")

st.markdown("[Back to Home](../app.py)")
