import streamlit as st
from datetime import datetime
from utils.helpers import add_client, update_client, delete_client

def render_client_management():
    st.header("Gestion des Clients")
    
    tab1, tab2, tab3 = st.tabs(["Voir Clients", "Ajouter Client", "Modifier/Supprimer Client"])
    
    with tab1:
        st.dataframe(st.session_state.clients, use_container_width=True)
    
    with tab2:
        with st.form("add_client_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Nom Complet")
                phone = st.text_input("Téléphone")
                email = st.text_input("Email")
            with col2:
                address = st.text_input("Adresse")
                service_type = st.selectbox("Type de Service", 
                                          ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise"])
                status = st.selectbox("Statut", ["Active", "Suspended", "Cancelled"])
            
            submitted = st.form_submit_button("Ajouter Client")
            if submitted:
                if name and phone:
                    client_data = {
                        'name': name,
                        'phone': phone,
                        'email': email,
                        'address': address,
                        'service_type': service_type,
                        'subscription_date': datetime.now().strftime("%Y-%m-%d"),
                        'status': status
                    }
                    add_client(client_data)
                    st.success("Client ajouté avec succès!")
                    st.rerun()
                else:
                    st.error("Le nom et le téléphone sont obligatoires!")
    
    with tab3:
        if not st.session_state.clients.empty:
            client_id = st.selectbox(
                "Sélectionnez un client", 
                st.session_state.clients['id'],
                format_func=lambda x: f"{st.session_state.clients[st.session_state.clients['id'] == x]['name'].iloc[0]} (ID: {x})"
            )
            
            client_data = st.session_state.clients[st.session_state.clients['id'] == client_id].iloc[0]
            
            with st.form("edit_client_form"):
                col1, col2 = st.columns(2)
                with col1:
                    edit_name = st.text_input("Nom Complet", value=client_data['name'])
                    edit_phone = st.text_input("Téléphone", value=client_data['phone'])
                    edit_email = st.text_input("Email", value=client_data['email'])
                with col2:
                    edit_address = st.text_input("Adresse", value=client_data['address'])
                    edit_service_type = st.selectbox("Type de Service", 
                                                   ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise"],
                                                   index=["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise"].index(client_data['service_type']) if client_data['service_type'] in ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise"] else 0)
                    edit_status = st.selectbox("Statut", 
                                             ["Active", "Suspended", "Cancelled"],
                                             index=["Active", "Suspended", "Cancelled"].index(client_data['status']))
                
                col1, col2 = st.columns(2)
                with col1:
                    update_submitted = st.form_submit_button("Mettre à jour Client")
                with col2:
                    delete_submitted = st.form_submit_button("Supprimer Client")
                
                if update_submitted:
                    updated_data = {
                        'name': edit_name,
                        'phone': edit_phone,
                        'email': edit_email,
                        'address': edit_address,
                        'service_type': edit_service_type,
                        'status': edit_status
                    }
                    update_client(client_id, updated_data)
                    st.success("Client mis à jour avec succès!")
                    st.rerun()
                
                if delete_submitted:
                    delete_client(client_id)
                    st.success("Client supprimé avec succès!")
                    st.rerun()
        else:
            st.info("Aucun client à modifier")