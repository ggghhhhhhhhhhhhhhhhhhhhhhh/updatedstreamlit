import streamlit as st 
from models import User 
import os 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine 

os.makedirs('instance',exist_ok=True)
engine=create_engine('sqlite:///instance/recoverease.db',connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)

st.title("Login to RecoverEase")

username=st.text_input("Username")
password=st.text_input("Password",type="password")

if st.button("Login"):
  s=SessionLocal()
  user=s.query(User).filter_by(username=username,password=password).first()
  if user:
      s.close()
      st.session_state.logged_in=True 
      st.session_state.current_user=username 
      st.experimental_set_query_params(page="home")
      st.stop()  
  else:
      s.close()
      st.error("Invalid username or password.")

