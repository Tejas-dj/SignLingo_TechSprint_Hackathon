import os
import cv2
import mediapipe as mp
import csv
import numpy as np

# --- CONFIGURATION ---
# THIS IS POINTED TO THE KAGGLE DATASET FOLDER
# Structure should be: dataset/A/img1.jpg, dataset/B/img2.jpg...
DATA_DIR = r"C:\Users\Tejas.D.Jaiprakash\Documents\Datasets\ASL ALPHABET\asl_alphabet_train\asl_alphabet_train" 

# Output file
OUTPUT_FILE = "hand_landmarks.csv"

# --- MEDIAPIPE SETUP ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.3)

# --- HELPER: NORMALIZE LANDMARKS ---
def get_normalized_landmarks(landmarks):
    # Convert to a flat list [x1, y1, x2, y2...]
    # We make them relative to the WRIST (point 0) so the hand position on screen doesn't matter
    base_x, base_y = landmarks[0].x, landmarks[0].y
    
    normalized = []
    for lm in landmarks:
        normalized.append(lm.x - base_x)
        normalized.append(lm.y - base_y)
        
    return normalized

# --- MAIN LOOP ---
print(f"🚀 Starting processing from: {DATA_DIR}")

# Prepare CSV file
with open(OUTPUT_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Header: label, x0, y0, ... x20, y20
    header = ['label']
    for i in range(21):
        header.extend([f'x{i}', f'y{i}'])
    writer.writerow(header)

    # Loop through A-Z folders
    for label in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, label)
        if not os.path.isdir(path):
            continue
            
        print(f"📂 Processing Class: {label}...")
        
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            
            # Read Image
            img = cv2.imread(img_path)
            if img is None: continue
            
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Get the math coordinates
                    data = get_normalized_landmarks(hand_landmarks.landmark)
                    
                    # Save: [Label, x0, y0, ... y20]
                    writer.writerow([label] + data)

print("✅ Done! Data saved to hand_landmarks.csv")