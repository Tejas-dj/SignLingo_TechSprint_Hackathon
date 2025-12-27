import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 1. LOAD DATA
print("📂 Loading dataset...")
data = pd.read_csv('hand_landmarks.csv')

X = data.iloc[:, 1:].values # Coordinates (Input)
y = data.iloc[:, 0].values  # Labels (Output)

# 2. ENCODE LABELS (A -> 0, B -> 1, etc.)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save the label mapping so we know 0 = A later
import pickle
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# 3. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 4. BUILDING THE "BRAIN" (MODEL)
# Simple Feed-Forward Neural Network
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(42,)),          # 21 points * 2 coords (x,y)
    tf.keras.layers.Dense(128, activation='relu'), # Hidden Layer 1
    tf.keras.layers.Dropout(0.2),                # Prevents overfitting
    tf.keras.layers.Dense(64, activation='relu'),  # Hidden Layer 2
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax') # Output Layer (A-Z)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. TRAIN
print("🚀 Training model on RTX 3050...")
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# 6. SAVE
model.save('sign_language_model.h5')
print("✅ Model saved as 'sign_language_model.h5'")