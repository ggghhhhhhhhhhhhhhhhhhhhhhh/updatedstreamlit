import streamlit as st

# Initialize session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Set page configuration
st.set_page_config(page_title="RecoverEase", layout="wide")

if not st.session_state.logged_in:
    # Redirect to login page if not logged in
    st.warning("Please log in to access the application.")
    st.markdown("[Go to Login Page](./1_Login)")
else:
    # Display home page for logged-in users
    if st.sidebar.button("Logout"):
        # Reset login state and redirect to login page upon logout
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.warning("You have logged out.")
        st.experimental_set_query_params(page="login")
    
    # Home page content for logged-in users
    else:
        st.title(f"Welcome to RecoverEase, {st.session_state.current_user}")
        st.markdown("""
            RecoverEase helps you report and manage lost and found items easily.
            Use the sidebar to navigate between pages.
        """)
