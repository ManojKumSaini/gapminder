import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# App title and description
st.title("Gapminder Bubble Chart Dashboard")
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")

# Load data
file_path = Path(r'C:\Users\manoj\OneDrive\Desktop\HWR Berlin Projects\Big data\gapminder\data\final_data\merged_gapminder.csv')
df = pd.read_csv(file_path)

# Sidebar filters
years = sorted(df['year'].unique())
countries = sorted(df['country'].unique())

selected_year = st.sidebar.slider("Select Year", min_value=min(years), max_value=max(years), value=min(years))
selected_countries = st.sidebar.multiselect("Select Countries", options=countries, default=countries[:10])

# Filter data
filtered_df = df[(df['year'] == selected_year) & (df['country'].isin(selected_countries))]

# GNI range for consistent scaling
gni_min, gni_max = df['gniPPP'].min(), df['gniPPP'].max()

# Create static scatter plot for selected year
fig = px.scatter(
    filtered_df,
    x="gniPPP",
    y="lifeExp",
    size="population",
    color="country",
    hover_name="country",
    log_x=True,
    size_max=40,
    range_x=[gni_min, gni_max],
    range_y=[df['lifeExp'].min(), df['lifeExp'].max()],
    title=f"Life Expectancy vs. GNI per Capita in {selected_year}"
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)
