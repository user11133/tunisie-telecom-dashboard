
import streamlit as st
from pathlib import Path

def display_tt_logo(width=150):
    """Display Tunisie Telecom logo from local file"""
    try:
        # Get the path to the logo
        logo_path = Path(__file__).parent / "tt_logo.png"
        
        if logo_path.exists():
            st.image(
                str(logo_path),
                width=width,
                use_container_width=False
            )
        else:
            st.markdown(f"### Tunisie Telecom")
    except Exception as e:
        st.markdown(f"### Tunisie Telecom")
def apply_custom_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            color: #0055A4;
            text-align: center;
        }
        .tt-blue {
            color: #0055A4;
        }
        .tt-orange {
            color: #FF6B35;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #0055A4;
        }
        .export-btn {
            background-color: #0055A4;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .export-btn:hover {
            background-color: #003D73;
        }
    </style>
    """, unsafe_allow_html=True)