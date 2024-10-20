# Google Images Downloader App
This project is a web application hosted on Streamlit that allows users to search and download images from Google in bulk, based on a Query/Keyword they enter. It utilizes the **google_images_search** API to fetch and download images directly from Google.

**Key Features:**
-Keyword-based Image Search: Users can input a keyword to search for images related to their query (e.g., “Dogs” , “flowers” ,"Bikes").

-Image Quantity Selection: Allows users to choose the number of images to download (up to 100 images per search).

-ZIP File Creation: After downloading, the images are automatically zipped for convenient bulk download.

-Email Functionality: Users can also provide an email address, and the web app will send the zip file containing the images directly to their inbox.

-Responsive Design: The interface is user-friendly, clean, and responsive, built with Streamlit’s simple web framework.

**Interface**
![image](https://github.com/user-attachments/assets/e96b07ce-2b33-4e9b-b012-d134e9631782)

**How It Works:**
-User Input: The user inputs a keyword and specifies the number of images to download.

-Image Fetching: The app uses Google’s Custom Search API to fetch the desired images.

-File Compression: The images are saved in a folder and then compressed into a ZIP file.

Email: The user can have the ZIP file directly emailed to them.

**Backend Overview:**
-Google Images Search: The app uses the google_images_search Python package, which leverages Google’s Custom Search API to retrieve images.

-Email Sending: For email functionality, the app uses Python’s smtplib to send emails with attachments securely.

**Requirements:**
-Google API Key and Custom Search Engine ID(CX): The app requires a Google Custom Search API key and CX to fetch images.

-App Password for Gmail: The app uses an App Password for Gmail instead of traditional email passwords, ensuring secure email sending via SMTP.

**Output Screen**
![image](https://github.com/user-attachments/assets/ad10dcb5-50fd-4f9e-942d-051e9ad08e07)

