import streamlit as st
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, LostItem, FoundItem

# Database setup with error handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
instance_dir = os.path.join(BASE_DIR, 'instance')
os.makedirs(instance_dir, exist_ok=True)  # Ensure 'instance' directory exists

db_path = os.path.join(instance_dir, 'recoverease.db')

# Verify that the database file exists or create it if necessary
if not os.path.isfile(db_path):
    open(db_path, 'w').close()  # Create an empty database file

engine = create_engine(f'sqlite:///{db_path}', connect_args={"timeout": 30})
SessionLocal = sessionmaker(bind=engine)

# Initialize database tables if not already created
from models import Base
Base.metadata.create_all(engine)

# Streamlit app starts here
st.title("RecoverEase - Lost & Found Items")

menu_options = ["Home", "Login", "Register", "Report Lost Item", "Report Found Item", "Admin Panel"]
choice = st.sidebar.selectbox("Menu", menu_options)

session = SessionLocal()

if choice == "Home":
    st.header("Lost Items")
    lost_items = session.query(LostItem).all()
    if lost_items:
        for item in lost_items:
            st.subheader(item.owner_name)
            st.write(f"Description: {item.item_desc}")
            st.write(f"Last Seen Location: {item.last_seen_location}")
            st.write(f"Status: {item.status}")
            if item.status == "Lost":
                if st.button(f"Mark as Found [{item.id}]"):
                    item.status = "Found"
                    session.commit()
                    st.success(f"Item marked as found!")
            else:
                st.write("Resolved")
            if item.image_url:
                st.image(item.image_url)
            st.markdown("---")
    else:
        st.write("No lost items reported yet.")

elif choice == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:  # Replace with secure hash comparison logic
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password.")

elif choice == "Register":
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        user_exists = session.query(User).filter_by(email=email).first()
        if user_exists:
            st.error("Email already exists.")
        else:
            new_user = User(username=username, email=email, password=password)  # Replace with hashed password logic
            session.add(new_user)
            session.commit()
            st.success(f"Account created successfully for {username}!")

elif choice == "Report Lost Item":
    owner_name = st.text_input("Owner Name")
    item_desc = st.text_area("Item Description")
    last_seen_location = st.text_input("Last Seen Location")
    image_url = st.text_input("Image URL (optional)")

    if st.button("Submit Report"):
        new_item = LostItem(
            owner_name=owner_name,
            item_desc=item_desc,
            last_seen_location=last_seen_location,
            image_url=image_url,
            status="Lost"
        )
        session.add(new_item)
        session.commit()
        st.success(f"Lost item reported successfully for {owner_name}!")

elif choice == "Report Found Item":
    finder_name = st.text_input("Finder Name")
    contact_info = st.text_input("Contact Info")
    item_desc = st.text_area("Item Description")
    found_location = st.text_input("Found Location")

    if st.button("Submit Report"):
        new_item = FoundItem(
            finder_name=finder_name,
            contact_info=contact_info,
            item_desc=item_desc,
            found_location=found_location,
        )
        session.add(new_item)
        session.commit()
        st.success(f"Found item reported successfully by {finder_name}!")

elif choice == "Admin Panel":
    admin_password = "admin"  # Replace with secure authentication logic
    password_input = st.text_input("Enter Admin Password", type="password")
    if password_input == admin_password:
        lost_items = session.query(LostItem).all()
        found_items = session.query(FoundItem).all()

        if lost_items:
            st.subheader("Lost Items")
            for item in lost_items:
                delete_btn_id = f"Delete Lost [{item.id}]"
                if st.button(delete_btn_id):
                    session.delete(item)
                    session.commit()
                    st.success(f"Deleted lost item ID {item.id}.")
                else:
                    pass

session.close()
