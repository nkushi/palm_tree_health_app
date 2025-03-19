import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load pest report data
pest_data_file = "pest_reports.csv"
try:
    pest_data = pd.read_csv(pest_data_file)
except FileNotFoundError:
    pest_data = pd.DataFrame(columns=["Location", "Pest Type", "Notes"])

# App Title
st.title("🌴 Palm Tree Health Monitoring Guide")

# Sidebar Navigation
menu = ["Home", "Pest Prevention Tips", "Tree Maintenance Checklist", "Image Comparison", "Disease Database", "Pest Reporting", "Pest Data Visualization"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.header("Welcome to the Palm Tree Health Monitoring Guide")
    st.write("This app helps farmers maintain healthy palm trees and detect potential infestations early.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Palm_Tree.jpg/800px-Palm_Tree.jpg", 
         caption="Healthy Palm Trees", use_container_width=True)


# Pest Prevention Tips Page
elif choice == "Pest Prevention Tips":
    st.header("🌿 Pest Prevention Tips")
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
        st.success("Thank you! If you notice issues, consider further inspection.")

# Image Comparison (Basic Image Uploader)
elif choice == "Image Comparison":
    st.header("📸 Compare Your Palm Tree Images")
    uploaded_file = st.file_uploader("Upload an image of your palm tree", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Ensure your palm tree has no visible signs of infestation such as holes or discoloration.")

# Disease Database
elif choice == "Disease Database":
    st.header("🌿 Common Palm Tree Diseases")
    diseases = {
        "Lethal Yellowing": "Affects the vascular system, causing frond yellowing and fruit drop.",
        "Ganoderma Butt Rot": "Fungal disease that causes decay at the base of the trunk.",
        "Fusarium Wilt": "Affects fronds, causing one-sided yellowing and wilting.",
        "Red Palm Weevil Infestation": "Larvae burrow into the trunk, leading to structural weakness."
    }
    for disease, description in diseases.items():
        st.subheader(disease)
        st.write(description)

# Pest Reporting
elif choice == "Pest Reporting":
    st.header("📍 Report a Pest Sighting")
    location = st.text_input("Enter Location:")
    pest_type = st.selectbox("Select Pest Type:", ["Red Palm Weevil", "Spider Mites", "Fungal Infection", "Other"])
    notes = st.text_area("Additional Notes:")
    if st.button("Submit Report"):
        new_entry = pd.DataFrame([[location, pest_type, notes]], columns=["Location", "Pest Type", "Notes"])
        pest_data = pd.concat([pest_data, new_entry], ignore_index=True)
        pest_data.to_csv(pest_data_file, index=False)
        st.success("Pest report submitted successfully!")

# Pest Data Visualization
elif choice == "Pest Data Visualization":
    st.header("📊 Pest Report Data")
    if not pest_data.empty:
        st.write("### Recent Pest Reports")
        st.dataframe(pest_data)
        st.write("### Pest Type Distribution")
        fig, ax = plt.subplots()
        pest_data["Pest Type"].value_counts().plot(kind="bar", ax=ax, color='green')
        st.pyplot(fig)
    else:
        st.info("No pest reports available yet.")

# Footer
st.markdown("---")
st.markdown("Developed using **Streamlit**. Free to use and deploy!")
