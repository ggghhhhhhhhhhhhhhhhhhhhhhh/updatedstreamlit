import streamlit as st

# Initialize session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Set page configuration
st.set_page_config(page_title="RecoverEase", layout="wide")

if st.session_state.logged_in:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False  # Reset login state
        st.session_state.current_user = None
        st.warning("You have logged out.")
        st.experimental_set_query_params(page="login")  # Redirect to login page

# Redirect based on login status
if not st.session_state.logged_in:
    st.warning("Please log in to access the application.")
    
else:
    st.title(f"Welcome to RecoverEase, {st.session_state.current_user}")
    st.markdown("""
    RecoverEase helps you report and manage lost and found items easily.

    Use the sidebar to navigate between pages.
    """)
