import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Connecticut towns census dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv"

df = pd.read_csv(url)

# Title
st.title("Connecticut Town Income Dashboard")

st.markdown(
    "This dashboard uses 2020 census data for Connecticut cities and towns. "
    "Use the controls below to explore towns by county and median household income."
)

# Show the original data columns
st.subheader("Explore Connecticut Towns")

# County selectbox
county = st.selectbox(
    "Select a county:",
    sorted(df["County"].dropna().unique())
)

# Filter data by county
county_df = df[df["County"] == county]

# Display county data
st.write(f"Cities and towns in {county} County:")

st.dataframe(
    county_df,
    width=800,
    height=200
)

# Find minimum and maximum income
min_income = int(df["Median Household Income"].min())
max_income = int(df["Median Household Income"].max())

# Income slider
income_range = st.slider(
    "Select a median household income range:",
    min_value=min_income,
    max_value=max_income,
    value=(min_income, max_income),
    step=1000
)

# Filter by income range
income_df = df[
    (df["Median Household Income"] >= income_range[0]) &
    (df["Median Household Income"] <= income_range[1])
]

# Display filtered data
st.subheader("Towns Within Selected Income Range")

st.write(
    f"Median household income from "
    f"${income_range[0]:,} to ${income_range[1]:,}"
)

st.dataframe(
    income_df,
    width=800,
    height=200
)

# Highest and lowest 5 towns
lowest_5 = df.nsmallest(5, "Median Household Income")
highest_5 = df.nlargest(5, "Median Household Income")

# Combine the highest and lowest towns
graph_df = pd.concat([lowest_5, highest_5])

# Sort by income for the graph
graph_df = graph_df.sort_values("Median Household Income")

# Bar graph
st.subheader("Five Highest and Five Lowest Median Household Incomes")

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    graph_df["Town"],
    graph_df["Median Household Income"]
)

ax.set_xlabel("City / Town")
ax.set_ylabel("Median Household Income ($)")
ax.set_title("Five Highest and Five Lowest Median Household Incomes")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

st.pyplot(fig, clear_figure=True)
