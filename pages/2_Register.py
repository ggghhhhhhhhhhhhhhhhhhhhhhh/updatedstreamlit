import streamlit as st
from models import User
import os 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine 

os.makedirs('instance', exist_ok=True)
engine=create_engine('sqlite:///instance/recoverease.db',connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)

st.title("Register to RecoverEase")

username=st.text_input("Username")
email=st.text_input("Email")
password=st.text_input("Password",type="password")

if st.button("Register"):
  with SessionLocal() as s:
      existing=s.query(User).filter_by(username=username).first()
      if existing_user:
          st.error("Username already exists.")
      else:
          user_new=User(username=username,email=email,password=password)
          s.add(user_new)
          s.commit()
          s.close()
          st.success(f"Account created successfully for {username}!")
          st.session_state.logged_in=True 
          st.session_state.current_user=username 
          st.experimental_set_query_params(page="home")
