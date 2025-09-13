# Printing Surah Fatah using quran cloud API
import streamlit as st
import requests

st.set_page_config(page_title="سُورَةُ الفَتۡحِ", layout='centered')

response = requests.get("https://api.alquran.cloud/v1/surah/48")


if response.status_code == 200:
    info = response.json()["data"]
    st.title(info["name"])
    st.markdown("---")
    st.text("Surah Number :")
    st.text(info["number"])
    st.markdown("---")
    st.text("Total Ayahs :")
    st.text(info["numberOfAyahs"])
    st.markdown("---")
    surah = info["ayahs"]
    for ayah in surah:
        st.subheader(ayah["text"])
        st.text(ayah["numberInSurah"])
    st.markdown("---")