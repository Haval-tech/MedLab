import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Streamlit app title
st.title('Pharmacy Collaboration Lab')

# Streamlit form
with st.form("collaboration_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")

# Define email sending function
def send_email(recipient_email, subject, body):
    sender_email = "halo.wigan@gmail.com"  # Your email
    sender_password = "snod ncei ellk xxzb"  # Your app-specific password

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

# Handle form submission
if submit_button:
    if "pharmacy" in name.lower() or "pharmacy" in email.lower():
        # Send acceptance email
        send_email(email, "Accepted", f"Hello {name}, you've been accepted into the collaboration!")
        st.success(f"Congratulations {name}, you've been accepted!")
    else:
        # Send rejection email
        send_email(email, "Not Accepted", f"Hello {name}, unfortunately, you were not accepted.")
        st.warning(f"Sorry {name}, you did not meet the criteria.")
