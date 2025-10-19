import streamlit as st
from assets.style import display_tt_logo

def render_sidebar():
    # Only show sidebar if user is authenticated
    if not st.session_state.authenticated:
        return None
    
    with st.sidebar:
        # Display Tunisie Telecom logo
        display_tt_logo(width=150)
        
        st.title("Navigation")
        
        # Vérifier si une navigation a été déclenchée depuis l'overview
        if 'sidebar_navigation' in st.session_state:
            default_index = ["Aperçu", "Gestion des Clients", "Gestion des Offres", "Importer des Données", "Exporter des Données", "Rapports"].index(st.session_state.sidebar_navigation)
            # Supprimer la variable après utilisation
            del st.session_state.sidebar_navigation
        else:
            default_index = 0
        
        menu_option = st.radio(
            "Sélectionnez une section:",
            ["Aperçu", "Gestion des Clients", "Gestion des Offres", "Importer des Données", "Exporter des Données", "Rapports"],
            index=default_index
        )
        
        # Add some sample data if empty
        if st.session_state.clients.empty:
            if st.button("Charger des données exemple"):
                from utils.helpers import load_sample_data
                load_sample_data()
                st.success("Données exemple chargées!")
                st.rerun()
                
    return menu_option