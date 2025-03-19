import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Load pest report data
pest_data_file = "pest_reports.csv"
try:
    pest_data = pd.read_csv(pest_data_file)
except FileNotFoundError:
    pest_data = pd.DataFrame(columns=["Location", "Pest Type", "Notes"])

# Load a pre-trained MobileNetV2 model for pest detection
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Define pest-related keywords for filtering predictions
pest_keywords = ["weevil", "mite", "fungus", "pest", "beetle", "insect", "damage"]

# App Title
st.title("Palm Tree Health Monitoring Guide")

# Sidebar Navigation
menu = ["Home", "Tree Maintenance Checklist", "Pest Reporting", "Pest Data Visualization", "AI Pest Detection"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.header("Welcome to the Palm Tree Health Monitoring Guide")
    st.write("This application assists farmers in maintaining healthy palm trees and detecting potential infestations early.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9a/Palm_Tree.jpg", caption="Healthy Palm Trees", use_container_width=True)

# Tree Maintenance Checklist
elif choice == "Tree Maintenance Checklist":
    st.header("Tree Maintenance Checklist")
    st.write("Ensure optimal health of palm trees by following this checklist.")
    tasks = [
        "Prune dead fronds regularly.",
        "Water adequately based on soil moisture levels.",
        "Apply fertilizers as recommended for palm trees.",
        "Inspect trees for signs of pest infestations.",
        "Ensure proper spacing between trees to reduce disease spread."
    ]
    completed_tasks = []
    for task in tasks:
        if st.checkbox(task):
            completed_tasks.append(task)
    if len(completed_tasks) == len(tasks):
        st.success("All maintenance tasks completed!")

# Pest Reporting
elif choice == "Pest Reporting":
    st.header("Pest Reporting")
    location = st.text_input("Enter the location of infestation:")
    pest_type = st.text_input("Enter pest type:")
    notes = st.text_area("Additional notes:")
    if st.button("Submit Report"):
        new_report = pd.DataFrame([[location, pest_type, notes]], columns=["Location", "Pest Type", "Notes"])
        pest_data = pd.concat([pest_data, new_report], ignore_index=True)
        pest_data.to_csv(pest_data_file, index=False)
        st.success("Pest report submitted successfully.")

# Pest Data Visualization
elif choice == "Pest Data Visualization":
    st.header("Pest Data Visualization")
    if not pest_data.empty:
        st.write("Visualizing reported pest infestations.")
        fig, ax = plt.subplots()
        pest_counts = pest_data["Pest Type"].value_counts()
        pest_counts.plot(kind="bar", ax=ax)
        ax.set_title("Reported Pest Infestations")
        ax.set_xlabel("Pest Type")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.write("No pest reports available for visualization.")

# AI Pest Detection
elif choice == "AI Pest Detection":
    st.header("AI Pest Detection")
    uploaded_pest_image = st.file_uploader("Upload an image for pest detection", type=["jpg", "png", "jpeg"])
    if uploaded_pest_image is not None:
        image = Image.open(uploaded_pest_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        image = image.resize((224, 224))
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
        predictions = model.predict(image_array)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
        
        # Filter predictions to only show pest-related results
        pest_prediction = None
        for _, label, _ in decoded_predictions:
            if any(keyword in label.lower() for keyword in pest_keywords):
                pest_prediction = label
                break
        
        if pest_prediction:
            st.write(f"### AI Prediction: {pest_prediction}")
        else:
            st.write("### AI did not detect a known pest. Further inspection is recommended.")
