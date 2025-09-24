# 1: Even odd using lambda function
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(10))

# 2: Marksheet using lambda function
marksheet = lambda percentage: "A+" if percentage >= 90 else ("A" if percentage >= 80 else ("B" if percentage >=70 else ("C" if percentage >= 60 else ("D" if percentage >= 50 else "F"))))

print(marksheet(85))

# 3: Surah Fetching using lambda function
import requests
surah_name = lambda x: requests.get(f"https://api.alquran.cloud/v1/surah/{x}").json()["data"]["englishName"] if requests.get(f"https://api.alquran.cloud/v1/surah/{x}").status_code == 200 else "Error fetching data"
print(surah_name(5))