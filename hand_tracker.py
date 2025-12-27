import cv2
import av
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pickle
from streamlit_webrtc import VideoProcessorBase
from collections import deque, Counter

# --- CONFIGURATION ---
MODEL_PATH = 'sign_language_model.h5'
ENCODER_PATH = 'label_encoder.pkl'

class HandDetectorProcessor(VideoProcessorBase):
    def __init__(self):
        # 1. Load the "Brain" (Therained model)
        try:
            self.model = tf.keras.models.load_model(MODEL_PATH)
            with open(ENCODER_PATH, 'rb') as f:
                self.label_encoder = pickle.load(f)
            print("✅ Model & Encoder Loaded Successfully")
        except Exception as e:
            st.error(f"Error loading model: {e}")
            self.model = None

        # 2. Initialize MediaPipe (The Eyes)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

        # 3. Stability Buffer (Prevents flickering between 'A' and 'B')
        self.history = deque(maxlen=20)
        self.detected_gesture = "Waiting..."

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.flip(img, 1) # Mirror image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = self.hands.process(img_rgb)
        
        gesture = "Waiting..." # Default state

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw skeleton
                self.mp_drawing.draw_landmarks(
                    img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # --- PREPROCESSING (Must match create_dataset.py exactly) ---
                # 1. Extract coordinates relative to WRIST (Point 0)
                base_x = hand_landmarks.landmark[0].x
                base_y = hand_landmarks.landmark[0].y
                
                input_data = []
                for lm in hand_landmarks.landmark:
                    # Normalize: Subtract wrist position
                    input_data.append(lm.x - base_x)
                    input_data.append(lm.y - base_y)

                # --- PREDICTION ---
                if self.model:
                    # Reshape for model: (1, 42)
                    input_np = np.array(input_data).reshape(1, -1)
                    
                    # Get prediction (Probability distribution)
                    prediction = self.model.predict(input_np, verbose=0)
                    
                    # Find the class with highest probability
                    class_id = np.argmax(prediction)
                    confidence = np.max(prediction)
                    
                    # Only accept if confidence is high (> 70%)
                    if confidence > 0.7:
                        gesture = self.label_encoder.inverse_transform([class_id])[0]
                    else:
                        gesture = "..."

        # --- STABILIZATION LOGIC ---
        self.history.append(gesture)
        most_common, frequency = Counter(self.history).most_common(1)[0]
        
        # If 15 out of last 20 frames are the same, lock it in
        if frequency > 15:
            self.detected_gesture = most_common

        # Debug Text on Screen
        cv2.putText(img, f"Output: {self.detected_gesture}", (10, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")