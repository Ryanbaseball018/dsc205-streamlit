import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the diabetes dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/diabetes_nan.csv"
df = pd.read_csv(url)

# Title
st.title("Diabetes Patient Dashboard")

st.markdown(
    "This dashboard uses a diabetes dataset containing information about patients "
    "and their medical measurements. Use the radio buttons to compare diabetic and "
    "non-diabetic patients."
)

# Radio button
st.subheader("Select Patient Group")

selection = st.radio(
    "Choose a group:",
    ["All Patients", "Diabetic", "Non-Diabetic"]
)

# Filter the data
if selection == "Diabetic":
    filtered_df = df[df["Outcome"] == 1]
elif selection == "Non-Diabetic":
    filtered_df = df[df["Outcome"] == 0]
else:
    filtered_df = df

# Display selected data
st.subheader("Patient Data")

st.write(f"Number of patients: {len(filtered_df)}")

st.dataframe(filtered_df)

# Calculate averages
numeric_columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "Age"
]

averages = filtered_df[numeric_columns].mean()

# Create bar chart
st.subheader("Average Patient Measurements")

fig, ax = plt.subplots()

ax.bar(averages.index, averages.values)

ax.set_xlabel("Measurement")
ax.set_ylabel("Average Value")
ax.set_title(f"Average Measurements - {selection}")

plt.xticks(rotation=45)

st.pyplot(fig, clear_figure=True)
