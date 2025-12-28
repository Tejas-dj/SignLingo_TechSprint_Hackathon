import streamlit as st
import time
import os
import random
import hand_tracker 
import io
from assets import sign_dictionary
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from streamlit_option_menu import option_menu



st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', unsafe_allow_html=True)

# --- CONFIGURATION ---
st.set_page_config(
    page_title="SignLingo",
    page_icon="🤟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD EXTERNAL CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("styles.css")

# --- STATE MANAGEMENT ---
if "gesture_history" not in st.session_state:
    st.session_state["gesture_history"] = []

@st.cache_data
def load_dictionary():
    try:
        with open("words_alpha.txt", "r") as f:
            words = [line.strip().lower() for line in f.readlines()]
        return words
    except FileNotFoundError:
        return ["hello", "help", "how", "are", "you", "thank", "python", "project"]

word_list = load_dictionary()






# --- SIDEBAR ---

with st.sidebar:
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.image("logo.png", width=100)
    st.markdown('<h2 class="sidebar-title">SignLingo</h2>', unsafe_allow_html=True)
    st.markdown("---")

    app_mode = option_menu(
        menu_title=None,
        options=["Home", "Sign to Text", "Text to Sign", "Learn ASL"],
        icons=["house-fill", "camera-video-fill", "keyboard-fill", "book-half"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "padding": "10px"},
        }
    )






# --- MAIN PAGE LOGIC ---

