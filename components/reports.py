import streamlit as st
from utils.helpers import export_to_excel

def render_reports():
    st.header("Rapports et Analyses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Répartition des Clients par Statut")
        status_counts = st.session_state.clients['status'].value_counts()
        st.plotly_chart({
            'data': [{
                'values': status_counts.values,
                'labels': status_counts.index,
                'type': 'pie',
                'hole': 0.4,
                'marker': {'colors': ['#0055A4', '#FF6B35', '#8ECAE6']}
            }],
            'layout': {
                'title': 'Clients par Statut'
            }
        }, use_container_width=True)
    
    with col2:
        st.subheader("Répartition des Offres par Type de Service")
        service_offers = st.session_state.offers['service_type'].value_counts()
        st.plotly_chart({
            'data': [{
                'x': service_offers.index,
                'y': service_offers.values,
                'type': 'bar',
                'marker': {'color': '#0055A4'}
            }],
            'layout': {
                'title': 'Offres par Type de Service'
            }
        }, use_container_width=True)
    
    st.subheader("Prix des Offres Actives")
    active_offers = st.session_state.offers[st.session_state.offers['status'] == 'Active']
    if not active_offers.empty:
        st.plotly_chart({
            'data': [{
                'x': active_offers['name'],
                'y': active_offers['price'],
                'type': 'bar',
                'marker': {'color': '#FF6B35'}
            }],
            'layout': {
                'title': 'Prix des Offres Actives (TND)'
            }
        }, use_container_width=True)
        
        # Export active offers
        st.download_button(
            label="📥 Exporter les Offres Actives",
            data=export_to_excel(active_offers, "offres_actives_tunisie_telecom"),
            file_name="offres_actives_tunisie_telecom.xlsx",
            mime="application/vnd.ms-excel"
        )
    else:
        st.info("Aucune offre active à afficher")