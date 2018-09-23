import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect('localhost', 8000)
#Next, log in to the server
server.login("karan.sheth@somaiya.edu", "toastsandwhich")

def sendConfirmationMail(number, receiver):
    try:
        message = """From: Schemio admin@schemio.io
            
            Subject: Confirm Your Email

            Enter the pin on the website.\n The pin is """+str(number)+". "
    
        server.sendmail("karan.sheth@somaiya.edu", receiver, message)        
        print( "Successfully sent email")
    except SMTPException:
        print ("Error: unable to send email")