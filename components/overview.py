import streamlit as st
from datetime import datetime

def render_overview():
    # CSS optimisé
    st.markdown("""
    <style>
    .welcome-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        color: white;
        text-align: center;
    }
    
    .welcome-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .quick-nav-btn {
        height: 120px;
        font-size: 0.9rem;
    }
    
    .offer-card {
        background: #f8f9fa; 
        padding: 1rem; 
        border-radius: 10px; 
        margin-bottom: 1rem; 
        border-left: 4px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header simple et rapide
    current_hour = datetime.now().hour
    greeting = "☀️ Bonjour" if current_hour < 12 else "🌤️ Bon après-midi" if current_hour < 18 else "🌙 Bonsoir"
    
    st.markdown(f'<div class="welcome-container"><div class="welcome-title">Tunisie Telecom</div><div style="font-size: 1.2rem;">{greeting} ! Plateforme de gestion</div></div>', unsafe_allow_html=True)
    
    # Navigation rapide - UN SEUL rerun à la fin
    st.subheader("🚀 Accès Rapide")
    
    col1, col2, col3 = st.columns(3)
    
    nav_clicked = False
    target_page = None
    
    with col1:
        if st.button("👥 **Clients**\n\nGestion clients", use_container_width=True, key="nav_clients"):
            target_page = "Gestion des Clients"
            nav_clicked = True
    
    with col2:
        if st.button("🎯 **Offres**\n\nGestion offres", use_container_width=True, key="nav_offers"):
            target_page = "Gestion des Offres" 
            nav_clicked = True
    
    with col3:
        if st.button("📊 **Rapports**\n\nAnalyses", use_container_width=True, key="nav_reports"):
            target_page = "Rapports"
            nav_clicked = True
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("📥 **Importer**\n\nImport données", use_container_width=True, key="nav_import"):
            target_page = "Importer des Données"
            nav_clicked = True
    
    with col5:
        if st.button("📤 **Exporter**\n\nExport données", use_container_width=True, key="nav_export"):
            target_page = "Exporter des Données"
            nav_clicked = True
    
    with col6:
        if st.button("🔄 **Actualiser**\n\nRecharger", use_container_width=True, key="nav_refresh"):
            nav_clicked = True

    # Appliquer la navigation UNE SEULE FOIS
    if nav_clicked and target_page:
        st.session_state.sidebar_navigation = target_page
        st.rerun()
    elif nav_clicked:
        st.rerun()

    # Offres populaires - version simplifiée
    st.subheader("🌟 Offres Populaires")
    
    if 'offers' in st.session_state and not st.session_state.offers.empty:
        active_offers = st.session_state.offers[st.session_state.offers['status'] == 'Active'].head(4)
        
        if not active_offers.empty:
            for _, offer in active_offers.iterrows():
                price_color = "🟢" if offer['price'] < 100 else "🟠"
                st.write(f"**{offer['name']}** {price_color}")
                st.write(f"_{offer['description']}_")
                st.write(f"**Prix:** {offer['price']} TND • **Validité:** {offer['validity_period']} jours")
                st.divider()
            
            if st.button("Voir toutes les offres →", key="view_all_offers"):
                st.session_state.sidebar_navigation = "Gestion des Offres"
                st.rerun()
        else:
            st.info("Aucune offre active")
    else:
        st.info("Chargez des données depuis la sidebar")

    # Métriques rapides
    st.subheader("📊 Aperçu")
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        clients_count = len(st.session_state.clients[st.session_state.clients['status'] == 'Active']) if not st.session_state.clients.empty else 0
        st.metric("Clients Actifs", clients_count)
    
    with col8:
        offers_count = len(st.session_state.offers[st.session_state.offers['status'] == 'Active']) if not st.session_state.offers.empty else 0
        st.metric("Offres Actives", offers_count)
    
    with col9:
        if not st.session_state.offers.empty and not st.session_state.clients.empty:
            revenue = st.session_state.offers[st.session_state.offers['status'] == 'Active']['price'].sum() * clients_count
        else:
            revenue = 0
        st.metric("Revenu Estimé", f"{revenue:,.0f} TND")