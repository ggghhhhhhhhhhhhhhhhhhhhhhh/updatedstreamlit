import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem, FoundItem

engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
else:
    admin_username = st.text_input("Admin Username", key="admin_username")
    admin_password = st.text_input("Admin Password", type="password", key="admin_password")

    if admin_username == "admin" and admin_password == "admin":
        st.success("Welcome, Admin!")
        session = SessionLocal()

        # Display Lost Items Table
        st.subheader("Lost Items Table")
        lost_items = session.query(LostItem).all()
        if lost_items:
            table_data = [{"Owner Name": item.owner_name,
                           "Description": item.item_desc,
                           "Last Seen Location": item.last_seen_location,
                           "Status": item.status} for item in lost_items]
            import pandas as pd
            df_lost_items = pd.DataFrame(table_data)
            st.dataframe(df_lost_items)

            for item in lost_items:
                if st.button(f"Delete Lost Item [{item.id}]"):
                    session.delete(item)
                    session.commit()
                    st.success(f"Deleted lost item ID {item.id}")
        else:
            st.write("No lost items reported yet.")

        # Display Found Items Table
        st.subheader("Found Items Table")
        found_items = session.query(FoundItem).all()
        if found_items:
            table_data_found = [{"Finder Name": item.finder_name,
                                 "Contact Info": item.contact_info} for item in found_items]
            df_found_items = pd.DataFrame(table_data_found)
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
        st.error("Invalid admin credentials. Please try again.")
