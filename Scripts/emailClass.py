class EmailClass:
#Aurora Prediction emailClass.py
#--Last Version Changed: v1.3
#Created by AtomicYakuza on 10/01/2024
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def sendMail(self, receiverEmail, fileNames):
        # Email Configuration
        senderEmail = "atomicyakuza.git@gmail.com"
        password = "dqtm fzte wgft jhsz"

        # Create the email
        subject = "Subject: Aurora in the next 3 days!"
        body = "Please find attatched an .ics file for a calendar invite!"

        # Construct the email
        msg = self.MIMEMultipart()
        msg['From'] = senderEmail
        msg['To'] = receiverEmail
        msg['Subject'] = subject
        msg.attach(self.MIMEText(body, 'plain'))


        filename = "example.txt"  # File to attach

        for filename in fileNames:
            filePath = self.os.path.join(self.BASE_DIR, filename)

            filePath = "Calendar Events/"+filename
            fileFolder = filePath.split('/')[0]
            fileFolder = self.os.path.join(self.BASE_DIR, fileFolder)
            filePath = self.os.path.join(self.BASE_DIR, filePath)
            # Attach the file
            attachment = self.MIMEBase('application', 'octet-stream')
            with open(filePath, 'rb') as file:
                attachment.set_payload(file.read())

            self.encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename={filename}'
            )

            msg.attach(attachment)

        try:
            # Connect to the Gmail SMTP server
            server = self.smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            server.login(senderEmail, password)
            
            # Send the email
            server.sendmail(senderEmail, receiverEmail, msg.as_string())
            print("Email sent successfully!")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        finally:
            server.quit()