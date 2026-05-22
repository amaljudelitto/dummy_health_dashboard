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
    # 1. Average Wellness Score & Top 3 Concerns (Top Row)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        avg_score = int(df['Wellness Score'].mean())
        st.metric(label="Average Wellness Score", value=f"{avg_score}/100")
        
        st.subheader("Top 3 Concerns")
        top_concerns = df['Wellness Goals'].value_counts().head(3)
        for i, (concern, count) in enumerate(top_concerns.items()):
            st.write(f"**{i+1}. {concern}** ({count} users)")

    with col2:
        # 2. User Segmentation by Lifestyle
        fig_segmentation = px.pie(df, names='Lifestyle', title="User Segmentation by Lifestyle", hole=0.4)
        st.plotly_chart(fig_segmentation, width="stretch")

    st.divider() # Adds a clean horizontal line

    # 3. Stress & Activity Distributions (Middle Row)
    col3, col4 = st.columns(2)
    
    with col3:
        # Stress level distribution
        fig_stress = px.histogram(df, x="Stress Level", title="Stress Level Distribution", nbins=10)
        st.plotly_chart(fig_stress, width="stretch")
        
    with col4:
        # Activity summary
        fig_activity = px.box(df, x="Lifestyle", y="Activity Level", title="Activity Summary by Lifestyle", color="Lifestyle")
        st.plotly_chart(fig_activity, width="stretch")

    # 4. Sleep Trend (Bottom Row)
    # Since we don't have time-series dates, we show the trend across age groups
    df_sorted_age = df.sort_values(by="Age")
    fig_sleep = px.line(df_sorted_age, x="Age", y="Sleep Hours", color="Lifestyle", markers=True, title="Sleep Trend Across Ages")
    st.plotly_chart(fig_sleep, width="stretch")


elif view_mode == "Individual User Report":
    st.title("Individual Wellness Profile")
    
    selected_user = st.selectbox("Select a User ID:", df['User ID'].unique())
    user_data = df[df['User ID'] == selected_user].iloc[0]
    
    # 1. Display User Info & Wellness Score
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Age:** {user_data['Age']} | **Gender:** {user_data['Gender']}")
        st.write(f"**Lifestyle:** {user_data['Lifestyle']}")
        st.write(f"**Primary Goal:** {user_data['Wellness Goals']}")
    with col2:
        st.metric(label="Individual Wellness Score", value=f"{int(user_data['Wellness Score'])}/100")
        
    st.divider()
    
    # 2. Logic to determine Strong & Risk Areas
    strong_areas = []
    risk_areas = []
    
    if user_data['Sleep Hours'] >= 7: strong_areas.append("Healthy Sleep Routine")
    elif user_data['Sleep Hours'] < 6: risk_areas.append("Sleep Deficit")
        
    if user_data['Stress Level'] <= 4: strong_areas.append("Excellent Stress Management")
    elif user_data['Stress Level'] >= 7: risk_areas.append("High Stress Levels")
        
    if user_data['Activity Level'] >= 7: strong_areas.append("High Physical Activity")
    elif user_data['Activity Level'] < 5: risk_areas.append("Low Physical Activity")
        
    if user_data['Water Intake (L)'] >= 2.5: strong_areas.append("Optimal Hydration")
    elif user_data['Water Intake (L)'] < 1.5: risk_areas.append("Dehydration Risk")

    # Fallbacks
    if not strong_areas: strong_areas.append("Building Baseline Habits")
    if not risk_areas: risk_areas.append("No immediate risk areas detected")

    # 3. Display Strong and Risk Areas
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Strong Areas")
        for area in strong_areas:
            st.markdown(f"- ✅ {area}")
            
    with col4:
        st.subheader("Risk Areas")
        for area in risk_areas:
            st.markdown(f"- 🚩 {area}")
            
    st.divider()
    
    # 4. AI Insights (Your existing Gemini code)
    st.subheader("AI Insights")
    
    if st.button("Generate AI Recommendations"):
        with st.spinner("Analyzing profile data via Gemini..."):
            ai_response = get_ai_wellness_insights(user_data)
            st.success("Analysis Complete!")
            st.markdown(ai_response)




