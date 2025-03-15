import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem
import pandas as pd
import os

# Ensure instance directory exists
os.makedirs('instance', exist_ok=True)

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Restrict access if not logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
    st.markdown("[Go to Login Page](./1_Login)")
else:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False  # Reset login state
        st.session_state.current_user = None
        st.experimental_set_query_params(page="login")  # Redirect to login page
        st.stop()

    st.title(f"Home - Lost Items ({st.session_state.current_user})")

    session = SessionLocal()

    lost_items = session.query(LostItem).all()

    if lost_items:
        table_data = []
        for item in lost_items:
            table_data.append({
                "Owner Name": item.owner_name,
                "Description": item.item_desc,
                "Last Seen Location": item.last_seen_location,
                "Status": item.status,
                "Action": f"Mark as Found [{item.id}]" if item.status == "Lost" else "Resolved"
            })

        df_table_data = pd.DataFrame(table_data)
        st.subheader("Lost Items")
        st.dataframe(df_table_data)

        for item in lost_items:
            if item.status == "Lost":
                if st.button(f"Mark as Found [{item.id}]"):
                    item.status = "Found"
                    session.commit()
                    st.success(f"Item ID {item.id} marked as found!")
            else:
                st.write(f"Item ID {item.id} is already resolved.")
    else:
        st.write("No lost items reported yet.")

    session.close()  # <-- Correctly placed inside the 'else' block
