import smtplib
from email.message import EmailMessage


from_email_addr = "3313409739@qq.com"

from_email_pass = "yrdaviqjpydecigj"
to_email_addr = "3215640696@qq.com"

msg = EmailMessage()
msg.set_content("Plant is TOO DRY! Please water it!")
msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = "Raspberry Pi: Plant Needs Water"

server = smtplib.SMTP('smtp.qq.com', 587)
server.starttls()
server.login(from_email_addr, from_email_pass)
server.send_message(msg)
print("Email sent successfully")
server.quit()
