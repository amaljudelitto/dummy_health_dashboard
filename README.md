# 🌿 AyurGenX Health Analytics Dashboard

A dynamic, interactive dashboard built to visualize user wellness metrics, identify lifestyle trends, and generate personalized health insights using Google's Gemini 2.0 AI.

👉 **[Click Here to View the Live Dashboard](https://ayurgenxdashboard-wmstgf8esjnnd6ndxhn2ua.streamlit.app/)**

---

## 🎯 Project Overview
This project was developed to demonstrate full-stack data handling, from programmatic generation to AI-driven analysis. It consists of three main engines:
1. **The Data Generator:** A Python script that builds a realistic, mathematically weighted dataset of 50 dummy users.
2. **The Visualization Layer:** A Streamlit interface utilizing Plotly for interactive, global health trend analysis.
3. **The AI Engine:** An integration with the Gemini 2.0 Flash API to provide actionable, personalized wellness recommendations based on individual user parameters.

---

## 🚀 How to Use the Live App (Recommended)
Simply click the link at the top of this page! The app is hosted on Streamlit Community Cloud. 
* Use the **Sidebar Navigation** to switch between the Global Overview and the Individual User Report.
* In the Individual tab, select a User ID and click **Generate AI Recommendations** to see the LLM in action.

---

## 💻 How to Run Locally (For Technical Reviewers)

If you prefer to run the architecture on your local machine, follow these steps:

### 1. Prerequisites
* Python 3.9+ installed
* Git installed
* A valid Gemini API Key (from Google AI Studio)

### 2. Installation Setup
Open your terminal and run the following commands:

```bash
# Clone the repository
git clone [https://github.com/amaljudelitto/dummy_health_dashboard.git](https://github.com/amaljudelitto/dummy_health_dashboard.git)
cd dummy_health_dashboard

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt

# Creating dummy data
run generate_data.py after changing the name for the csv file which will be generated to
create a new set of dummy data or feel free to use the csv file which is already generated.

# Running the Streamlit app
run app.py to create a new streamlit app with the newly generated dummy data.

