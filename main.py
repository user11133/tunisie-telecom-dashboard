import streamlit as st
from components.sidebar import render_sidebar
from components.overview import render_overview
from components.client_management import render_client_management
from components.offer_management import render_offer_management
from components.data_import import render_data_import
from components.data_export import render_data_export
from components.reports import render_reports
from utils.session_state import initialize_session_state
from assets.style import apply_custom_css
from utils.auth import init_auth_session_state, authenticate_admin

# Set page configuration
st.set_page_config(
    page_title="Tunisie Telecom Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session states
init_auth_session_state()
initialize_session_state()

# Apply custom CSS
apply_custom_css()

# Authentication functions
def show_login_form():
    """Display login form"""
    # Add Tunisie Telecom logo above login form
    from assets.style import display_tt_logo
    display_tt_logo(width=200)
    
    with st.form("login_form"):
        st.subheader("Connexion Administrateur")
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        login_submitted = st.form_submit_button("Se connecter")
        
        if login_submitted:
            if username and password:
                success, message = authenticate_admin(username, password)
                if success:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.show_login = False
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Veuillez remplir tous les champs")
def show_logout():
    """Display logout button"""
    if st.sidebar.button("Se déconnecter"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.show_login = True
        st.rerun()

# Main application logic
if not st.session_state.authenticated:
    # Show login form
    show_login_form()
else:
    # Show the main application
    st.markdown(f'<h1 class="main-header">Tunisie Telecom Dashboard</h1>', unsafe_allow_html=True)
    st.markdown(f"**Bienvenue, {st.session_state.username}!**")
    st.markdown("""
    **Tunisie Telecom** est l'opérateur historique des télécommunications en Tunisie.
    Il propose une large gamme de services : téléphonie fixe, mobile, Internet haut débit (ADSL, VDSL, Fibre optique) et solutions pour entreprises.
    """)
    
    # Render sidebar and get selected menu option
    menu_option = render_sidebar()
    
    # Show logout button in sidebar
    show_logout()
    
    # Render the selected section
    if menu_option == "Aperçu":
        render_overview()
    elif menu_option == "Gestion des Clients":
        render_client_management()
    elif menu_option == "Gestion des Offres":
        render_offer_management()
    elif menu_option == "Importer des Données":
        render_data_import()
    elif menu_option == "Exporter des Données":
        render_data_export()
    elif menu_option == "Rapports":
        render_reports()

# Footer
st.markdown("---")
st.markdown("**Tunisie Telecom Dashboard** © 2025 | Développé pour la gestion des clients et offres")