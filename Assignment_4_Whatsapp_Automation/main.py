import streamlit as st
import pandas as pd
import pywhatkit as kit
import time
import pyautogui

st.set_page_config(page_title="Whatsapp Sender Automation", layout="centered")
st.title("Whatsapp Automation System")
upload = st.file_uploader("Upload Your Excel File", type=["xlsx"])

Message = st.text_area("Enter your Message Here ", "Follow me On github and Linkedin, https://github.com/MuhammadUsman-Khan, https://www.linkedin.com/in/muhammad-usman-khan-bb3607336/")
reminder = st.text_input("Enter your reminder", "It is a remainder message")
if upload is not None:
    df = pd.read_excel(upload)
    st.write("Contacts Uploaded")
    st.dataframe(df)
    if st.button("Send Message"):

        for index, row in df.iterrows():
            name=f"{row["name"]}"
            phonenumber = f"+{row["phone"]}"
            certification_status = f"{row["certification status"]}"
            
            try:
                if certification_status == "yes" or certification_status == "Yes":
                    kit.sendwhatmsg_instantly(phonenumber, reminder, wait_time=35)
                    time.sleep(10)
                    print(f"Sent to {name}, {phonenumber}")
                    time.sleep(5)
                    pyautogui.press("enter")
                
                else:
                    kit.sendwhatmsg_instantly(phonenumber, Message, wait_time=35)
                    time.sleep(10)
                    print("Sent")
                    time.sleep(5)
                    pyautogui.press("enter")

            except Exception as e:
                print(f"Number not send {name}, {phonenumber}")

