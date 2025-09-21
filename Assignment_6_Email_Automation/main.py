import streamlit as st
import pandas as pd
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Email Automation")
st.title("Email Automation")

st.write("Upload an Excel file with columns: Name, Email")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])


st.subheader("Email Account Settings")
email_address = st.text_input("Your Gmail Address")
email_password = st.text_input(
    "Your Gmail Password", type="password"
)

st.subheader("Message Settings")
subject = st.text_input("Email Subject", "Hello from our team")
body_template = st.text_area(
    "Email Body Template",
    "Hello {Name},\n\nThis is a test email.\n\nRegards,\nTeam",
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Contacts loaded:")
    st.dataframe(df)

if uploaded_file is not None and st.button("Send Emails"):
    if not email_address or not email_password:
        st.error("Please enter your Gmail and App Password.")
    else:
        success_count = 0
        fail_count = 0
        log_placeholder = st.empty()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_address, email_password)

                for _, row in df.iterrows():
                    msg = EmailMessage()
                    msg["Subject"] = subject
                    msg["From"] = email_address
                    msg["To"] = row["Email"]

                    # personalize the body
                    personalized_body = body_template.format(Name=row["Name"])
                    msg.set_content(personalized_body)

                    try:
                        smtp.send_message(msg)
                        success_count += 1
                        log_placeholder.write(f"Sent to {row['Email']}")
                    except Exception as e:
                        fail_count += 1
                        log_placeholder.write(
                            f"Failed to send to {row['Email']}: {e}"
                        )

            st.success(f"Done! Sent: {success_count}, Failed: {fail_count}")

        except Exception as e:
            st.error(f"Connection error: {e}")
