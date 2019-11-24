import smtplib
import os
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect('localhost', 8000)
# Next, log in to the server
server.login(os.environ.get('email'), os.environ.get('password'))

def sendConfirmationMail(number, receiver):
    try:
       message = """
            Enter the pin on the website.\n Your unique super secret pin is """+str(number)+". "

        server.sendmail(os.environ.get('email'), receiver, message)
        print( "Successfully sent email")
    except SMTPException:
        print ("Error: unable to send email")