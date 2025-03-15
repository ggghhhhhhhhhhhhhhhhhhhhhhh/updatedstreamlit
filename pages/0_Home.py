import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

st.title("Home - Lost Items")

session = SessionLocal()
lost_items = session.query(LostItem).all()

if lost_items:
    st.subheader("Lost Items")
    for item in lost_items:
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.write(item.owner_name)
        col2.write(item.item_desc)
        col3.write(item.last_seen_location)
        col4.write(item.status)
        if item.status == "Lost":
            if col5.button(f"Mark as Found [{item.id}]"):
                item.status = "Found"
                session.commit()
                st.success(f"Item ID {item.id} marked as found!")
        else:
            col5.write("Resolved")
else:
    st.write("No lost items reported yet.")

session.close()
