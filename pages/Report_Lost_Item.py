import streamlit as st
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import LostItem

db_path = 'instance/recoverease.db'
engine = sa.create_engine(f'sqlite:///{db_path}')
SessionLocal = sessionmaker(bind=engine)

st.title("Report Lost Item")

owner_name = st.text_input("Owner Name")
item_desc = st.text_area("Item Description")
last_seen_location = st.text_input("Last Seen Location")
image_url = st.text_input("Image URL (optional)")

if st.button("Submit Report"):
    session=SessionLocal()
    new_item=LostItem(owner_name=owner_name,item_desc=item_desc,
                      last_seen_location=last_seen_location,image_url=image_url,status="Lost")
    session.add(new_item)
    session.commit()
    session.close()
    st.success(f"Lost item reported successfully for {owner_name}!")
