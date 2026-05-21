import pandas as pd
import numpy as np
import random

# 1. Set the seed so your random numbers stay consistent every time you run it
np.random.seed(42)
random.seed(42)

# 2. Define the size of the dataset
num_users = 50

# 3. Create lists to hold your columns
user_ids = [f"USER_{str(i).zfill(3)}" for i in range(1, num_users + 1)]
ages = []
genders = []
lifestyles = []
sleep_hours = []
stress_levels = []
activity_levels = []
water_intakes = []
digestion_scores = []
energy_scores = []
wellness_goals = []

# 4. Loop 50 times to generate realistic human data
for i in range(num_users):
    # Use standard python random/numpy functions to fill out the attributes
    ages.append(random.randint(18, 65))
    genders.append(random.choice(['Male', 'Female', 'Other']))
    lifestyles.append(random.choice(['Student', 'Working Professional', 'Founder', 'Homemaker']))
    wellness_goals.append(random.choice(['Stress', 'Sleep', 'Digestion', 'Weight', 'Detox', 'Energy']))
    sleep_hours.append(round(random.uniform(4.0, 9.0), 1))
    stress_levels.append(round(random.uniform(0.0, 10.0), 1))
    activity_levels.append(round(random.uniform(0.0, 10.0), 1))
    water_intakes.append(round(random.uniform(1.0, 4.0), 1))
    digestion_scores.append(round(random.uniform(0.0, 10.0), 1))
    energy_scores.append(round(random.uniform(0.0, 10.0), 1))

data = {
    "User ID": user_ids,
    "Age": ages,
    "Gender": genders,
    "Lifestyle": lifestyles,
    "Sleep Hours": sleep_hours,
    "Stress Level": stress_levels,
    "Activity Level": activity_levels,
    "Water Intake (L)": water_intakes,
    "Digestion Score": digestion_scores,
    "Energy Score": energy_scores,
    "Wellness Goals": wellness_goals,
}

# Turning into a DataFrame
df = pd.DataFrame(data)
sleep_score = (df['Sleep Hours'] / 8.0).clip(upper=1.0) * 25  
stress_score = ((10 - df['Stress Level']) / 9.0).clip(upper=1.0) * 20      
activity_score = (df['Activity Level'] / 10.0) * 15          
water_score = (df['Water Intake (L)'] / 3.0).clip(upper=1.0) * 20 
digestion_score = (df['Digestion Score'] / 10.0) * 10
energy_score = (df['Energy Score']/ 10.0) * 10

# Summing up and rounding to a clean whole number
df['Wellness Score'] = round(sleep_score + stress_score + activity_score + water_score + digestion_score + energy_score)

df.to_csv("dummy_health_data.csv", index=False)
print("Data generated and Wellness Scores calculated successfully!")