import streamlit as st
from PIL import Image
import ocr_module
import simplify_module
import demo_module
import tts_module

"""
AI Medicine Label Explainer (Main Application)
----------------------------------------------
This application helps elderly users understand medicine labels easily.
It reads text from a medicine image and explains it in simple language using AI.
The app works fully offline, uses open-source tools, and does not provide medical advice—only explains what is written on the label.
"""

# Configure page
st.set_page_config(
    page_title="AI Medicine Label Explainer",
    page_icon="💊",
    layout="centered"
)

# --- Custom CSS for clean UI ---
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #444;
        text-align: center;
        margin-bottom: 25px;
    }
    .disclaimer-box {
        background-color: #FFF3CD;
        color: #856404;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #FFEEBA;
        margin-top: 30px;
        font-size: 1.1rem;
        text-align: center;
        font-weight: bold;
    }
    .result-box {
        background-color: #F0F8FF; /* AliceBlue */
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #cbd5e0;
        font-size: 1.3rem; /* Larger text for elderly */
        line-height: 1.8;
        color: #2d3748;
    }
    /* Enhance standard Streamlit elements */
    .stButton button {
        font-size: 1.2rem !important;
        height: 3em !important;
        width: 100%;
    }
    div[data-testid="stMarkdownContainer"] h2 {
        font-size: 1.8rem !important;
        color: #2c5282;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-header">💊 Medicine Explainer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Simple & Easy to read medicine labels</div>', unsafe_allow_html=True)

# --- Controls ---
language = st.radio("Select Language / மொழியைத் தேர்ந்தெடுக்கவும்:", ["English", "Tamil"], horizontal=True)
st.markdown("---")

# --- Sidebar ---
st.sidebar.info("Tip: Ensure the photo is clear and well-lit.")

# --- Session State ---
if 'image_input' not in st.session_state:
    st.session_state.image_input = None
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

# --- Main Content ---
# --- Main Content ---

# Tabs for Upload vs Demo
tab1, tab2 = st.tabs(["📤 Upload Image", "🖼️ Try Demo"])

with tab1:
    uploaded_file = st.file_uploader("Choose a photo...", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        st.session_state.image_input = Image.open(uploaded_file)
        st.session_state.file_uploaded = True
        st.session_state.show_explanation = False # Reset for new upload

with tab2:
    if st.button("🚀 Load & Run Demo Image"):
        demo_image = demo_module.get_demo_image()
        if demo_image is None:
            st.error("Demo image not found in assets/ folder.")
        else:
            st.session_state.image_input = demo_image
            st.session_state.file_uploaded = False # It's a demo, not an upload
            st.session_state.show_explanation = True # Trigger auto-explanation for demo
            st.success("Demo image loaded!")

# Process Image
if st.session_state.image_input:
    st.image(st.session_state.image_input, caption="Medicine Label", width=400)
    
    # Check if we should show explanation (Manual Click OR Auto-Demo)
    if st.button("🔍 Explain Label", type="primary"):
        st.session_state.show_explanation = True
    
    if st.session_state.get('show_explanation', False):
        with st.spinner(f"Reading text and explaining in {language}..."):
            extracted_text = ocr_module.extract_text(st.session_state.image_input)
        
        if not extracted_text:
            st.error("Could not find any text in the image. Please try a clearer photo.")
        else:
            with st.expander("View Extracted Text (Debug)"):
                st.text(extracted_text)
                
            with st.spinner(f"Simplifying..."):
                explanation = simplify_module.simplify_text(extracted_text, language)
            
            st.markdown("### 📋 Explanation:")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(explanation)
            st.markdown('</div>', unsafe_allow_html=True)

            # --- TTS Section ---
            st.markdown("---")
            if st.button("🔊 Read Out Loud / சத்தமாக வாசிக்கவும்"):
                with st.spinner("Generating audio..."):
                    # Remove markdown symbols for cleaner speech
                    clean_text = explanation.replace("#", "").replace("*", "")
                    audio_file = tts_module.text_to_speech(clean_text)
                    if audio_file:
                        st.audio(audio_file, format='audio/mp3')
                    else:
                        st.error("Could not generate audio.")

# --- Disclaimer ---
st.markdown("""
    <div class="disclaimer-box">
        ⚠️ <strong>Disclaimer:</strong> This app explains only the text written on the medicine label. 
        It does not provide medical advice. Consult a doctor for any health concerns.
    </div>
""", unsafe_allow_html=True)
