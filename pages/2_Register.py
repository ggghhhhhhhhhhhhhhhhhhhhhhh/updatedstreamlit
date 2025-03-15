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

if st.button("Register"):
    session = SessionLocal()
    user_exists = session.query(User).filter_by(email=email).first()
    if user_exists:
        st.error("Email already exists.")
    else:
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        st.success(f"Account created successfully for {username}!")
    session.close()

st.markdown("[Already have an account? Login here](./1_Login)")
