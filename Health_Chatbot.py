import streamlit as st
from groq import Groq

# ==============================================================================
# 1. ENTERPRISE CONFIGURATION & THEME RESTRUCTURING
# ==============================================================================
st.set_page_config(
    page_title="MediQuery AI — Clinical Informatics Interface",
    layout="centered"
)

# Theme-Safe CSS Injection: Enhances layout structure without forcing text colors
st.markdown("""
    <style>
    /* Clinical Interface Header Typography */
    .clinical-header {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 2px;
    }
    /* Sub-text Definition */
    .clinical-subtitle {
        font-size: 14px;
        margin-bottom: 20px;
        opacity: 0.8;
    }
    /* Structured System Alert Panel (Uses neutral variables for full theme support) */
    .safety-panel {
        background-color: rgba(2, 132, 199, 0.08);
        border-left: 4px solid #0284c7;
        padding: 16px;
        border-radius: 4px;
        font-size: 13.5px;
        line-height: 1.5;
        margin-bottom: 24px;
    }
    /* Control Panel Sidebar Box Layouts */
    .control-card {
        background-color: rgba(128, 128, 128, 0.05);
        padding: 12px;
        border-radius: 4px;
        border: 1px solid rgba(128, 128, 128, 0.15);
        font-size: 13px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Remote Inference Client
# Replace this string with your actual active Groq API Key!
client = Groq(api_key="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")

# ==============================================================================
# 2. SYSTEM CONTROL SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("### System Configuration")
    st.markdown("---")
    
    # Technical Deployment Meta-data using adaptive background cards
    st.markdown('<div class="control-card"><b>LLM Core Endpoint:</b><br>Llama-3.1-8b-Instant</div>', unsafe_allow_html=True)
    st.markdown('<div class="control-card"><b>Inference Hardware:</b><br>Groq LPU Cluster</div>', unsafe_allow_html=True)
    st.markdown('<div class="control-card"><b>Safety Protocol:</b><br>System Prompts Enforced</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("##### Deployment Metadata")
    st.caption("Operator: Areej Fatima")
    st.caption("Affiliation: BSIT Morning A (2023-2027)")

# ==============================================================================
# 3. CORE CLINICAL INTERFACE HEADER
# ==============================================================================
st.markdown("<div class='clinical-header'>MediQuery AI Informatics Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='clinical-subtitle'>Automated natural language parsing for general health literacy and medical terminology education.</div>", unsafe_allow_html=True)

# Formal Corporate Operational Advisory Banner
st.markdown("""
    <div class="safety-panel">
        <strong>Operational Directive:</strong> This interface is restricted to delivering verified public health literature, anatomical classifications, and metabolic education. Automated filters systematically intercept and suppress commands related to definitive differential diagnostics or quantitative pharmaceutical dosing.
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. AGENT SYSTEM GUARDRAILS (PROMPT ENGINEERING)
# ==============================================================================
SYSTEM_PROMPT = """
You are a formal, professional, and objective general health query assistant designed for medical educational triage. Your purpose is to provide clear, precise, and scientifically grounded information regarding general health, lifestyle wellness, and standard medical terminology.

OPERATIONAL GUARDRAILS:
1. Medical Diagnosis Prohibition: You are not a certified physician. You must never offer formal medical diagnoses or confirm pathologies.
2. Pharmaceutical Dosing Restriction: You are strictly prohibited from prescribing or calculating drug dosages or therapeutic schedules.
3. Emergency Escalation Protocol: If the user inputs acute or life-threatening symptoms (e.g., localized chest pain, dyspnea, acute neurological deficits), you must immediately issue an explicit directive advising them to contact emergency medical services or report to the nearest emergency facility.
4. Professional Disclaimer Mandate: Every output must conclude with a standard, formal medical disclaimer stating that the information provided is for educational utility and requires clinical validation by a licensed health professional.
"""

# Initialize clean conversation arrays
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Enter your query regarding health concepts or clinical terminology below."}
    ]

# Render chat interface with standard neutral labels (Native text colors adapt automatically)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==============================================================================
# 5. LIVE INFERENCE EXECUTION LOOP
# ==============================================================================
if user_query := st.chat_input("Enter clinical terminology or health query..."):
    
    with st.chat_message("user"):
        st.markdown(user_query)
    
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Processing queries and auditing safety protocols..."):
            try:
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *st.session_state.messages
                    ],
                    temperature=0.3,
                    max_tokens=512
                )
                response = completion.choices[0].message.content
                message_placeholder.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                message_placeholder.error(f"Inference Connection Error: {str(e)}")