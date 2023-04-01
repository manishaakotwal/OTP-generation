
import math
import random
import smtplib


# generating random 6-digit otp
digits = "0123456789"
OTP = ""
for i in range(0, 6):
    OTP = OTP + digits[math.floor(random.random()*10)]
message = OTP + " " +"OTP verification and its your One time password"


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("manishakotwal502@gmail.com", "kxiz wysi wxnq qvak")    # emailid and app password required for sending mail
email = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', email, message)    # sending otp via email 


# verifying otp
passcode = input("Enter your OTP: ")
if passcode == OTP:
    print("Verified")
else:
    print("Invalid OTP")