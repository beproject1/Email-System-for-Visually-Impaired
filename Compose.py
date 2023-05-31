import AudioManager
import smtplib
from email.message import EmailMessage
import csv
from csv import writer
import sys
import os

audio_input_handler_compose = AudioManager.AudioInputHandler()
program_talkback_compose = AudioManager.ProgramTalkback()

class ComposeMail:
    
    def __init__(self):
        self.receiver = "groupprojectblind@gmail.com"
        self.subject = "your_subject_here"
        self.body = "Your Email Body here"
        #self.dict = {"ayush":"aayushagarwal764@gmail.com", "simran":"simrann2002@gmail.com", "groupproject": "groupprojectblind@gmail.com", "shaunak": "shaun.salunke@gmail.com", "yukta": "yuktak17@gmail.com"}

        
    def sendEmail(self):
        self.instantiateTLSServer()
        self.initiateLogin()
        self.setEmailContent()

    def instantiateTLSServer(self):
        self.mail_sending_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.mail_sending_server.starttls()
    
    def initiateLogin(self):
        with open("your_email_id_and_password.txt", mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.mail_sending_server.login(row['email_id'], row['password'])
                
                
    def setEmailContent(self):
        flagUserNotFound = 1
        self.email = EmailMessage()
        self.email["From"] = "groupprojectblind@gmail.com"
        self.receiver = self.receiver.replace(" ","")
        self.receiver = self.receiver.lower()
        with open('names_and_email_ids.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if(self.receiver in row['name']):
                    flagUserNotFound = 0
                    self.receiver = row['email_id']
                    break
        if(flagUserNotFound == 1): 
            self.addNewUserToDict()
            
        self.email["To"] = self.receiver
        print(self.receiver)
        self.email["subject"] = self.subject
        
        self.email.set_content(self.body)
            
        self.sendActualEmail(self.email)

    def sendActualEmail(self, email_to_be_sent):
        self.mail_sending_server.send_message(email_to_be_sent)
        print("Email sent successfully\n")
        program_talkback_compose.speak("Email sent successfully")
        print("Do you want to run the program again? Say one for yes and zero for no")
        program_talkback_compose.speak("Do you want to run the program again? Say one for yes and zero for no")
        print("Speak Now")
        program_talkback_compose.speak("Speak Now")
        user_choice = audio_input_handler_compose.startListening()
        print(user_choice)
        program_talkback_compose.speak(user_choice)
        if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold())):
            os.system("cls")
            os.system("python " + r'"Voice Based Email.py"')
        else:
            os.system("cls")
            sys.exit()

    def addNewUserToDict(self):
        program_talkback_compose.speak("This appears to be a New Recipient")
        print("This appears to be a New Recipient")
        newUser = self.receiver
        program_talkback_compose.speak("Speak the email id of the user")
        print("Speak the email id of the user")
        program_talkback_compose.speak("Speak Now")
        print("Speak Now")
        newEmailId = audio_input_handler_compose.startListening()
        newEmailId = newEmailId.replace(" ","")
        newEmailId = newEmailId.lower()
        if("atgmail.com".casefold() in newEmailId.casefold()):
            newEmailId = newEmailId.replace("atgmail.com", "@gmail.com")
            
        with open('names_and_email_ids.txt', mode='a') as csv_file:
            csv_writer = writer(csv_file)
            appendThis = [newUser, newEmailId]
            csv_writer.writerow(appendThis)
            csv_file.close()
        self.receiver = newEmailId
        
    
if __name__ == "__main__":
    compose_mail = ComposeMail()
    compose_mail.receiver = "ayush"
    compose_mail.subject = "Random Subject"
    compose_mail.body = "Random Email"

    
    compose_mail.sendEmail()
