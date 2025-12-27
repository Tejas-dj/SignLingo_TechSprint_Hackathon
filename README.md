# 🤟 SignLingo: AI-Powered Bidirectional Sign Language Translator

**SignLingo** is a real-time accessibility tool designed to bridge the communication gap between the Deaf/Hard-of-Hearing community and the hearing world. Built with advanced Computer Vision and Generative AI, it provides seamless **Sign-to-Text** and **Text-to-Sign** translation.

---

## 🚀 Key Features

### 1. 📷 Real-Time Sign to Text
* **Custom AI Model:** Uses a custom-trained TensorFlow/Keras Neural Network (trained on the Kaggle ASL Alphabet dataset) to recognize hand gestures with 95%+ accuracy.
* **Smart Stabilization:** Implements a `Deque` sliding window algorithm to remove "flickering" and ensure smooth letter detection.
* **Predictive Text:** Auto-complete engine suggests words as you spell (e.g., spelling "P-Y-T" suggests "PYTHON"), significantly speeding up communication.
* **AI Grammar Correction:** Raw sign outputs (e.g., "ME GO STORE") are converted into fluent English sentences using **Google Gemini 1.5 Flash**.

### 2. 🤖 Text to Sign (The "Infinite Dictionary")
* **Visual Translation:** Converts text input into dynamic Sign Language GIFs.
* **Fingerspelling Engine:** If a word (e.g., "ChatGPT") is not in the GIF database, the system automatically falls back to **Fingerspelling** the word letter-by-letter using a visual asset library.
* **Voice Input:** Integrated Speech-to-Text allows hearing users to speak into the microphone to generate signs instantly.

### 3. 🎮 Gamified Learning Mode
* **Interactive Tutor:** A "Duolingo-style" module that challenges users to mimic specific ASL signs.
* **Real-time Feedback:** Uses Computer Vision to score the user's accuracy instantly.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit (Python)
* **Computer Vision:** MediaPipe (Hand Landmarks), OpenCV
* **AI/ML:** TensorFlow (Keras), Scikit-Learn
* **Generative AI:** Google Gemini API (Grammar Correction)
* **Speech:** Google SpeechRecognition, gTTS (Google Text-to-Speech)
* **Hardware Acceleration:** Optimized for NVIDIA RTX GPUs (tested on RTX 3050).

---

## 📂 Project Structure

```text
SignLingo/
├── letters&numbers/    # Database of images for the Fingerspelling Engine
├── venv/               # Python Virtual Environment
├── app.py              # Main application entry point (Streamlit)
├── assets.py           # Logic for GIF mappings and static assets
├── create_dataset.py   # Script to convert raw images into landmark CSV
├── gemini_ai.py        # AI module for Grammar Correction & TTS
├── hand_landmarks.csv  # Processed dataset of 21-point hand coordinates
├── hand_tracker.py     # Real-time MediaPipe detection & stability logic
├── label_encoder.pkl   # Decodes model predictions back to letters (0->A)
├── logo.png            # Local logo file
├── requirements.txt    # List of dependencies
├── sign_language_model.h5 # The trained Custom Neural Network
├── styles.css          # Custom CSS for "Aurora" theme and UI
├── train_model.py      # Script used to train the Neural Network
├── words_alpha.txt     # English dictionary for Predictive Text
└── README.md           # Project Documentation

```

---

## 🛠️ Prerequisites

This project is strictly dependent on **Python 3.10.0** due to specific library compatibility (MediaPipe/TensorFlow).

Before running the project, please ensure you have the correct version installed:

1. **Verify your Python version:**
```bash
python --version
# Output must be Python 3.10.0

```



---

## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone [https://github.com/yourusername/SignLingo.git](https://github.com/yourusername/SignLingo.git)
cd SignLingo

```


2. **Install Dependencies**
```bash
pip install -r requirements.txt

```


*Required: `streamlit`, `streamlit-webrtc`, `mediapipe`, `tensorflow`, `opencv-python`, `google-generativeai`, `SpeechRecognition`, `gTTS`.*
3. **Setup Assets**
* Ensure `sign_language_model.h5` and `label_encoder.pkl` are in the root directory.
* Ensure the `letters/` folder contains images named `a.jpg`, `b.jpg`, etc.
* Ensure `logo.png` is present.


4. **Run the App**
```bash
streamlit run app.py

```



---

## 🔑 Configuration & API Key

To fully utilize the **AI Grammar Correction** and **Voice Input** features, the app requires a Google Gemini API Key.

> [!IMPORTANT]
> **For Judges:**
> A temporary API key has been provided below for evaluation purposes. Please copy and paste this into the **sidebar** of the application when prompted.
> **API Key:** `AIzaSyDAUHQgv74CG-svuUweXBeYMqKTjKM3FuU`
> *(Note: This key is restricted and will be revoked after the hackathon evaluation period.)*

---

## ⚠️ Usage & Limitations

### ✋ Left-Hand Only Detection

**Important:** The current AI model has been trained exclusively on **left-hand** data.

* ✅ **DO:** Use your **LEFT HAND** to perform sign language gestures.
* ❌ **DON'T:** Use your right hand; the model will not recognize the gestures accurately.

### 💡 Best Practices

* Ensure your hand is clearly visible and well-lit.
* Keep your hand within the camera frame at all times.
* Avoid cluttered backgrounds.

---

## 🧠 How It Works

1. **Landmark Extraction:** Extracts 21 3D coordinates (x, y, z) using MediaPipe.
2. **Normalization:** Coordinates are normalized relative to the wrist.
3. **Classification:** Data is fed into a Feed-Forward Neural Network.
4. **Verification:** A "Stability Buffer" checks the last 15 frames for consistency.

---

## ❓ Troubleshooting

**Camera not working?**

1. **Check Permissions:** Ensure your browser has allowed camera access.
2. **Network Firewalls:** If on a College/Office WiFi, try a **Mobile Hotspot**.
3. **Browser:** Use Google Chrome or Edge.

---

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

* **Kaggle:** For the ASL Alphabet Dataset.
* **Google:** For the Gemini API and MediaPipe.
* **Streamlit:** For the web framework.

---

## 👨‍💻 Team

* **Varsha Suresh** - *Second Year Engineering CSE-(AIML), GSSS*
* **Tejas D.J** - *First Year Engineering (AIML), BMSCE*
