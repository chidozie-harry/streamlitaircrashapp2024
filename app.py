import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sn

# Load dataset
df = pd.read_csv('aircrahesFullDataUpdated_2024.csv')


# Group by year and count crashes
accidents_per_year = df['Year'].value_counts().sort_index()

# Plot in Streamlit
st.subheader('Air Crashes Over Time')
st.line_chart(accidents_per_year)
# Count crashes by airline
airline_crashes = df['Aircraft'].value_counts().head(10)

# Plot in Streamlit
st.subheader('Top 10 Aircraft with Highest Number of Crashes')
st.bar_chart(airline_crashes)
# Count crashes by airline
airline_crashes = df['Aircraft'].value_counts().head(10)

# Plot in Streamlit
st.subheader('Top 10 Aircraft with Highest Number of Crashes')
st.bar_chart(airline_crashes)
st.header('Top 10 Aircraft Manufacturers Involved in Crashes')
plt.figure(figsize=(10, 6))
plt.title('Top 10 Aircraft Manufacturers Involved in Crashes')
plt.xlabel('Aircraft Manufacturer')
plt.ylabel('Number of Crashes')
st.pyplot(plt)
# 5. Fatalities Over Time
st.header('Fatalities Over Time')
fatalities_per_year = df.groupby('Year')['Fatalities (air)'].sum()
plt.figure(figsize=(10, 6))
plt.plot(fatalities_per_year.index, fatalities_per_year.values, marker='o', linestyle='-', color='r')
plt.title('Total Fatalities per Year')
plt.xlabel('Year')
plt.ylabel('Total Fatalities')
st.pyplot(plt)

# Option to download the filtered data
st.header('Download the filtered data')
st.write("You can download the filtered dataset as a CSV file.")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(label="Download CSV", data=csv, file_name='filtered_aircrashes_data.csv', mime='text/csv')