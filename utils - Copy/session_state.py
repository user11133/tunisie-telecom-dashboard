import streamlit as st
import pandas as pd

def initialize_session_state():
    if 'clients' not in st.session_state:
        st.session_state.clients = pd.DataFrame(columns=[
            'id', 'name', 'phone', 'email', 'address', 'service_type', 'subscription_date', 'status'
        ])

    if 'offers' not in st.session_state:
        st.session_state.offers = pd.DataFrame(columns=[
            'id', 'name', 'description', 'service_type', 'price', 'validity_period', 'status'
        ])