import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import FoundItem

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

st.title("Report Found Item")

finder_name = st.text_input("Finder Name")
contact_info = st.text_input("Contact Info")
item_desc = st.text_area("Item Description")
found_location = st.text_input("Found Location")

if st.button("Submit Report"):
    session = SessionLocal()
    new_item = FoundItem(
        finder_name=finder_name,
        contact_info=contact_info,
        item_desc=item_desc,
        found_location=found_location,
    )
    session.add(new_item)
    session.commit()
    st.success(f"Found item reported successfully by {finder_name}!")
    session.close()

st.markdown("[Back to Home](../app.py)")
