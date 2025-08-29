import streamlit as st
from io import BytesIO
import pandas as pd
from utils.helpers import export_to_excel

def render_data_export():
    st.header("Exporter des Données vers Excel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Exporter les Clients")
        if not st.session_state.clients.empty:
            st.download_button(
                label="📥 Télécharger les Clients en Excel",
                data=export_to_excel(st.session_state.clients, "clients_tunisie_telecom"),
                file_name="clients_tunisie_telecom.xlsx",
                mime="application/vnd.ms-excel"
            )
            
            # Filter options
            st.subheader("Options de Filtrage")
            status_filter = st.multiselect(
                "Filtrer par statut",
                options=st.session_state.clients['status'].unique(),
                default=st.session_state.clients['status'].unique()
            )
            
            service_filter = st.multiselect(
                "Filtrer par type de service",
                options=st.session_state.clients['service_type'].unique(),
                default=st.session_state.clients['service_type'].unique()
            )
            
            # Apply filters
            filtered_clients = st.session_state.clients[
                (st.session_state.clients['status'].isin(status_filter)) &
                (st.session_state.clients['service_type'].isin(service_filter))
            ]
            
            st.write(f"{len(filtered_clients)} clients correspondants aux filtres")
            
            if not filtered_clients.empty:
                st.download_button(
                    label="📥 Télécharger les Clients Filtrés",
                    data=export_to_excel(filtered_clients, "clients_filtres_tunisie_telecom"),
                    file_name="clients_filtres_tunisie_telecom.xlsx",
                    mime="application/vnd.ms-excel"
                )
        else:
            st.info("Aucune donnée client à exporter")
    
    with col2:
        st.subheader("Exporter les Offres")
        if not st.session_state.offers.empty:
            st.download_button(
                label="📥 Télécharger les Offres en Excel",
                data=export_to_excel(st.session_state.offers, "offres_tunisie_telecom"),
                file_name="offres_tunisie_telecom.xlsx",
                mime="application/vnd.ms-excel"
            )
            
            # Filter options
            st.subheader("Options de Filtrage")
            status_filter_offers = st.multiselect(
                "Filtrer par statut",
                options=st.session_state.offers['status'].unique(),
                default=st.session_state.offers['status'].unique(),
                key="offer_status_filter"
            )
            
            service_filter_offers = st.multiselect(
                "Filtrer par type de service",
                options=st.session_state.offers['service_type'].unique(),
                default=st.session_state.offers['service_type'].unique(),
                key="offer_service_filter"
            )
            
            # Apply filters
            filtered_offers = st.session_state.offers[
                (st.session_state.offers['status'].isin(status_filter_offers)) &
                (st.session_state.offers['service_type'].isin(service_filter_offers))
            ]
            
            st.write(f"{len(filtered_offers)} offres correspondantes aux filtres")
            
            if not filtered_offers.empty:
                st.download_button(
                    label="📥 Télécharger les Offres Filtrées",
                    data=export_to_excel(filtered_offers, "offres_filtres_tunisie_telecom"),
                    file_name="offres_filtres_tunisie_telecom.xlsx",
                    mime="application/vnd.ms-excel"
                )
        else:
            st.info("Aucune donnée offre à exporter")
    
    # Export both clients and offers in a single file
    st.subheader("Exporter Toutes les Données")
    if not st.session_state.clients.empty or not st.session_state.offers.empty:
        # Create an Excel file with multiple sheets
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            if not st.session_state.clients.empty:
                st.session_state.clients.to_excel(writer, index=False, sheet_name='Clients')
            if not st.session_state.offers.empty:
                st.session_state.offers.to_excel(writer, index=False, sheet_name='Offres')
        
        st.download_button(
            label="📥 Télécharger Toutes les Données",
            data=output.getvalue(),
            file_name="toutes_donnees_tunisie_telecom.xlsx",
            mime="application/vnd.ms-excel"
        )
    else:
        st.info("Aucune donnée à exporter")