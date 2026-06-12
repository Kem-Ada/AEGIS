"""
AEGIS — AI Ethics & Governance Integrated System
# Copyright (c) 2026 Kem Ada. Licensed under the MIT License.
Streamlit UI — EU AI Act Classifier, Model Card Generator, DPIA Mapper
Author: Kem Ada | https://linkedin.com/in/kem-a-695462101
"""

import streamlit as st
from classifier import classify_ai_system, ClassificationResult
from model_card import ModelCard, generate_model_card
from dpia_mapper import assess_dpia_requirement, DPIAResult

# --- Page Config ---
st.set_page_config(
    page_title="AEGIS — AI Governance Toolkit",
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
    .stApp { background: #0a0a0f; }
    h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

    .aegis-header { text-align: center; padding: 2.5rem 0 1rem 0; }
    .aegis-title {
        font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #00f5c4 0%, #0099ff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; margin: 0;
    }
    .aegis-subtitle {
        font-family: 'DM Mono', monospace; font-size: 0.78rem; color: #6b7280;
        letter-spacing: 2px; text-transform: uppercase; margin-top: 0.4rem;
    }
    .section-label {
        font-family: 'Syne', sans-serif; font-size: 0.7rem; letter-spacing: 3px;
        text-transform: uppercase; color: #00f5c4; margin: 1rem 0;
    }
    .result-unacceptable { background: linear-gradient(135deg, #1a0505 0%, #2d0a0a 100%); border: 1px solid #7f1d1d; border-radius: 12px; padding: 2rem; margin-top: 1.5rem; }
    .result-high { background: linear-gradient(135deg, #1a0d00 0%, #2d1800 100%); border: 1px solid #7c2d12; border-radius: 12px; padding: 2rem; margin-top: 1.5rem; }
    .result-limited { background: linear-gradient(135deg, #0f1a00 0%, #1a2d00 100%); border: 1px solid #365314; border-radius: 12px; padding: 2rem; margin-top: 1.5rem; }
    .result-minimal { background: linear-gradient(135deg, #001a14 0%, #002d22 100%); border: 1px solid #064e3b; border-radius: 12px; padding: 2rem; margin-top: 1.5rem; }
    .risk-tier-label { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800; margin-bottom: 0.5rem; }
    .rationale-box { background: rgba(0,0,0,0.3); border-left: 3px solid #00f5c4; padding: 1rem 1.2rem; margin: 1rem 0; border-radius: 0 8px 8px 0; font-size: 0.85rem; color: #9ca3af; font-style: italic; }
    .obligation-item { display: flex; align-items: flex-start; gap: 0.6rem; padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.85rem; color: #d1d5db; }
    .obligation-number { color: #00f5c4; font-weight: 600; min-width: 1.5rem; }
    .footer-text { text-align: center; font-size: 0.72rem; color: #374151; padding: 2rem 0 1rem 0; letter-spacing: 1px; }

    .stTextInput > div > div > input, .stTextArea textarea {
        background: #13131f !important; border: 1px solid #1e1e2e !important;
        color: #e8e8f0 !important; font-family: 'DM Mono', monospace !important;
    }
    div[data-testid="stCheckbox"] label { color: #d1d5db !important; font-size: 0.88rem; }
    .stButton > button {
        background: linear-gradient(135deg, #00f5c4, #0099ff) !important; color: #0a0a0f !important;
        font-family: 'Syne', sans-serif !important; font-weight: 700 !important; font-size: 1rem !important;
        border: none !important; border-radius: 8px !important; padding: 0.7rem 2rem !important;
        width: 100% !important; letter-spacing: 1px !important; text-transform: uppercase !important; cursor: pointer !important;
    }
    .stButton > button:hover { opacity: 0.9 !important; transform: translateY(-1px) !important; }
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.markdown("""
<div class="aegis-header">
    <div class="aegis-title">⚖ AEGIS</div>
    <div class="aegis-subtitle">AI Ethics & Governance Integrated System</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#6b7280; font-size:0.85rem; margin-bottom:1.5rem;'>Open source AI governance toolkit — risk classification, model cards, and DPIA mapping.</p>", unsafe_allow_html=True)


# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🔴 EU AI Act Classifier", "📋 Model Card", "🗺️ DPIA Mapper"])


# ============ TAB 1: CLASSIFIER ============
with tab1:
    st.markdown('<div class="section-label">EU AI Act Risk Classification</div>', unsafe_allow_html=True)

    system_name = st.text_input("AI System Name", placeholder="e.g. Customer Credit Scoring Model", key="clf_name")
    sector = st.selectbox("Sector / Domain", options=[
        "Select a sector...", "Employment & Recruitment", "Education & Vocational Training",
        "Financial Services & Credit", "Healthcare & Medical", "Law Enforcement",
        "Border Control & Immigration", "Critical Infrastructure (Energy, Water, Transport)",
        "Justice & Legal", "Retail & E-commerce", "Marketing & Advertising", "Public Services", "Other",
    ], key="clf_sector")

    makes_automated_decisions = st.checkbox("This system makes or assists in automated decisions that affect individuals", key="clf_auto")
    is_biometric = st.checkbox("This system processes biometric data (facial recognition, fingerprints, voice etc.)", key="clf_bio")
    is_chatbot = st.checkbox("This system is a chatbot, virtual assistant, or generates synthetic content", key="clf_chat")
    is_social_scoring = st.checkbox("This system scores or ranks people based on their social behaviour or personal characteristics", key="clf_social")
    manipulates_behaviour = st.checkbox("This system uses subliminal or manipulative techniques to influence user behaviour without their awareness", key="clf_manip")

    if st.button("🔍 CLASSIFY SYSTEM", key="clf_btn"):
        if not system_name or sector == "Select a sector...":
            st.warning("Please enter a system name and select a sector before classifying.")
        else:
            result = classify_ai_system(
                system_name=system_name, makes_automated_decisions_about_people=makes_automated_decisions,
                sector=sector, is_biometric=is_biometric, is_chatbot_or_generated_content=is_chatbot,
                is_social_scoring=is_social_scoring, manipulates_behaviour=manipulates_behaviour,
            )
            card_class = {"UNACCEPTABLE": "result-unacceptable", "HIGH": "result-high", "LIMITED": "result-limited", "MINIMAL": "result-minimal"}.get(result.risk_tier, "result-minimal")
            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
            st.markdown(f'<div class="risk-tier-label">{result.label}</div>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#9ca3af; font-size:0.88rem; margin:0.3rem 0 1rem 0;">{result.description}</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="rationale-box">⚡ {result.rationale}</div>', unsafe_allow_html=True)
            st.markdown('<p style="font-family:\'Syne\',sans-serif; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00f5c4; margin:1.2rem 0 0.6rem 0;">Applicable Obligations</p>', unsafe_allow_html=True)
            for i, obligation in enumerate(result.obligations, 1):
                st.markdown(f'<div class="obligation-item"><span class="obligation-number">{i:02d}</span><span>{obligation}</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<p style="font-size:0.72rem; color:#374151; margin-top:1rem; text-align:center;">⚠ This tool provides indicative guidance only and does not constitute legal advice.</p>', unsafe_allow_html=True)


# ============ TAB 2: MODEL CARD ============
with tab2:
    st.markdown('<div class="section-label">Model Card Generator</div>', unsafe_allow_html=True)

    mc_name = st.text_input("Model Name", placeholder="e.g. Customer Credit Scoring Model", key="mc_name")
    mc_version = st.text_input("Version", placeholder="e.g. v2.1", key="mc_version")
    mc_type = st.text_input("Model Type", placeholder="e.g. Gradient Boosted Decision Tree", key="mc_type")
    mc_dev = st.text_input("Developed By", placeholder="e.g. Internal Data Science Team", key="mc_dev")
    mc_date = st.text_input("Release Date", placeholder="e.g. 2024-01-15", key="mc_date")
    mc_desc = st.text_area("Model Description", placeholder="What does this model do?", key="mc_desc")
    mc_intended = st.text_area("Intended Uses (one per line)", placeholder="Assessing creditworthiness\nSupporting underwriters", key="mc_intended")
    mc_outscope = st.text_area("Out-of-Scope Uses (one per line)", placeholder="Sole automated decision-making\nInsurance screening", key="mc_outscope")
    mc_training = st.text_area("Training Data Description", placeholder="Describe the training data", key="mc_training")
    mc_sources = st.text_area("Data Sources (one per line)", placeholder="Internal database\nCredit bureau data", key="mc_sources")
    mc_perf = st.text_area("Performance Summary", placeholder="Accuracy, metrics etc.", key="mc_perf")
    mc_limits = st.text_area("Known Limitations (one per line)", placeholder="Limitation 1\nLimitation 2", key="mc_limits")
    mc_ethical = st.text_area("Ethical Considerations (one per line)", placeholder="Consideration 1\nConsideration 2", key="mc_ethical")
    mc_bias = st.text_area("Bias & Fairness Risks (one per line)", placeholder="Risk 1\nRisk 2", key="mc_bias")
    mc_oversight = st.text_area("Human Oversight", placeholder="Describe human oversight measures", key="mc_oversight")
    mc_contact = st.text_input("Contact", placeholder="e.g. ai-governance@company.com", key="mc_contact")

    if st.button("📋 GENERATE MODEL CARD", key="mc_btn"):
        if not mc_name:
            st.warning("Please enter at least a model name.")
        else:
            def to_list(text):
                return [line.strip() for line in text.split("\n") if line.strip()] or ["Not specified"]
            card = ModelCard(
                model_name=mc_name, version=mc_version or "Not specified", description=mc_desc or "Not specified",
                model_type=mc_type or "Not specified", developed_by=mc_dev or "Not specified", release_date=mc_date or "Not specified",
                intended_uses=to_list(mc_intended), out_of_scope_uses=to_list(mc_outscope),
                training_data_description=mc_training or "Not specified", data_sources=to_list(mc_sources),
                performance_summary=mc_perf or "Not specified", known_limitations=to_list(mc_limits),
                ethical_considerations=to_list(mc_ethical), bias_risks=to_list(mc_bias),
                human_oversight=mc_oversight or "Not specified", contact=mc_contact or "Not specified",
            )
            markdown_output = generate_model_card(card)
            st.markdown('<div class="result-minimal">', unsafe_allow_html=True)
            st.markdown("**✅ Model card generated!** Copy the markdown below or download it.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.code(markdown_output, language="markdown")
            st.download_button("⬇️ Download Model Card", markdown_output, file_name=f"{mc_name.replace(' ','_')}_model_card.md", mime="text/markdown")


# ============ TAB 3: DPIA MAPPER ============
with tab3:
    st.markdown('<div class="section-label">GDPR Article 35 DPIA Mapper</div>', unsafe_allow_html=True)

    dp_name = st.text_input("System Name", placeholder="e.g. Customer Credit Scoring Model", key="dp_name")
    st.markdown('<p style="color:#6b7280; font-size:0.8rem; margin-top:1rem;">Tick all that apply:</p>', unsafe_allow_html=True)

    dp_auto = st.checkbox("Makes automated decisions with significant effects on individuals", key="dp_auto")
    dp_special = st.checkbox("Processes special category data (health, race, religion, biometrics etc.)", key="dp_special")
    dp_monitor = st.checkbox("Systematically monitors publicly accessible areas", key="dp_monitor")
    dp_vulnerable = st.checkbox("Processes data of vulnerable individuals (children, employees, patients)", key="dp_vulnerable")
    dp_biometric = st.checkbox("Processes biometric data for unique identification", key="dp_biometric")
    dp_large = st.checkbox("Large-scale processing affecting many individuals", key="dp_large")
    dp_novel = st.checkbox("Uses novel or innovative technology", key="dp_novel")

    if st.button("🗺️ ASSESS DPIA REQUIREMENT", key="dp_btn"):
        if not dp_name:
            st.warning("Please enter a system name.")
        else:
            result = assess_dpia_requirement(
                system_name=dp_name, automated_decisions=dp_auto, special_category_data=dp_special,
                systematic_monitoring=dp_monitor, vulnerable_subjects=dp_vulnerable, biometric_data=dp_biometric,
                large_scale=dp_large, novel_technology=dp_novel,
            )
            card_class = "result-high" if result.dpia_required else "result-minimal"
            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
            st.markdown(f'<div class="risk-tier-label">{"⚠️ DPIA Required" if result.dpia_required else "✅ DPIA Not Mandatory"}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="rationale-box">⚡ {result.requirement_rationale}</div>', unsafe_allow_html=True)

            if result.triggered_criteria:
                st.markdown('<p style="font-family:\'Syne\',sans-serif; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00f5c4; margin:1.2rem 0 0.6rem 0;">Triggered Criteria</p>', unsafe_allow_html=True)
                for i, c in enumerate(result.triggered_criteria, 1):
                    st.markdown(f'<div class="obligation-item"><span class="obligation-number">{i:02d}</span><span>{c}</span></div>', unsafe_allow_html=True)

            st.markdown('<p style="font-family:\'Syne\',sans-serif; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00f5c4; margin:1.2rem 0 0.6rem 0;">Risks to Individuals</p>', unsafe_allow_html=True)
            for i, r in enumerate(result.risks_to_individuals, 1):
                st.markdown(f'<div class="obligation-item"><span class="obligation-number">{i:02d}</span><span>{r}</span></div>', unsafe_allow_html=True)

            st.markdown('<p style="font-family:\'Syne\',sans-serif; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00f5c4; margin:1.2rem 0 0.6rem 0;">Recommended Mitigations</p>', unsafe_allow_html=True)
            for i, m in enumerate(result.recommended_mitigations, 1):
                st.markdown(f'<div class="obligation-item"><span class="obligation-number">{i:02d}</span><span>{m}</span></div>', unsafe_allow_html=True)

            st.markdown(f'<p style="color:#d1d5db; font-size:0.85rem; margin-top:1.2rem;"><strong>Residual Risk:</strong> {result.residual_risk_level}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#d1d5db; font-size:0.85rem;"><strong>DPO Consultation Required:</strong> {"Yes" if result.dpo_consultation_required else "No"}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
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
