import streamlit as st

def render_overview():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Clients Actifs", 
                 len(st.session_state.clients[st.session_state.clients['status'] == 'Active']))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Offres Actives", 
                 len(st.session_state.offers[st.session_state.offers['status'] == 'Active']))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        revenue = st.session_state.offers[st.session_state.offers['status'] == 'Active']['price'].sum() * 100
        st.metric("Revenu Mensuel Estimé", f"{revenue:,.0f} TND")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Service type distribution
    st.subheader("Répartition des Clients par Type de Service")
    service_counts = st.session_state.clients['service_type'].value_counts()
    st.bar_chart(service_counts)
    
    # Recent clients
    st.subheader("Clients Récents")
    st.dataframe(st.session_state.clients.head(5), use_container_width=True)