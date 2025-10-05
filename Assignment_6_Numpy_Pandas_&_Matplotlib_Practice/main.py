import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Make a NumPy array of monthly Zakat collections (12 months). Show only the months above average.
zakat = np.array([1200, 950, 1100, 1300, 1600, 900, 1020, 1250, 1400, 980, 1150, 1700])

average_zakat = np.mean(zakat)
above_average_months = zakat[zakat > average_zakat]
print("Months with above average Zakat collections:", above_average_months)

# 2️⃣ Generate a 5×5 random NumPy matrix of deposits (in millions) for 5 Islamic banks across 5 years. Find max, min, mean, std.
deposits = np.random.randint(50, 500,size=(5,5)) 
# print(deposits)
print(f"Maximum Deposits are : {deposits.max()}")
print(f"Minimum Deposits are : {deposits.min()}")
print(f"Their mean is : {deposits.mean()}")
print(f"Their Standard Deviation is : {np.round(deposits.std(),2)}")

#3️⃣ Create a DataFrame with Surah_Number, Ayah_Count, Category (Makki/Madani). Show Surahs with more than 100 verses.
df = pd.read_csv('quran.csv')
print(df)


