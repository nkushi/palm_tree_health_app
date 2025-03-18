import streamlit as st
import pandas as pd
from PIL import Image

# App Title
st.title("🌴 Palm Tree Health Monitoring Guide")

# Sidebar Navigation
menu = ["Home", "Pest Prevention Tips", "Tree Maintenance Checklist", "Image Comparison"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.header("Welcome to the Palm Tree Health Monitoring Guide")
    st.write("This app helps farmers and plantation owners maintain healthy palm trees and detect potential infestations early.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9a/Palm_Tree.jpg", caption="Healthy Palm Trees", use_column_width=True)

# Pest Prevention Tips Page
elif choice == "Pest Prevention Tips":
    st.header("🌿 Pest Prevention Tips")
    st.write("### How to Keep Your Palm Trees Healthy")
    tips = [
        "Regularly inspect palm trees for early signs of infestation.",
        "Prune dead or weak fronds to prevent pest breeding grounds.",
        "Avoid mechanical damage to the trunk, as it can attract pests.",
        "Use pheromone traps to monitor and control Red Palm Weevils.",
        "Ensure proper irrigation and fertilization for strong, pest-resistant trees."
    ]
    for tip in tips:
        st.markdown(f"- {tip}")

# Tree Maintenance Checklist
elif choice == "Tree Maintenance Checklist":
    st.header("✅ Palm Tree Maintenance Checklist")
    checklist = {
        "Are the leaves green and healthy?": False,
        "Are there any visible holes in the trunk?": False,
        "Are there any unusual sounds inside the trunk?": False,
        "Is there sap oozing from the tree?": False,
        "Are there any weak or drooping fronds?": False
    }
    responses = {}
    for question in checklist:
        responses[question] = st.checkbox(question)
    if st.button("Submit Checklist"):
        st.success("Thank you! Based on your responses, if you notice issues, consider further inspection.")

# Image Comparison (Basic Image Uploader)
elif choice == "Image Comparison":
    st.header("📸 Compare Your Palm Tree Images")
    uploaded_file = st.file_uploader("Upload an image of your palm tree", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Ensure that your palm tree has no visible signs of infestation such as holes or discoloration.")

# Footer
st.markdown("---")
st.markdown("Developed using **Streamlit**. Free to use and deploy!")
