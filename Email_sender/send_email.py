import smtplib

sender_email = input("Enter sender email: ")
receiver_email = input("Enter receiver email: ")

subject = input("Enter the subject: ")
body = input("Enter the body of the email: ")

message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, 'poht uora phdz aohu')
server.sendmail(sender_email, receiver_email, message)
print("Email sent successfully!")

server.quit()