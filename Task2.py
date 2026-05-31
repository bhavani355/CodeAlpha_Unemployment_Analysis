# =========================================================
# UNEMPLOYMENT ANALYSIS WITH PYTHON
# =========================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv(r"C:\Users\testm\OneDrive\Desktop\Unemployment in India.csv")

# =========================================================
# DATA CLEANING
# =========================================================

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Rename columns
df.columns = [
    'Region',
    'Date',
    'Frequency',
    'Estimated_Unemployment_Rate',
    'Estimated_Employed',
    'Estimated_Labour_Participation_Rate',
    'Area'
]

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Remove missing values
df.dropna(inplace=True)

# =========================================================
# BASIC INFORMATION
# =========================================================

print("\n================ DATASET INFO ================\n")
print(df.info())

print("\n================ FIRST 5 ROWS ================\n")
print(df.head())

print("\n================ MISSING VALUES ================\n")
print(df.isnull().sum())

print("\n================ BASIC ANALYSIS ================\n")

print("Average Unemployment Rate : ",
      round(df['Estimated_Unemployment_Rate'].mean(), 2))

print("Maximum Unemployment Rate : ",
      round(df['Estimated_Unemployment_Rate'].max(), 2))

print("Minimum Unemployment Rate : ",
      round(df['Estimated_Unemployment_Rate'].min(), 2))

# =========================================================
# GRAPH 1 : UNEMPLOYMENT TREND OVER TIME
# =========================================================

avg_unemployment = df.groupby(
    'Date'
)['Estimated_Unemployment_Rate'].mean()

plt.figure(figsize=(14,6))

plt.plot(
    avg_unemployment.index,
    avg_unemployment.values,
    marker='o',
    linewidth=3
)

plt.title(
    "Average Unemployment Rate Over Time",
    fontsize=18
)

plt.xlabel("Date", fontsize=14)
plt.ylabel("Unemployment Rate (%)", fontsize=14)

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()
plt.show()

# =========================================================
# GRAPH 2 : TOP 10 STATES WITH HIGHEST UNEMPLOYMENT
# =========================================================

state_avg = df.groupby(
    'Region'
)['Estimated_Unemployment_Rate'].mean()

top_states = state_avg.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

top_states.plot(kind='bar')

plt.title(
    "Top 10 States with Highest Unemployment",
    fontsize=16
)

plt.xlabel("States", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# =========================================================
# GRAPH 3 : AREA WISE COMPARISON
# =========================================================

area_avg = df.groupby(
    'Area'
)['Estimated_Unemployment_Rate'].mean()

plt.figure(figsize=(8,5))

area_avg.plot(kind='bar')

plt.title(
    "Urban vs Rural Unemployment",
    fontsize=16
)

plt.xlabel("Area", fontsize=12)
plt.ylabel("Average Unemployment Rate (%)", fontsize=12)

plt.tight_layout()
plt.show()

# =========================================================
# GRAPH 4 : COVID-19 IMPACT ANALYSIS
# =========================================================

covid_data = df[df['Date'].dt.year == 2020]

monthly_unemployment = covid_data.groupby(
    covid_data['Date'].dt.month
)['Estimated_Unemployment_Rate'].mean()

plt.figure(figsize=(12,6))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker='o',
    linewidth=3
)

plt.title(
    "Covid-19 Impact on Unemployment in 2020",
    fontsize=18
)

plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Unemployment Rate (%)", fontsize=14)

plt.grid(True)

plt.tight_layout()
plt.show()

# =========================================================
# GRAPH 5 : SEASONAL TREND ANALYSIS
# =========================================================

df['Month'] = df['Date'].dt.month_name()

seasonal = df.groupby(
    'Month'
)['Estimated_Unemployment_Rate'].mean()

months_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

seasonal = seasonal.reindex(months_order)

plt.figure(figsize=(14,6))

plt.plot(
    seasonal.index,
    seasonal.values,
    marker='o',
    linewidth=3
)

plt.title(
    "Seasonal Trend in Unemployment",
    fontsize=18
)

plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Unemployment Rate (%)", fontsize=14)

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()
plt.show()

# =========================================================
# FINAL INSIGHTS
# =========================================================

print("\n================ INSIGHTS ================\n")

print("1. Covid-19 caused a sharp rise in unemployment.")
print("2. Some states consistently show higher unemployment.")
print("3. Urban and Rural unemployment rates are different.")
print("4. Seasonal unemployment patterns are visible.")
print("5. Data analysis helps in economic policy planning.")

print("\n=============== PROJECT COMPLETED ===============")