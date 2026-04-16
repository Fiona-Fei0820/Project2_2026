import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

from_email = "3313409739@qq.com"
from_password = "yrdaviqjpydecigj"
to_email = "3215640696@qq.com"
last_email_time = 0
email_interval = 21600  # 6小时 = 6*60*60 秒
def send_notification():    
 global last_email_time    
 current_time = time.time()    
 if current_time - last_email_time < email_interval:        
  return    
 msg = EmailMessage()    
 msg.set_content("WARNING: Soil is DRY. Please water your plant!")    
 msg['From'] = from_email    
 msg['To'] = to_email    
 msg['Subject'] = "Raspberry Pi Plant Monitor: NEED WATER"
 server = smtplib.SMTP('smtp.qq.com', 587)    
 server.starttls()    
 server.login(from_email, from_password)    
 server.send_message(msg)    
 server.quit()    
 print("Notification email sent!")    
 last_email_time = current_time
def monitor_soil(channel):    
 if GPIO.input(channel):        
  print("Soil is DRY → Need water")        
  send_notification()    
 else:        
  print("Soil is WET → No need water")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500)
GPIO.add_event_callback(channel, monitor_soil)
print("Plant moisture monitor running...")
while True:    
 time.sleep(2)
