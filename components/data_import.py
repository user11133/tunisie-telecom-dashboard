import streamlit as st
import pandas as pd
from datetime import datetime

def render_data_import():
    st.header("Importer des Données depuis Excel")
    
    tab1, tab2 = st.tabs(["Importer Clients", "Importer Offres"])
    
    with tab1:
        st.subheader("Importer des Clients")
        uploaded_file = st.file_uploader("Choisir un fichier Excel pour les clients", type=['xlsx'], key="client_upload")
        
        if uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
                st.write("Aperçu des données:", df.head())
                
                # Check required columns
                required_cols = ['name', 'phone']
                if all(col in df.columns for col in required_cols):
                    # Generate missing columns if needed
                    for col in ['email', 'address', 'service_type', 'status']:
                        if col not in df.columns:
                            df[col] = ""
                    
                    if 'subscription_date' not in df.columns:
                        df['subscription_date'] = datetime.now().strftime("%Y-%m-%d")
                    
                    # Generate IDs
                    if 'id' not in df.columns:
                        max_id = st.session_state.clients['id'].max() if not st.session_state.clients.empty else 0
                        df['id'] = range(max_id + 1, max_id + 1 + len(df))
                    
                    if st.button("Importer les Clients"):
                        st.session_state.clients = pd.concat([st.session_state.clients, df], ignore_index=True)
                        st.success(f"{len(df)} clients importés avec succès!")
                        st.rerun()
                else:
                    st.error(f"Le fichier doit contenir au moins les colonnes: {required_cols}")
            
            except Exception as e:
                st.error(f"Erreur lors de la lecture du fichier: {e}")
    
    with tab2:
        st.subheader("Importer des Offres")
        uploaded_file = st.file_uploader("Choisir un fichier Excel pour les offres", type=['xlsx'], key="offer_upload")
        
        if uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
                st.write("Aperçu des données:", df.head())
                
                # Check required columns
                required_cols = ['name', 'price']
                if all(col in df.columns for col in required_cols):
                    # Generate missing columns if needed
                    for col in ['description', 'service_type', 'validity_period', 'status']:
                        if col not in df.columns:
                            if col == 'validity_period':
                                df[col] = 30
                            elif col == 'status':
                                df[col] = "Active"
                            else:
                                df[col] = ""
                    
                    # Generate IDs
                    if 'id' not in df.columns:
                        max_id = st.session_state.offers['id'].max() if not st.session_state.offers.empty else 0
                        df['id'] = range(max_id + 1, max_id + 1 + len(df))
                    
                    if st.button("Importer les Offres"):
                        st.session_state.offers = pd.concat([st.session_state.offers, df], ignore_index=True)
                        st.success(f"{len(df)} offres importées avec succès!")
                        st.rerun()
                else:
                    st.error(f"Le fichier doit contenir au moins les colonnes: {required_cols}")
            
            except Exception as e:
                st.error(f"Erreur lors de la lecture du fichier: {e}")