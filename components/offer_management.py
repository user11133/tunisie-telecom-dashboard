import streamlit as st
from utils.helpers import add_offer, update_offer, delete_offer

def render_offer_management():
    st.header("Gestion des Offres")
    
    tab1, tab2, tab3 = st.tabs(["Voir Offres", "Ajouter Offre", "Modifier/Supprimer Offre"])
    
    with tab1:
        st.dataframe(st.session_state.offers, use_container_width=True)
    
    with tab2:
        with st.form("add_offer_form"):
            col1, col2 = st.columns(2)
            with col1:
                offer_name = st.text_input("Nom de l'offre")
                description = st.text_area("Description")
                service_type = st.selectbox("Type de Service", 
                                          ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise", "Mixte"])
            with col2:
                price = st.number_input("Prix (TND)", min_value=0.0, format="%.2f")
                validity = st.number_input("Période de validité (jours)", min_value=1, value=30)
                status = st.selectbox("Statut", ["Active", "Inactive"])
            
            submitted = st.form_submit_button("Ajouter Offre")
            if submitted:
                if offer_name and price:
                    offer_data = {
                        'name': offer_name,
                        'description': description,
                        'service_type': service_type,
                        'price': price,
                        'validity_period': validity,
                        'status': status
                    }
                    add_offer(offer_data)
                    st.success("Offre ajoutée avec succès!")
                    st.rerun()
                else:
                    st.error("Le nom et le prix sont obligatoires!")
    
    with tab3:
        if not st.session_state.offers.empty:
            offer_id = st.selectbox(
                "Sélectionnez une offre", 
                st.session_state.offers['id'],
                format_func=lambda x: f"{st.session_state.offers[st.session_state.offers['id'] == x]['name'].iloc[0]} (ID: {x})"
            )
            
            offer_data = st.session_state.offers[st.session_state.offers['id'] == offer_id].iloc[0]
            
            with st.form("edit_offer_form"):
                col1, col2 = st.columns(2)
                with col1:
                    edit_name = st.text_input("Nom de l'offre", value=offer_data['name'])
                    edit_description = st.text_area("Description", value=offer_data['description'])
                    edit_service_type = st.selectbox("Type de Service", 
                                                   ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise", "Mixte"],
                                                   index=["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise", "Mixte"].index(offer_data['service_type']) if offer_data['service_type'] in ["Fibre optique", "ADSL", "VDSL", "Mobile", "Entreprise", "Mixte"] else 0)
                with col2:
                    edit_price = st.number_input("Prix (TND)", min_value=0.0, value=float(offer_data['price']), format="%.2f")
                    edit_validity = st.number_input("Période de validité (jours)", min_value=1, value=int(offer_data['validity_period']))
                    edit_status = st.selectbox("Statut", 
                                             ["Active", "Inactive"],
                                             index=["Active", "Inactive"].index(offer_data['status']))
                
                col1, col2 = st.columns(2)
                with col1:
                    update_submitted = st.form_submit_button("Mettre à jour Offre")
                with col2:
                    delete_submitted = st.form_submit_button("Supprimer Offre")
                
                if update_submitted:
                    updated_data = {
                        'name': edit_name,
                        'description': edit_description,
                        'service_type': edit_service_type,
                        'price': edit_price,
                        'validity_period': edit_validity,
                        'status': edit_status
                    }
                    update_offer(offer_id, updated_data)
                    st.success("Offre mise à jour avec succès!")
                    st.rerun()
                
                if delete_submitted:
                    delete_offer(offer_id)
                    st.success("Offre supprimée avec succès!")
                    st.rerun()
        else:
            st.info("Aucune offre à modifier")