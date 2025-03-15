import streamlit as st
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import FoundItem

db_path = 'instance/recoverease.db'
engine = sa.create_engine(f'sqlite:///{db_path}')
SessionLocal = sessionmaker(bind=engine)

st.title("Report Found Item")

finder_name = st.text_input("Finder Name")
contact_info = st.text_input("Contact Info")
item_desc = st.text_area("Item Description")
found_location = st.text_input("Found Location")

if st.button("Submit Report"):
    new_item = FoundItem(
        finder_name=finder_name,
        contact_info=contact_info,
        item_desc=item_desc,
        found_location=found_location,
    )
    session = SessionLocal()
    session.add(new_item)
    session.commit()
    session.close()
    st.success(f"Found item reported successfully by {finder_name}!")
