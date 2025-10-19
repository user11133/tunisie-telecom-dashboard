import pandas as pd
from io import BytesIO
import streamlit as st


# Sample data for demonstration
sample_clients = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Client A', 'Client B', 'Client C', 'Client D'],
    'phone': ['12345678', '23456789', '34567890', '45678901'],
    'email': ['a@example.com', 'b@example.com', 'c@example.com', 'd@example.com'],
    'address': ['Tunis', 'Sfax', 'Sousse', 'Nabeul'],
    'service_type': ['Fibre optique', 'Mobile', 'ADSL', 'VDSL'],
    'subscription_date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05'],
    'status': ['Active', 'Active', 'Suspended', 'Active']
})

sample_offers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Fibre 100Mb', 'Mobile Premium', 'ADSL 20Mb', 'Pack Entreprise'],
    'description': ['Fibre optique 100Mb/s', 'Forfait mobile illimité', 'ADSL 20Mb/s', 'Solution complète pour entreprises'],
    'service_type': ['Fibre optique', 'Mobile', 'ADSL', 'Mixte'],
    'price': [99.9, 29.9, 49.9, 199.9],
    'validity_period': [30, 30, 30, 365],
    'status': ['Active', 'Active', 'Inactive', 'Active']
})

def load_sample_data():
    st.session_state.clients = sample_clients
    st.session_state.offers = sample_offers

def add_client(client_data):
    new_id = max(st.session_state.clients['id'].max(), 0) + 1 if not st.session_state.clients.empty else 1
    client_data['id'] = new_id
    new_client = pd.DataFrame([client_data])
    st.session_state.clients = pd.concat([st.session_state.clients, new_client], ignore_index=True)

def update_client(client_id, updated_data):
    idx = st.session_state.clients[st.session_state.clients['id'] == client_id].index
    if len(idx) > 0:
        for key, value in updated_data.items():
            st.session_state.clients.at[idx[0], key] = value

def delete_client(client_id):
    st.session_state.clients = st.session_state.clients[st.session_state.clients['id'] != client_id]

def add_offer(offer_data):
    new_id = max(st.session_state.offers['id'].max(), 0) + 1 if not st.session_state.offers.empty else 1
    offer_data['id'] = new_id
    new_offer = pd.DataFrame([offer_data])
    st.session_state.offers = pd.concat([st.session_state.offers, new_offer], ignore_index=True)

def update_offer(offer_id, updated_data):
    idx = st.session_state.offers[st.session_state.offers['id'] == offer_id].index
    if len(idx) > 0:
        for key, value in updated_data.items():
            st.session_state.offers.at[idx[0], key] = value

def delete_offer(offer_id):
    st.session_state.offers = st.session_state.offers[st.session_state.offers['id'] != offer_id]

def export_to_excel(df, filename):
    """Export DataFrame to Excel file"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')
    processed_data = output.getvalue()
    return processed_data