if app_mode == "Home":
    with st.container(horizontal_alignment ="center"):
        st.image("logo.png", width=150)
        st.markdown('<h1 class="main-header">SignLingo</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Bridging the gap between silence and sound with Computer Vision and AI.</h2>', unsafe_allow_html=True)
    
    st.markdown("---")

    # 2. Body Text 
    st.markdown("""
    <div class="centered-text">
        <h3> Welcome to the Future Of Communication</h3>
        <p>SignLingo utilizes advanced Computer Vision with self a trained hand detection RNN and the Gemini AI engine to translate Sign Language in real-time.</p>
        <br>
    <p><b>Get Started:</b></p>
    <p><i class="bi bi-camera-video-fill"></i> &nbsp; <b>Sign to Text:</b> Translate hand gestures into spoken words.</p>
    <p><i class="bi bi-keyboard-fill"></i> &nbsp; <b>Text to Sign:</b> Type a sentence and see how to sign it.</p>
    <p><i class="bi bi-book-half"></i> &nbsp; <b>Learn ASL:</b> Practice your skills with our interactive tutor.</p>
</div>
    """, unsafe_allow_html=True)

    st.write("") 
    st.write("") 
    st.markdown("---")


    # Features Grid (Cards)
    st.markdown('<h3 class="section-title">Why SignLingo?</h3>', unsafe_allow_html=True)
    
    f_col1, f_col2, f_col3 = st.columns(3)
    
    with f_col1:
        st.markdown("""
        <div class="feature-card">
            <h3><i class="bi bi-camera-video-fill"></i> &nbsp;Real-Time</h3>
            <p>Zero latency translation powered by optimized MediaPipe models.</p>
        </div>
        """, unsafe_allow_html=True)

    with f_col2:
        st.markdown("""
        <div class="feature-card">
            <h3><i class="bi bi-robot"></i> &nbsp;AI Powered</h3>
            <p>Leveraging Google Gemini to understand context and complex sentences.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with f_col3:
        st.markdown("""
        <div class="feature-card">
            <h3><i class="bi bi-book-half"></i> &nbsp;Educational</h3>
            <p>Not just a translator, but a tool to help you learn ASL.</p>
        </div>
        """, unsafe_allow_html=True)










#------SIGN TO TEXT MODE ------
elif app_mode == "Sign to Text":
    st.header("Sign to Text 👆➡️📝")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        ctx = webrtc_streamer(
            key="sign_cam", 
            mode=WebRtcMode.SENDRECV,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            video_processor_factory=hand_tracker.HandDetectorProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True
        )

    with col2:
        st.subheader("Your Sentence")
        
        status_text = st.empty()
        sentence_display = st.empty()
        suggestion_box = st.empty() 
        
        # --- PREDICTIVE TEXT LOGIC ---
        history = st.session_state["gesture_history"]
        current_prefix = ""
        
        if history:
            for item in reversed(history):
                if item == " " or len(item) > 1: 
                    break
                current_prefix = item + current_prefix
        
        suggestions = []
        if current_prefix and len(current_prefix) >= 1:
            suggestions = [w for w in word_list if w.startswith(current_prefix.lower())][:3]

        if suggestions:
            st.markdown(f"**Did you mean?** (Prefix: *{current_prefix}*)")
            cols = st.columns(len(suggestions))
            for i, word in enumerate(suggestions):
                if cols[i].button(word, key=f"sugg_{word}"):
                    for _ in range(len(current_prefix)):
                        if st.session_state["gesture_history"]:
                            st.session_state["gesture_history"].pop()
                    
                    st.session_state["gesture_history"].append(word)
                    st.session_state["gesture_history"].append(" ") 
                    st.rerun()

        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state["gesture_history"] = []
            st.rerun()


    # Logic Loop
    if ctx.video_processor:
        gesture = getattr(ctx.video_processor, "detected_gesture", "Waiting...")
        
        if gesture == "space":
            gesture_to_store = " " 
        else:
            gesture_to_store = gesture

        if gesture == "Waiting..." or gesture == "..." or gesture == "None":
            status_text.info(f"Current: **Waiting...**")
        else:
            status_text.success(f"Detected: **{gesture}**")
        
        ignored_gestures = ["Waiting...", "...", "None", "Using..."]
        
        if gesture not in ignored_gestures:
            if not st.session_state["gesture_history"] or st.session_state["gesture_history"][-1] != gesture:
                st.session_state["gesture_history"].append(gesture_to_store)
                status_text.warning(f"✅ Added: **{gesture}**")
                time.sleep(0.5) 
                st.rerun()

        formatted_sentence = "".join(st.session_state["gesture_history"]) 
        if formatted_sentence:
            # Using external CSS class for the display box
            sentence_display.markdown(f"""
            <div class="sentence-box">
                <h3>{formatted_sentence}</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            sentence_display.info("Start signing...")

    if ctx.state.playing:
        time.sleep(1.0) 
        st.rerun()










#------TEXT TO SIGN ------
elif app_mode == "Text to Sign":    
    st.header("Text to Sign 📝➡️👆")
    
    with st.form(key="text_to_sign_form"):
        text_input = st.text_input("Enter word (e.g. Hello, Python)").lower().strip()
        submit_button = st.form_submit_button(label="Show Sign")

    if submit_button and text_input:
        if text_input in sign_dictionary:
            st.success(f"Showing sign for: **{text_input}**")
            st.image(sign_dictionary[text_input], width=400)
        else:
            st.warning(f"Word '{text_input}' not in dictionary. Switching to Fingerspelling...")
            
            image_placeholder = st.empty()
            text_placeholder = st.empty()
            
            for char in text_input:
                if char.isalpha():
                    img_path = f"spelling_assets/{char}.jpg"
                    
                    if os.path.exists(img_path):
                        image_placeholder.image(img_path, width=300, caption=f"Letter: {char.upper()}")
                        text_placeholder.markdown(f"## **{char.upper()}**")
                        time.sleep(0.75) 
                    else:
                        st.error(f"Missing image for letter: {char}")
                elif char == " ":
                    image_placeholder.empty()
                    text_placeholder.info("Space")
                    time.sleep(0.75)
            for int in text_input:
                if int.isdigit():
                    img_path = f"spelling_assets/{int}.jpg"
                    
                    if os.path.exists(img_path):
                        image_placeholder.image(img_path, width=300, caption=f"Number: {int}")
                        text_placeholder.markdown(f"## **{int}**")
                        time.sleep(0.75) 
                    else:
                        st.error(f"Missing image for letter: {char}")
                elif char == " ":
                    image_placeholder.empty()
                    text_placeholder.info("Space")
                    time.sleep(0.75)
            st.success("Fingerspelling Complete!")
            











#------LEARN ASL------
elif app_mode == "Learn ASL":
    st.header("Learn ASL 📚")
    st.markdown("Test your skills! Mimic the sign shown below to earn points.")

    if "game_score" not in st.session_state:
        st.session_state["game_score"] = 0
    
    valid_letters = "ABCDEFGHIKLMNOPQRSTUVWXY" 
    if "target_letter" not in st.session_state:
        st.session_state["target_letter"] = random.choice(valid_letters)

    col1, col2 = st.columns([2, 1])

    with col1:
        ctx = webrtc_streamer(
            key="learn_cam", 
            mode=WebRtcMode.SENDRECV,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            video_processor_factory=hand_tracker.HandDetectorProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True
        )

    with col2:
        # Scoreboard using external CSS
        st.markdown(f"""
        <div class="score-card">
            <h3>🏆 Score</h3>
            <h1>{st.session_state['game_score']}</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("") 

        # Challenge Letter using external CSS
        st.markdown(f"""
        <div class="challenge-card">
            <h4>Your Challenge:</h4>
            <h1>{st.session_state['target_letter']}</h1>
            <p>Show this sign to the camera!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") 


        if st.button("Skip Letter ⏭️", use_container_width=True):
            st.session_state["target_letter"] = random.choice(valid_letters)
            st.rerun()

    if ctx.video_processor:
        current_gesture = getattr(ctx.video_processor, "detected_gesture", "Waiting...")
        
        if current_gesture != "Waiting..." and current_gesture != "...":
             st.info(f"You are showing: **{current_gesture}**")

        if current_gesture == st.session_state["target_letter"]:
            st.balloons()
            st.success(f"🎉 Correct! It was {current_gesture}!")
            st.session_state["game_score"] += 1
            st.session_state["target_letter"] = random.choice(valid_letters)
            time.sleep(1.5)
            st.rerun()
            
    if ctx.state.playing:
        time.sleep(1.0)
        st.rerun()