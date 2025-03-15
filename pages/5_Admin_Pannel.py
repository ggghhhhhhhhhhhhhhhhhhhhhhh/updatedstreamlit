import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem, FoundItem

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

st.title("Admin Panel")

admin_password_input = st.text_input("Enter Admin Password", type="password")

if admin_password_input == "admin":  # Replace with secure logic later.
    session = SessionLocal()

    lost_items = session.query(LostItem).all()
    found_items = session.query(FoundItem).all()

    if lost_items:
        st.subheader("Lost Items")
        for item in lost_items:
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            col1.write(item.owner_name)
            col2.write(item.item_desc)
            col3.write(item.last_seen_location)
            col4.write(item.status)
            if col5.button(f"Delete Lost [{item.id}]"):
                session.delete(item)
                session.commit()
                st.success(f"Deleted lost item ID {item.id}")

    if found_items:
        st.subheader("Found Items")
        for item in found_items:
            col1, col2, col3, col4, col5 = st.columns(5)
            col1.write(item.finder_name)
            col2.write(item.item_desc)
            col3.write(item.contact_info)
            if col4.button(f"Delete Found [{item.id}]"):
                session.delete(item)
                session.commit()
                st.success(f"Deleted found item ID {item.id}.")

session.close()
