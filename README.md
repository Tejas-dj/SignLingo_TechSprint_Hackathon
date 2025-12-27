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

```bash
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



## 🛠️ Prerequisites

This project is strictly dependent on **Python 3.10.0** due to specific library compatibility (MediaPipe/TensorFlow).

![Python Version](https://img.shields.io/badge/python-3.10.0-blue)

Before running the project, please ensure you have the correct version installed:

1. **Verify your Python version:**
   ```bash
   python --version
   # Output must be Python 3.10.0

---


## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/SignLingo.git
cd SignLingo

```


2. **Install Dependencies**
```bash
pip install -r requirements.txt

```


*Required libraries: `streamlit`, `streamlit-webrtc`, `mediapipe`, `tensorflow`, `opencv-python`, `google-generativeai`, `SpeechRecognition`, `gTTS`.*
3. **Setup Assets**
* Ensure `sign_language_model.h5` and `label_encoder.pkl` are in the root directory.
* Ensure the `letters/` folder contains images named `a.jpg`, `b.jpg`, etc., for the fingerspelling engine.
* Ensure `logo.png` is present.


4. **Run the App**
```bash
streamlit run app.py

---

## 🔑 Configuration & API Key

To fully utilize the **AI Grammar Correction** (Sign-to-Text) and **Voice Input** features, the app requires a Google Gemini API Key.

> **👨‍⚖️ For Judges:**
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
For the most accurate detection:
* Ensure your hand is clearly visible and well-lit.
* Keep your hand within the camera frame at all times.
* Avoid cluttered backgrounds if possible.

---


## 🧠 How It Works

1. **Landmark Extraction:** The app uses MediaPipe to extract 21 3D coordinates (x, y, z) from the user's hand in real-time.
2. **Normalization:** These coordinates are normalized relative to the wrist to ensure the system works regardless of hand position or camera distance.
3. **Classification:** The normalized data is fed into a Feed-Forward Neural Network which classifies the gesture into one of 26 ASL alphabets.
4. **Verification:** A "Stability Buffer" checks the last 15 frames. If the prediction is consistent, the character is confirmed and added to the sentence.

---

## ❓ Troubleshooting

**Camera not working / "Connection taking too long"?**

1. **Check Permissions:** Ensure your browser has allowed camera access.
2. **Network Firewalls:** If you are on a College/Office WiFi, the connection might be blocked. Try switching to a **Mobile Hotspot**.
3. **Browser:** Try using Google Chrome or Edge for best compatibility.

---

## 🔮 Future Scope

* **Dynamic Gesture Recognition:** Expanding the model to recognize moving gestures (like "Thank You" or "J") using LSTM (Long Short-Term Memory) networks.
* **Mobile App:** Porting the logic to Flutter/React Native for mobile accessibility.
* **Regional Languages:** Adding support for ISL (Indian Sign Language).

---


## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

* **Kaggle:** For the ASL Alphabet Dataset.
* **Google:** For the Gemini API and MediaPipe solutions.
* **Streamlit:** For the amazing web framework.


## 👨‍💻 Team

* **Varsha.Suresh**
* *Second Year Engineering CSE-(AIML), GSSS*
* **Tejas.D.J**
* *First Year Engineering (AIML), BMSCE*
