# Palm Tree Health Monitoring Guide

## Overview
This application is designed to help farmers and agricultural professionals monitor palm tree health, report pest infestations, and visualize data on pest occurrences. The application also includes an AI-powered pest detection feature to analyze uploaded images and identify potential threats to palm trees.

## Features
- **Tree Maintenance Checklist**: Interactive checklist to ensure proper tree care.
- **Pest Reporting**: Users can submit reports on detected pests, including location and details.
- **Pest Data Visualization**: Displays a summary of reported pest occurrences.
- **AI Pest Detection**: Uses a machine learning model to classify potential pest infestations based on uploaded images.

## AI Pest Detection - Limitations and Issues
The AI model currently in use is based on **MobileNetV2**, a pre-trained model trained on the ImageNet dataset. However, **ImageNet does not specialize in palm tree pests**, which leads to inaccurate classifications. To address this:
- The app **filters predictions** to only display pest-related results.
- The model is **not specifically trained on palm tree pests**, so results may not always be reliable.
- A more effective approach would involve **fine-tuning the model on a dedicated dataset** of palm tree pests and diseases.

## Future Improvements
To enhance the application, the following improvements can be made:
- **Custom AI Model**: Train a dedicated machine learning model specifically for palm tree pests and diseases.
- **Integration with a Pest Database**: Cross-reference detected pests with a verified database for better accuracy.
- **Improved Reporting System**: Allow users to attach images to reports and categorize pest severity.
- **Mobile-Friendly UI**: Optimize the interface for mobile use to improve accessibility for field workers.

## Setup Instructions
1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/palm_tree_health_app.git
   ```
2. Navigate to the project directory:
   ```sh
   cd palm_tree_health_app
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   streamlit run app.py
   ```

## Contribution
If you would like to contribute to this project, please feel free to submit a pull request with improvements or bug fixes.

