"""
AEGIS — AI Ethics & Governance Integrated System
Streamlit UI for EU AI Act Risk Classification
Author: Kem Ada | https://linkedin.com/in/kem-a-695462101
"""

import streamlit as st
from classifier import classify_ai_system, ClassificationResult

# --- Page Config ---
st.set_page_config(
    page_title="AEGIS — AI Risk Classifier",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Mono', monospace;
        background-color: #0a0a0f;
        color: #e8e8f0;
    }

    .stApp {
        background: #0a0a0f;
    }

    h1, h2, h3 {
        font-family: 'Syne', sans-serif !important;
    }

    .aegis-header {
        text-align: center;
        padding: 2.5rem 0 1rem 0;
    }

    .aegis-title {
        font-family: 'Syne', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #00f5c4 0%, #0099ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }

    .aegis-subtitle {
        font-family: 'DM Mono', monospace;
        font-size: 0.78rem;
        color: #6b7280;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 0.4rem;
    }

    .section-card {
        background: #13131f;
        border: 1px solid #1e1e2e;
        border-radius: 12px;
        padding: 1.8rem;
        margin: 1.2rem 0;
    }

    .section-label {
        font-family: 'Syne', sans-serif;
        font-size: 0.7rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #00f5c4;
        margin-bottom: 1rem;
    }

    .result-unacceptable {
        background: linear-gradient(135deg, #1a0505 0%, #2d0a0a 100%);
        border: 1px solid #7f1d1d;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1.5rem;
    }

    .result-high {
        background: linear-gradient(135deg, #1a0d00 0%, #2d1800 100%);
        border: 1px solid #7c2d12;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1.5rem;
    }

    .result-limited {
        background: linear-gradient(135deg, #0f1a00 0%, #1a2d00 100%);
        border: 1px solid #365314;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1.5rem;
    }

    .result-minimal {
        background: linear-gradient(135deg, #001a14 0%, #002d22 100%);
        border: 1px solid #064e3b;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1.5rem;
    }

    .risk-tier-label {
        font-family: 'Syne', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .rationale-box {
        background: rgba(0,0,0,0.3);
        border-left: 3px solid #00f5c4;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.85rem;
        color: #9ca3af;
        font-style: italic;
    }

    .obligation-item {
        display: flex;
        align-items: flex-start;
        gap: 0.6rem;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        font-size: 0.85rem;
        color: #d1d5db;
    }

    .obligation-number {
        color: #00f5c4;
        font-weight: 600;
        min-width: 1.5rem;
    }

    .footer-text {
        text-align: center;
        font-size: 0.72rem;
        color: #374151;
        padding: 2rem 0 1rem 0;
        letter-spacing: 1px;
    }

    .stSelectbox > div > div {
        background: #13131f !important;
        border: 1px solid #1e1e2e !important;
        color: #e8e8f0 !important;
    }

    .stTextInput > div > div > input {
        background: #13131f !important;
        border: 1px solid #1e1e2e !important;
        color: #e8e8f0 !important;
        font-family: 'DM Mono', monospace !important;
    }

    div[data-testid="stCheckbox"] label {
        color: #d1d5db !important;
        font-size: 0.88rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00f5c4, #0099ff) !important;
        color: #0a0a0f !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        width: 100% !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        opacity: 0.9 !important;
        transform: translateY(-1px) !important;
    }
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.markdown("""
<div class="aegis-header">
    <div class="aegis-title">⚖ AEGIS</div>
    <div class="aegis-subtitle">AI Ethics & Governance Integrated System</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#6b7280; font-size:0.85rem; margin-bottom:2rem;'>EU AI Act Risk Classification Engine — enter your AI system details to receive an instant risk assessment.</p>", unsafe_allow_html=True)


# --- Input Form ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">01 — System Details</div>', unsafe_allow_html=True)

system_name = st.text_input(
    "AI System Name",
    placeholder="e.g. Customer Credit Scoring Model",
    help="Enter the name or description of the AI system you want to classify."
)

sector = st.selectbox(
    "Sector / Domain",
    options=[
        "Select a sector...",
        "Employment & Recruitment",
        "Education & Vocational Training",
        "Financial Services & Credit",
        "Healthcare & Medical",
        "Law Enforcement",
        "Border Control & Immigration",
        "Critical Infrastructure (Energy, Water, Transport)",
        "Justice & Legal",
        "Retail & E-commerce",
        "Marketing & Advertising",
        "Public Services",
        "Other",
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">02 — System Characteristics</div>', unsafe_allow_html=True)

makes_automated_decisions = st.checkbox(
    "This system makes or assists in automated decisions that affect individuals",
    help="e.g. approving/rejecting loans, screening CVs, triaging patients"
)

is_biometric = st.checkbox(
    "This system processes biometric data (facial recognition, fingerprints, voice etc.)",
)

is_chatbot = st.checkbox(
    "This system is a chatbot, virtual assistant, or generates synthetic content",
)

is_social_scoring = st.checkbox(
    "This system scores or ranks people based on their social behaviour or personal characteristics",
)

manipulates_behaviour = st.checkbox(
    "This system uses subliminal or manipulative techniques to influence user behaviour without their awareness",
)

st.markdown('</div>', unsafe_allow_html=True)


# --- Classify Button ---
classify_clicked = st.button("🔍 CLASSIFY SYSTEM")

# --- Results ---
if classify_clicked:
    if not system_name or sector == "Select a sector...":
        st.warning("Please enter a system name and select a sector before classifying.")
    else:
        result = classify_ai_system(
            system_name=system_name,
            makes_automated_decisions_about_people=makes_automated_decisions,
            sector=sector,
            is_biometric=is_biometric,
            is_chatbot_or_generated_content=is_chatbot,
            is_social_scoring=is_social_scoring,
            manipulates_behaviour=manipulates_behaviour,
        )

        # Choose card style based on tier
        card_class = {
            "UNACCEPTABLE": "result-unacceptable",
            "HIGH": "result-high",
            "LIMITED": "result-limited",
            "MINIMAL": "result-minimal",
        }.get(result.risk_tier, "result-minimal")

        st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
        st.markdown(f'<div class="risk-tier-label">{result.label}</div>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#9ca3af; font-size:0.88rem; margin:0.3rem 0 1rem 0;">{result.description}</p>', unsafe_allow_html=True)

        st.markdown(f'<div class="rationale-box">⚡ {result.rationale}</div>', unsafe_allow_html=True)

        st.markdown('<p style="font-family:\'Syne\',sans-serif; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00f5c4; margin:1.2rem 0 0.6rem 0;">Applicable Obligations</p>', unsafe_allow_html=True)

        for i, obligation in enumerate(result.obligations, 1):
            st.markdown(f'''
            <div class="obligation-item">
                <span class="obligation-number">{i:02d}</span>
                <span>{obligation}</span>
            </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Disclaimer
        st.markdown('<p style="font-size:0.72rem; color:#374151; margin-top:1rem; text-align:center;">⚠ This tool provides indicative guidance only and does not constitute legal advice.</p>', unsafe_allow_html=True)


# --- Footer ---
st.markdown("""
<div class="footer-text">
    AEGIS — Open Source AI Governance Framework<br>
    Built by <a href="https://linkedin.com/in/kem-a-695462101" style="color:#00f5c4; text-decoration:none;">Kem Ada</a> · 
    <a href="https://github.com/Kem-Ada/AEGIS" style="color:#00f5c4; text-decoration:none;">GitHub</a> · 
    MIT License
</div>
""", unsafe_allow_html=True)

