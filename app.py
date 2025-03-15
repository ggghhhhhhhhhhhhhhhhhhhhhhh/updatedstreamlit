import streamlit as st

# Initialize session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Set page configuration
st.set_page_config(page_title="RecoverEase", layout="wide")

# Display logout button if logged in
if st.session_state.logged_in:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False  # Reset login state
        st.experimental_rerun()

# Redirect based on login status
if not st.session_state.logged_in:
    st.warning("Please log in to access the application.")
    st.markdown("[Go to Login Page](./1_Login)")
else:
    st.title("Welcome to RecoverEase")
    st.markdown("""
    RecoverEase helps you report and manage lost and found items easily.

    Use the sidebar to navigate between pages.
    """)
