import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

st.title("Register for RecoverEase")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password != confirm_password:
        st.error("Passwords do not match!")
    else:
        session = SessionLocal()
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            st.error("Username already exists. Please choose a different username.")
        else:
            new_user = User(username=username, email=email, password=password)
            session.add(new_user)
            session.commit()
            st.success(f"Account created successfully for {username}!")
            st.session_state.logged_in = True  # Automatically log in after registration
            st.session_state.current_user = username
            st.experimental_set_query_params(page="home")  # Redirect to home page
        session.close()

st.markdown("[Already have an account? Login here](./1_Login)")
