# Introduction
# Google Trends gives us an estimate of search volume.
# Let's explore if search popularity relates to other kinds of data.
# Perhaps there are patterns in Google's search volume and the price of Bitcoin or a hot stock like Tesla.
# Perhaps search volume for the term "Unemployment Benefits" can tell us something about the actual unemployment rate?
# Import Statements

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the Data

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')

# Data Exploration

print(f"Shape of TESLA\n{df_tesla.shape}\n")

print(f"Columns of TESLA\n{df_tesla.columns}\n")

pd.set_option('display.float_format', '{:.2f}'.format)
df_tesla.describe()

print(df_tesla.head())

print(f'Largest value for Tesla in Web Search:\n ', df_tesla["TSLA_WEB_SEARCH"].max())
print(f'Smallest value for Tesla in Web Search:\n ', df_tesla["TSLA_WEB_SEARCH"].min())

print(f"\nShape of unemployment\n{df_unemployment.shape}")

print(f"\n{df_unemployment.head()}")

df_unemployment.describe()

print('\nLargest value for "Unemployemnt Benefits" '
      f'in Web Search:\n ', df_unemployment["UE_BENEFITS_WEB_SEARCH"].max())

print(df_btc_search.shape)
print(f"\nShape of BITCOIN\n{df_btc_price.shape}")
print(f"\n{df_btc_search.head()}")

print(f'\nlargest BTC News Search: \n', df_btc_search["BTC_NEWS_SEARCH"].max())

# Data Cleaning
# Check for Missing Values

print(f'Missing values for Tesla?: ', df_tesla.isnull().values.any())
print(f'Missing values for U/E?: ', df_unemployment.isnull().values.any())
print(f'Missing values for BTC Search?: ', df_btc_search.isnull().values.any())
print(f'Missing values for BTC price?: ', df_btc_price.isnull().values.any())
print(f'Number of missing values: ', df_btc_price.isnull().sum().sum())

print(f"{df_btc_price[df_btc_price.CLOSE.isna()]}")

# Removing Null Values
df_btc_price.dropna(inplace=True)

print(f'\nMissing values for BTC price?:\n ', df_btc_price.isnull().values.any())

# Convert Strings to DateTime Objects

df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
print(f"\nTESLA dataframe datatypes \n{df_tesla.dtypes}")

df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])
print(f"\nUNEMPLOYMENT dataframe datatypes \n{df_unemployment.dtypes}")

df_btc_search["MONTH"] = pd.to_datetime(df_btc_search["MONTH"])
print(f"\nBITCOIN SEARCH dataframe datatypes\n {df_btc_search.dtypes}")

df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])
print(f"\nBITCOIN PRICE dataframe datatypes\n{df_btc_price.dtypes}")

# Converting from Daily to Monthly Data

df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(f"\ndf_btc_price monthly\n{df_btc_monthly.head()}")

# Data Visualisation
# Create locators for ticks on the time axis
# Register date converters to avoid warning messages
# Tesla Stock Price v.s. Search Volume

# |--------------------------------------------------------------------|
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)

# |-------------------------------X-------------------------------------|

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("TSLA Stock Price", color="#E6232E")
ax2.set_ylabel("Search Trend", color="skyblue")

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E")
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue")
# |--------------------------------------------------------------------|

# |--------------------------------------------------------------------|

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontdict={"fontsize": 14})
ax2.set_ylabel("Search Trend", color="skyblue", fontdict={"fontsize": 14})

ax1.tick_params(axis='x', labelrotation=45, labelsize=14)

ax1.set_ylim((0.0, 600.0))
ax1.set_xlim((df_tesla.MONTH.min(), df_tesla.MONTH.max()))

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)

"""How to add tick formatting for dates on the x-axis."""

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontdict={"fontsize": 14})
ax2.set_ylabel("Search Trend", color="skyblue", fontdict={"fontsize": 14})

ax1.tick_params(axis='x', labelrotation=45, labelsize=14)

ax1.set_ylim((0, 600))
ax1.set_xlim((df_tesla.MONTH.min(), df_tesla.MONTH.max()))

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)

# Bitcoin (BTC) Price v.s. Search Volume
# |--------------------------------------------------------------------|

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)

plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("BTC Price", fontsize=14, color="orange")
ax2.set_ylabel("Search Trend", fontsize=14, color="skyblue")

ax1.set_ylim((0, 15000))
ax1.set_xlim((df_btc_search.MONTH.min(), df_btc_search.MONTH.max()))

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

ax1.plot(df_btc_search.MONTH, df_btc_monthly.CLOSE, color="orange", linewidth=3, linestyle="--")
ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, color="skyblue", linewidth=3, marker="o")

# Unemployment Benefits Search vs. Actual Unemployment in the U.S.
# |--------------------------------------------------------------------|

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("FRED U/E Rate", fontsize=14, color="purple")
ax2.set_ylabel("Search Trend", fontsize=14, color="skyblue")

ax1.set_ylim((3, 10.5))
ax1.set_xlim((df_unemployment.MONTH.min(), df_unemployment.MONTH.max()))

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color="purple", linewidth=3, linestyle="--")
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)

# |--------------------------------------------------------------------|

roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("FRED U/E Rate", fontsize=14, color="purple")
ax2.set_ylabel("Search Trend", fontsize=14, color="skyblue")

ax1.set_ylim((3, 10.5))
ax1.set_xlim((df_unemployment.MONTH.min(), df_unemployment.MONTH.max()))

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

# ax1.grid(color='grey', linestyle='--')

ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, color="purple", linewidth=3, linestyle="--")
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)

# Including 2020 in Unemployment Charts

df_unemployment_2020 = pd.read_csv("data/UE Benefits Search vs UE Rate 2004-20.csv")
df_unemployment_2020["MONTH"] = pd.to_datetime(df_unemployment_2020["MONTH"])

# |--------------------------------------------------------------------|

plt.figure(figsize=(14, 8), dpi=150)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate 2020', fontsize=18)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("FRED U/E Rate", fontsize=14, color="red")
ax2.set_ylabel("Search Trend", fontsize=14, color="skyblue")

ax1.set_xlim((df_unemployment_2020.MONTH.min(), df_unemployment_2020.MONTH.max()))

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

ax1.plot(df_unemployment_2020.MONTH, df_unemployment_2020.UNRATE, color="red", linewidth=3)
ax2.plot(df_unemployment_2020.MONTH, df_unemployment_2020.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)
plt.show()
