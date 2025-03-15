
import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

st.title("Login to RecoverEase")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    session = SessionLocal()
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password.")
    session.close()

st.markdown("[Don't have an account? Register here](./2_Register)")
