import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class data_base:
    def send_email(self,receiver_email, body, attachments=None):
        msg = MIMEMultipart()
        msg['From'] = "gokulavasan640@gmail.com"
        msg['To'] = receiver_email
        msg['Subject'] = 'Git hub ci/cd project'

    # Attach text
        msg.attach(MIMEText(body, 'plain'))

    # Attach files (images)
        if attachments:
            for file in attachments:
                part = MIMEApplication(file['data'].read())
                part.add_header(
                'Content-Disposition',
                f'attachment; filename="{file["filename"]}"'
            )
                msg.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("gokulavasan640@gmail.com", "xvao kbab zjqi ffzh")
            server.sendmail("gokulavasan640@gmail.com", receiver_email, msg.as_string())
            return "Email sent successfully!"
        except Exception as e:
            print(e)
            return "Error: Unable to send email."
        finally:
            server.quit()




