import streamlit as st
from google_images_search import GoogleImagesSearch
import os
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

API_KEY = 'AIzaSyDOoBbvKUElPG2rO3vG2I7IwLEl9gu7Wbs'
CX = 'b2fb4e4d139c3479f'

gis = GoogleImagesSearch(API_KEY,CX)

def download_images(keyword,n):
    search_params = {
        'q': keyword,
        'num': n,
        'fileType': 'jpg|png',
        'searchType': 'image',
        'imgType': 'photo',
        'safe': 'medium',
        'imgSize': 'MEDIUM',
    }
    
    dir = "downloads"
    os.makedirs(dir, exist_ok=True)

    gis.search(search_params=search_params, path_to_dir=dir)
    return dir

def create_zip_file(dir, keyword):
    zip_filename = f"{keyword}_images.zip"
    zip_filepath = os.path.join(dir, zip_filename)
    
    with zipfile.ZipFile(zip_filepath, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(dir):
            for filename in filenames:
                if not filename.endswith(".zip"):
                    filepath = os.path.join(foldername, filename)
                    zipf.write(filepath, os.path.basename(filepath))
    
    return zip_filepath

def send_email(zip_filepath, recipient_mail):
    sender_email ='aarushibajaj2004@gmail.com'
    sender_password ='qupu gcky ptnd yxoq' 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_mail
    msg['Subject'] = "Your Downloaded Images"
    
    body = "Please find attached the zip file of the images you requested."
    msg.attach(MIMEText(body, 'plain'))

    with open(zip_filepath, "rb") as attachment:
        msg.attach(MIMEText(attachment.read(), 'base64', 'zip'))
        msg.add_header('Content-Disposition', f'attachment; filename={os.path.basename(zip_filepath)}')

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_mail, msg.as_string())
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")

st.title("Google Images Downloader")

keyword = st.text_input("Enter query to search images", "")
n= st.number_input("Number of images", min_value=1, max_value=100)
email = st.text_input("Enter your email address", "")
if st.button("Download"):
    if keyword:
        st.write(f"Downloading {n} images for '{keyword}'...")
        download_images(keyword, n)
        st.success(f"Images downloaded successfully for '{keyword}'!")
        zip_file = create_zip_file("downloads", keyword)
        if email:
            send_email(zip_file, email)
            st.success(f"Zip file sent to '{email}'!")
        else:
            st.error("Please enter a valid email address.")

    else:
        st.error("Please enter a keyword")
