# Install necessary dependencies
!apt-get update
!apt-get install -y wget curl unzip libvulkan1 chromium-browser xvfb  # Add Xvfb for virtual display

# Install Selenium and WebDriver Manager
!pip install selenium webdriver-manager

# Import libraries
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Set up a virtual display (required in Colab)
os.system("Xvfb :99 -screen 0 1024x768x16 &")
os.environ["DISPLAY"] = ":99"

# Set up Chrome options (headless mode for Colab compatibility)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.set_page_load_timeout(120)
    print("WebDriver initialized successfully.")
except Exception as e:
    print(f"Failed to initialize WebDriver: {e}")
    driver = None

if driver:
    try:
        # Open the desired URL
        url = "https://youtu.be/iTmlw3vQPSs"
        print(f"Opening URL: {url}")
        driver.get(url)

        # Wait for the page to load completely
        WebDriverWait(driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("Page loaded successfully.")

        # Extract the meta description
        try:
            description = driver.find_element(By.CSS_SELECTOR, "meta[name='description']").get_attribute("content")
            print(f"Description: {description}")
        except Exception as e:
            print(f"Error extracting description: {e}")
            description = ""

        # Extract timestamps using regex
        timestamps = re.findall(r'\d{2}:\d{2}', description)
        print("Timestamps found:", timestamps)

        # Save the results to a file
        timestamp_list = "\n".join(timestamps)
        text_content = f"URL: {url}\n\nTimestamps:\n{timestamp_list}"

        file_path = "/content/timestamps.txt"
        with open(file_path, "w") as file:
            file.write(text_content)
        print(f"Timestamps saved to {file_path}")

        # Send email with results
        def send_email():
            sender_email = "vinayvasantham7@gmail.com"
            receiver_email = "hr@rapidken.ai"
            password = "nhhi wsov whur bddh"

            subject = "YouTube Timestamps"
            body = f"Please find below the YouTube video URL and timestamps:\n\n{text_content}"

            # Set up the email message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Attach the text file
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {'timestamps.txt'}",
                )
                msg.attach(part)

            # Send the email
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())
                print("Email sent successfully!")
            except Exception as e:
                print("Error sending email:", e)

        send_email()

    except Exception as e:
        print(f"Error during processing: {e}")
    finally:
        # Ensure browser is closed
        print("Closing the browser...")
        driver.quit()
else:
    print("WebDriver not initialized. Aborting execution.")
