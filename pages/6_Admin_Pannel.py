import streamlit as st
import pandas as pd
from models import LostItem, FoundItem
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

os.makedirs('instance', exist_ok=True)
engine = create_engine('sqlite:///instance/recoverease.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
else:
    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password")

    if admin_username == "admin" and admin_password == "admin":
        st.success("Welcome, Admin!")
        session = SessionLocal()

        st.subheader("Lost Items")
        lost_items = session.query(LostItem).all()
        if lost_items:
            df_lost_items = pd.DataFrame([{
                "Owner Name": item.owner_name,
                "Description": item.item_desc,
                "Last Seen Location": item.last_seen_location,
                "Status": item.status,
            } for item in lost_items])
            st.dataframe(df_lost_items)

            for item in lost_items:
                if st.button(f"Delete Lost Item [{item.id}]"):
                    session.delete(item)
                    session.commit()
                    st.success(f"Deleted lost item ID {item.id}")
        else:
            st.write("No lost items reported yet.")

        # Found items table
        found_items = session.query(FoundItem).all()
        if found_items:
            df_found_items = pd.DataFrame([{
                "Finder Name": item.finder_name,
                "Contact Info": item.contact_info,
            } for item in found_items])
            st.dataframe(df_found_items)

            for item in found_items:
                if st.button(f"Delete Found Item [{item.id}]"):
                    session.delete(item)
                    session.commit()
                    st.success(f"Deleted found item ID {item.id}")
        else:
            st.write("No found items reported yet.")
        session.close()
    else:
        st.error("Invalid admin credentials.")
