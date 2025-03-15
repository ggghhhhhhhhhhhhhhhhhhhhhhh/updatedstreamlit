import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '../instance/recoverease.db')
engine = sa.create_engine(f'sqlite:///{db_path}')
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
