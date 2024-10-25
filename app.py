import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Streamlit app title
st.title('MedLab Project')

# Project Overview Section
st.subheader("Project Overview")
st.write("""
**MedLab Sim** is a cutting-edge initiative focused on creating an AI-powered tool to streamline drug discovery. 
Our first goal is to develop a predictive model that estimates critical drug properties, starting with solubility, 
to help researchers save time and resources on early-stage experiments.
""")

st.subheader("Why This Project Matters")
st.write("""
MedLab Sim accelerates the drug discovery process by simulating essential drug properties, allowing us to filter out 
less promising compounds quickly. It’s also a unique educational tool, giving students hands-on experience with 
AI applications in pharmacy and medicine, while building a strong foundation for further developments in the future.
""")

# Founder Information
st.write("_Founded by: Haval, a pharmacy student at UEA, Norwich, UK._")

# Invitation to Fill the Form
st.markdown("<p style='color:#d9534f; font-weight:bold; margin-top:20px;'>If you are interested, please fill the form below.</p>", unsafe_allow_html=True)

# Streamlit form
with st.form("collaboration_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Valid Email Address")
    academic_status = st.text_input("Your Academic Status (e.g., '3rd-year Pharmacy Student at UEA')")
    skills = st.text_area("Skill(s) (e.g., research, data analysis, drug formulation, etc.)")
    hours = st.slider("How many hours are you willing to work on the project (per week)?", 1, 10)
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
    if full_name and email and academic_status and skills:
        # Define the message after form submission
        st.success("Thank you for submitting your information, we'll be in touch soon via email.")
        
        # Define the email content
        email_subject = "Confirmation of Information Submission"
        email_body = f"Dear {full_name},\n\n" \
                     "Thank you for submitting your information to the MedLab Project: Collaboration Hub. " \
                     "We have received your details, and one of our team members will be in touch with you soon to discuss the next steps.\n\n" \
                     "Best regards,\n" \
                     "The MedLab Team"
        
        # Send confirmation email
        send_email(email, email_subject, email_body)
    else:
        st.error("Please complete all fields before submitting.")
