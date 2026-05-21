import streamlit as st
import pandas as pd
import plotly.express as px
from llm_engine import get_ai_wellness_insights

# 1. Page Configuration

st.set_page_config(
    page_title="Dummy Health Analytics",
    page_icon="🌿",
    layout="wide"
)

st.sidebar.warning("⚠️ This dashboard provides wellness and preventive insights only, not medical diagnosis or treatment. (Dummy logic applied)")

@st.cache_data
def load_data():
    return pd.read_csv("dummy_health_data.csv")

df = load_data()

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
view_mode = st.sidebar.radio("Select View:", ["Global Overview", "Individual User Report"])

# 3. Main Content Routing
if view_mode == "Global Overview":
    st.title("Global Health Analytics")
    st.markdown("Overview of all 50 dummy users.")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1= st.metric(label="Average Sleep Hours", value=df['Sleep Hours'].mean())
    col2= st.metric(label="Average Stress Level", value=df['Stress Level'].mean())
    col3= st.metric(label="Average Activity Level", value=df['Activity Level'].mean())
    col4= st.metric(label="Average Water Intake (L)", value=df['Water Intake (L)'].mean())
    col5= st.metric(label="Average Digestion Score", value=df['Digestion Score'].mean())
    col6= st.metric(label="Average Energy Score", value=df['Energy Score'].mean())
    col7= st,metric(label="Average Wellness Score", value=df['Wellness Score'].mean())


elif view_mode == "Individual User Report":
    st.title("Individual Wellness Profile")
    selected_user = st.selectbox("Select a User ID:", df['User ID'].unique())
    user_data = df[df['User ID'] == selected_user].iloc[0]
    
    
    
    st.subheader("AI Insights")
    
    # Create a button to trigger the API call so it doesn't run automatically and cost money
    if st.button("Generate AI Recommendations"):
        with st.spinner("Analyzing profile data..."):
            ai_response = get_ai_wellness_insights(user_data)
            st.success("Analysis Complete!")
            st.markdown(ai_response)




